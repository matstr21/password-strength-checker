import re

def check_password_strength(password):
    """Checks the strength of a password based on basic criteria."""

    length_ok = len(password) >= 8
    has_uppercase = bool(re.search(r'[A-Z]', password))
    has_lowercase = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    strength = 0

    if length_ok:
        strength += 1
    if has_uppercase:
        strength += 1
    if has_lowercase:
        strength += 1
    if has_digit:
        strength += 1
    if has_special:
        strength += 1

    if strength == 5:
        return "Strong password!"
    elif strength >= 3:
        return "Medium password."
    else:
        return "Weak password."

# Example usage:
password = input("Enter your password: ")
result = check_password_strength(password)
print(result)
