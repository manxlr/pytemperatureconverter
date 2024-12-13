
# 📦 pytemperatureconverter

### A simple Python library to convert temperatures between four scales (Celsius, Fahrenheit, Kelvin, and Rankine) with user warnings for physically impossible conversions

`pytemperatureconverter` is a lightweight and easy-to-use Python package that provides functions to seamlessly convert temperatures across multiple scales. It includes robust warnings to prevent erroneous or physically impossible conversions, ensuring accurate and reliable temperature conversions.

---

## 🔍 **Key Features**

- **Support for All Major Temperature Scales**: Easily convert temperatures between:
  - Celsius ↔ Fahrenheit  
  - Celsius ↔ Kelvin  
  - Celsius ↔ Rankine  
  - Fahrenheit ↔ Kelvin  
  - Rankine ↔ Celsius  

- **User Input Warnings**: Prevents conversions that result in physically impossible temperatures (e.g., temperatures below absolute zero).
  
- **Comprehensive Test Coverage**: Includes robust test cases to ensure reliable conversions and edge case handling.

- **Open-Source Project**: Fully transparent and open for contributions under the MIT license.

---

## 📝 **Table of Contents**
1. [Installation](#installation)
2. [Usage](#usage)
3. [API Reference](#api-reference)
4. [Testing](#testing)
5. [Changelog](#changelog)
6. [Contribution](#contribution)
7. [License](#license)
8. [Contact](#contact)
9. [Donations](#donations)

---

## 📦 **Installation**

Install the `pytemperatureconverter` library from PyPI:

```bash
pip install pytemperatureconverter
```

---

## 🚀 **Usage**

Here's a quick example to demonstrate some of the conversions:

```python
from pytemperatureconverter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

# Celsius to Fahrenheit
temp_c = 25
print(f"{temp_c}°C is {celsius_to_fahrenheit(temp_c)}°F")

# Fahrenheit to Celsius
temp_f = 100
print(f"{temp_f}°F is {fahrenheit_to_celsius(temp_f)}°C")

# Celsius to Kelvin
print(f"{temp_c}°C is {celsius_to_kelvin(temp_c)}K")

# Kelvin to Celsius
temp_k = 300
print(f"{temp_k}K is {kelvin_to_celsius(temp_k)}°C")
```

---

## 🛡️ **User Warnings**

- The library now includes **validation mechanisms** to prevent **physically impossible conversions**.
- Temperatures that would result in unrealistic or negative Kelvin conversions will trigger appropriate warnings.
- This ensures that only meaningful and valid conversions are processed.

---

## ✅ **Testing**

We have included comprehensive test cases to ensure:

- Accurate conversions across all supported temperature scales.
- Handling of edge cases (e.g., extreme temperatures).
- Robust input validation to catch erroneous or invalid conversions.

Run the test suite to verify the correctness of conversions:

```bash
pytest tests/
```

---

## 🔄 **Changelog**

### Latest Updates (v1.1.0)

- Added **User Input Validation** with warnings for physically impossible conversions.
- Included **new test cases** to cover all edge cases across temperature scales.
- Fully open-sourced the project, ensuring the MIT license allows for free copying and modification.

---

## 🤝 **Contribution**

We welcome contributions! If you have any improvements, bug fixes, or new test ideas, feel free to contribute to the repository:

- Fork the repository.
- Create a new branch.
- Submit a Pull Request with a detailed description of your changes.

### Repo Link: [https://github.com/manxlr](https://github.com/manxlr)

---

## 📜 **License**

This project is licensed under the **MIT License**, allowing you to freely use, modify, and distribute the code.

[MIT License](https://opensource.org/licenses/MIT)

---

## 📧 **Contact**

For any questions, suggestions, or feedback, please reach out:

- **Email**: [nszeeshankhalid@gmail.com](mailto:nszeeshankhalid@gmail.com)
- **GitHub**: [https://github.com/manxlr](https://github.com/manxlr)

---

## 💖 **Donations**

If you find this project helpful and would like to support its continued development, you can donate using the following cryptocurrency addresses:

- **Ethereum (ETH)**: `0x23774348bc491Ff70F39c63f39B0e542a59b5B14`  
- **Bitcoin (BTC)**: `bc1qp7wltg8frvecuujjs9f3ck28r0s0h0qzld2fu6`  
- **Dogecoin (DOGE)**: `DTbwxMs4wenN2kUea77rHPQ8nbJrSk4o7D`  

Your support is greatly appreciated and helps maintain and improve open-source projects!

---
