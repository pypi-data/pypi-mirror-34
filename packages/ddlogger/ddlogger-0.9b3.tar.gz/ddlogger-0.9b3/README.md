# Dot Dot Logger

Prints dots to stdout to log the progress of a loop without knowing the total loops.

## Usage

```python
from ddlogger import DotDotLogger

def a_finite_generator():
    # ...
    # yield something

dl = DotDotLogger()
for item in a_finite_generator():
    # do something that does not contain "print" statement/function
    dl.update()  # prints a dot
```

Suppose in the above example the `a_finite_generator` returns an iterable of length 100, then it produces

	...............................................................................
	.....................

where each row contains at most 79 dots. To change the number of dots in a row or the shape of the dots, see `help(ddlogger.DotDotLogger)`.

## Installation

```bash
pip install ddlogger
```

or

```bash
pip3 install ddlogger
```
