"""
Temperature Conversion Package
===============================
This package provides functions to convert temperatures between Celsius, Fahrenheit, Kelvin, and Rankine scales.

Functions:
----------
- celsius_to_fahrenheit(c)
- celsius_to_kelvin(c)
- celsius_to_rankine(c)
- fahrenheit_to_celsius(f)
- fahrenheit_to_kelvin(f)
- fahrenheit_to_rankine(f)
- kelvin_to_celsius(k)
- kelvin_to_fahrenheit(k)
- kelvin_to_rankine(k)
- rankine_to_celsius(r)
- rankine_to_fahrenheit(r)
- rankine_to_kelvin(r)
"""

from .functions import *

# Package metadata
__version__ = "1.2.0"
__author__ = "Zeeshan Khalid"
__email__ = "nszeeshankhalid@gmail.com"

__all__ = [
    "celsius_to_fahrenheit",
    "celsius_to_kelvin",
    "celsius_to_rankine",
    "fahrenheit_to_celsius",
    "fahrenheit_to_kelvin",
    "fahrenheit_to_rankine",
    "kelvin_to_celsius",
    "kelvin_to_fahrenheit",
    "kelvin_to_rankine",
    "rankine_to_celsius",
    "rankine_to_fahrenheit",
    "rankine_to_kelvin",
]
