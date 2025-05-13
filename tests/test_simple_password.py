from pwdgen.validator import (
    is_numeric_only,
    has_special_chars,
    has_uppercase,
    has_lowercase,
    has_digit
)

def test_is_numeric_only():
    assert is_numeric_only("123456"), "Should return True for numeric-only input"

def test_has_special_chars():
    assert has_special_chars("abc@123"), "Should return True for input with special char"

def test_has_uppercase():
    assert has_uppercase("abcD"), "Should return True for input with uppercase letter"

def test_has_lowercase():
    assert has_lowercase("ABCd"), "Should return True for input with lowercase letter"

def test_has_digit():
    assert has_digit("pass123"), "Should return True for input with digit"