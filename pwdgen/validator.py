import re
import string

SPECIALS = string.punctuation

def is_secure_password(password: str, length: int = 8) -> bool:
    """
    Validates whether a password meets basic security requirements:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character
    - Minimum length
    """
    validator = fr'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[{re.escape(SPECIALS)}]).{{{length},}}$'
    
    return bool(re.match(validator, password))


def is_numeric_only(password: str) -> bool:
    return password.isdigit()


def has_special_chars(password: str) -> bool:
    return any(c in string.punctuation for c in password)


def has_uppercase(password: str) -> bool:
    return any(c.isupper() for c in password)


def has_lowercase(password: str) -> bool:
    return any(c.islower() for c in password)


def has_digit(password: str) -> bool:
    return any(c.isdigit() for c in password)