# Release Documentation

## 1. Install Required Tools
```bash
python -m pip install --upgrade build twine
```

## 2. Build Your Package
```bash
python -m build
```
This will create a `dist/` directory with `.whl` and `.tar.gz` files.

---

## 3. (Optional) Check Your Package

Run:

```bash
python -m twine check dist/*
```

This checks for common packaging errors.

---

## 4. Upload to PyPI

Run:

```bash
python -m twine upload dist/*
```

- Enter your PyPI username and password (or use an API token if you have one).

---

## 5. Test Your Package

After upload, verify installation from PyPI (ideally in a fresh virtual environment):

```bash
pip install dbconvert
```

Then test the CLI:

```bash
dbconvert --help
```
