import warnings

"""A simple python script to convert temperature between four scales"""

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    if c < -273.15:
        warnings.warn("Celsius value is below absolute zero!", UserWarning)
    return round(1.8 * c + 32, 2)

# Define a function to convert Celsius to Kelvin
def celsius_to_kelvin(c):
    if c < -273.15:
        warnings.warn("Celsius value is below absolute zero!", UserWarning)
    return round(c + 273.15, 2)

# Define a function to convert Celsius to Rankine
def celsius_to_rankine(c):
    if c < -273.15:
        warnings.warn("Celsius value is below absolute zero!", UserWarning)
    return round(1.8 * c + 491.67, 2)

# Define a function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    if f < -459.67:
        warnings.warn("Fahrenheit value is below absolute zero!", UserWarning)
    return round((f - 32) / 1.8, 2)

# Define a function to convert Fahrenheit to Kelvin
def fahrenheit_to_kelvin(f):
    if f < -459.67:
        warnings.warn("Fahrenheit value is below absolute zero!", UserWarning)
    return round((f + 459.67) / 1.8, 2)

# Define a function to convert Fahrenheit to Rankine
def fahrenheit_to_rankine(f):
    if f < -459.67:
        warnings.warn("Fahrenheit value is below absolute zero!", UserWarning)
    return round(f + 459.67, 2)

# Define a function to convert Kelvin to Celsius
def kelvin_to_celsius(k):
    if k < 0:
        warnings.warn("Kelvin value is below absolute zero!", UserWarning)
    return round(k - 273.15, 2)

# Define a function to convert Kelvin to Fahrenheit
def kelvin_to_fahrenheit(k):
    if k < 0:
        warnings.warn("Kelvin value is below absolute zero!", UserWarning)
    return round(1.8 * k - 459.67, 2)

# Define a function to convert Kelvin to Rankine
def kelvin_to_rankine(k):
    if k < 0:
        warnings.warn("Kelvin value is below absolute zero!", UserWarning)
    return round(1.8 * k, 2)

# Define a function to convert Rankine to Celsius
def rankine_to_celsius(r):
    if r < 0:
        warnings.warn("Rankine value is below absolute zero!", UserWarning)
    return round((r - 491.67) / 1.8, 2)

# Define a function to convert Rankine to Fahrenheit
def rankine_to_fahrenheit(r):
    if r < 0:
        warnings.warn("Rankine value is below absolute zero!", UserWarning)
    return round(r - 459.67, 2)

# Define a function to convert Rankine to Kelvin
def rankine_to_kelvin(r):
    if r < 0:
        warnings.warn("Rankine value is below absolute zero!", UserWarning)
    return round(r / 1.8, 2)

# Define an __all__ variable that lists the names of the functions you want to expose
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
