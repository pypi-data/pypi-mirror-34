import os
import sys
import time
from datetime import datetime
from bluepy.btle import Scanner

DEFAULT_FIELDS = ['appearance', 'manufacturer', 'complete local name']

class ScanResult():
    def __init__(self, manufacturer, appearance, localName, rssi):
        self.manufacturer = manufacturer
        self.appearance = appearance
        self.localName = localName
        self.rssi = rssi

    def __str__(self):
        return "ScanResult <manufacturer=%s appearance=%s localName=%s rssi=%ddB>" % (self.manufacturer, self.appearance, self.localName, self.rssi)

class BadgeBTLE():
    def __init__(self, manufacturer=None, appearance=None, scanTimeout=2, fields=[]):
        """Construct new BadgeBTLE instance.

        Args:
            manufacturer: Bluetooth Manufacturer ID [1] to scan for. Default is no filter.
            appearance: Optional Bluetooth Appearance ID [2] to scan for. If not set, defaults to current or upcoming DEF CON (e.g. 0x26dc).
            scanTimeout: Timeout for Bluetooth scan. Defaults to 2 seconds.

        References:
        [1] https://www.bluetooth.com/specifications/gatt/viewer?attributeXmlFile=org.bluetooth.characteristic.manufacturer_name_string.xml
        [2] https://www.bluetooth.com/specifications/gatt/viewer?attributeXmlFile=org.bluetooth.characteristic.gap.appearance.xml
        """
        self.scanner = Scanner()
        self.scanTimeout = scanTimeout
        self.manufacturer = manufacturer
        self.appearance = appearance if appearance else self.__determineAppearance()

    def __determineAppearance(self):
        year = datetime.now().year
        dcyear = year - 1992 # Calculate DEF CON year
        return "dc" + str(dcyear)

    def scan(self):
        """Perform Bluetooth scan until timeout and return list of nearby BLE devices
        with the specificed (or default) Appearance ID.

        Returns:
            A list of tuples containing these data points: Appearance ID, Manufacturer ID, Local Name, and Signal strength (RSSI).
        """
        devices = self.scanner.scan(self.scanTimeout)
        neighbors = []
        for dev in devices:
            appearance = None
            manufacturer = None
            localName = None
            for (adtype, desc, value) in dev.getScanData():
                if desc.lower() == "appearance":
                    appearance = value.lower()
                if desc.lower() == "manufacturer":
                    manufacturer = value[0:4]
                if desc.lower() == "complete local name":
                    localName = value
                if appearance == self.appearance and manufacturer is not None:
                    neighbors.append(ScanResult(manufacturer, appearance, localName, dev.rssi))
        self.scanner.clear()
        return neighbors
