import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="badgebtle",
    version="0.1.3",
    author="Robert Bost",
    description="DEF CON badge bluetooth library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dczia/python-badgebtle",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        "bluepy"
    ]
)
