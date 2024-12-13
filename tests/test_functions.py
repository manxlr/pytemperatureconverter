import pytest
import warnings
from pytemperatureconverter import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    celsius_to_rankine,
    fahrenheit_to_celsius,
    fahrenheit_to_kelvin,
    fahrenheit_to_rankine,
    kelvin_to_celsius,
    kelvin_to_fahrenheit,
    kelvin_to_rankine,
    rankine_to_celsius,
    rankine_to_fahrenheit,
    rankine_to_kelvin,
)

# Suppress warnings during testing
@pytest.fixture(autouse=True)
def suppress_warnings():
    warnings.simplefilter("ignore", UserWarning)

def test_celsius_conversions():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_rankine(0) == 491.67
    assert celsius_to_fahrenheit(-273.15) == -459.67
    assert celsius_to_kelvin(-273.15) == 0.0
    assert celsius_to_rankine(-273.15) == 0.0

def test_fahrenheit_conversions():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_kelvin(32) == 273.15
    assert fahrenheit_to_rankine(32) == 491.67
    assert fahrenheit_to_celsius(-459.67) == -273.15
    assert fahrenheit_to_kelvin(-459.67) == 0.0
    assert fahrenheit_to_rankine(-459.67) == 0.0

def test_kelvin_conversions():
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_fahrenheit(273.15) == 32.0
    assert kelvin_to_rankine(273.15) == 491.67
    assert kelvin_to_celsius(0) == -273.15
    assert kelvin_to_fahrenheit(0) == -459.67
    assert kelvin_to_rankine(0) == 0.0

def test_rankine_conversions():
    assert rankine_to_celsius(491.67) == 0.0
    assert rankine_to_fahrenheit(491.67) == 32.0
    assert rankine_to_kelvin(491.67) == 273.15
    assert rankine_to_celsius(0) == -273.15
    assert rankine_to_fahrenheit(0) == -459.67
    assert rankine_to_kelvin(0) == 0.0