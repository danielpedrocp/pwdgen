from pwdgen.generator import generate_secure_password
from pwdgen.validator import is_secure_password

def test_secure_password_meets_criteria():
    pwd = generate_secure_password()
    assert is_secure_password(pwd), "Password does not meet security requirements"