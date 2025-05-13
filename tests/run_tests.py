import argparse
import pytest

def main():
    parser = argparse.ArgumentParser(description="Run password generator tests.")
    parser.add_argument(
        "--module",
        choices=["secure", "simple", "all"],
        default="all",
        help="Which test module to run: secure, simple, or all (default)."
    )

    args = parser.parse_args()

    if args.module == "secure":
        pytest.main(["test_secure_password.py"])
    elif args.module == "simple":
        pytest.main(["test_simple_password.py"])
    else:  # all
        pytest.main(["test_secure_password.py", "test_simple_password.py"])

if __name__ == "__main__":
    main()