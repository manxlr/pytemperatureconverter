from setuptools import setup, find_packages

setup(
    name="pytemperatureconverter",
    version="1.1.0",
    author="Zeeshan Khalid",
    author_email="nszeeshankhalid@gmail.com",
    description="A simple Python library to convert temperatures between four scales (Celsius, Fahrenheit, Kelvin, and Rankine) with warnings for physically impossible conversions.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/manxlr",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
