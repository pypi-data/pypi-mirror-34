# Package Test

This is a small test about distribution.

## Generate distribution archives

`python setup.py sdist bdist_wheel`

## Upload to TestPyPi

Test PyPI is a separate instance of the package index intended for testing and experimentation.

install twint: `pip install twine`

upload: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

## Install

`pip install --index-url https://test.pypi.org/simple/ pypi_pkg_test`

## Usage

```python
from pypi_pkg_test.main import hello


print(hello())  # hello jason
```