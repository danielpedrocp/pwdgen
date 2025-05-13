# pwdgen
A simple and customizable password generator written in Python.

## 🚧 Milestones

- [x] Generate password with lowercase, uppercase, and digits
- [ ] Add punctuation to password generation
- [ ] Implement CLI with argparse and `--help`
- [ ] Add unit and pytest-compatible tests
- [ ] Define and validate password security policy (min 8–12+ chars, mixed charset)
- [ ] Package for PyPI with `setup.py` or `pyproject.toml`
- [ ] Add version badge and metadata parsing to README
- [ ] Create `api` branch for containerized service (FastAPI)

# pwdgen

A simple and customizable password generator written in Python.

## 🚧 Milestones

- [x] Generate password with lowercase, uppercase, and digits
- [x] Add symbols to password generation
- [ ] Implement CLI with argparse and `--help`
- [X] Add unit and pytest-compatible tests
- [ ] Define and validate password security policy (min 8–12+ chars, mixed charset)
- [ ] Implement password entropy calculator
- [ ] Package for PyPI with `setup.py` or `pyproject.toml`
- [ ] Add version badge and metadata parsing to README
- [ ] Create `api` branch for containerized service (FastAPI)
- [ ] Add validator module and expose as future API"

## 📁 Project Structure

<pre><code>📦 pwdgen/
├── pwdgen/               # Main package
│   ├── __init__.py       # Package initializer
│   ├── generator.py      # Password generator
│   └── validador.py      # Password validator
│
├── tests/                # Automated tests
│   ├── run_tests.py
│   ├── test_secure_password.py
│   └── test_simple_password.py
│
├── .gitignore            # Git ignore rules
├── LICENSE               # MIT License
├── MANIFEST.in           # Declares files to include in the package
├── pyproject.toml        # Packaging metadata
└── README.md             # Project documentation
</code></pre>