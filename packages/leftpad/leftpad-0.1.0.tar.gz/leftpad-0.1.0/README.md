# leftpad
Left pad a string in Python. 
Done to try out creating a `pip` package and uploading it to the [Python Package Index (PyPI)](https://pypi.org/).

# Install
`pip install leftpad`

# Usage
```python
from leftpad import left_pad

left_pad("foo", 5)
// => "  foo"

left_pad("foobar", 6)
// => "foobar"

left_pad(1, 2, '0')
// => "01"

left_pad(17, 5, 0)
// => "00017"
```

## Testing
Run `python -m doctest leftpad.py`.