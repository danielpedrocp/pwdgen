import string
import random

LOWERS = string.ascii_lowercase
UPPERS = string.ascii_uppercase
DIGITS = string.digits
SPECIALS = string.punctuation

def generate_secure_password(length=8):
    """
    Generate a secure password with uppercase, lowercase, digits and symbols.
    """
    requirements = [LOWERS, UPPERS, DIGITS, SPECIALS]
    pool = [random.choice(req) for req in requirements]

    while len(pool) < length:
        req = random.choice(requirements)
        pool.append(random.choice(req))

    random.shuffle(pool)
    return ''.join(pool)

def generate_simple_password(
        length=8,
        use_digits=False,
        use_lowers=False,
        use_uppers=False,
        use_specials=False,
    ):
    """
    Generate a simple password. Charset type can optionally be selected using flags.
    """
    charset_flags = {
        use_digits: DIGITS,
        use_lowers: LOWERS,
        use_uppers: UPPERS,
        use_specials: SPECIALS,
    }

    charset = ''.join(chars for flag, chars in charset_flags.items() if flag)
    if not charset:
        charset = LOWERS + UPPERS + DIGITS

    return ''.join(random.choice(charset) for _ in range(length))