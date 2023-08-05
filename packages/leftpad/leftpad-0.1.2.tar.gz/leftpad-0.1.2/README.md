# leftpad
Left pad a string in Python. 
Created to try out making a `pip` package and uploading it to the [Python Package Index (PyPI)](https://pypi.org/).
Inspired by the [`left-pad` package on npm](https://www.npmjs.com/package/left-pad) which [broke parts of the internet](https://www.theregister.co.uk/2016/03/23/npm_left_pad_chaos/).

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