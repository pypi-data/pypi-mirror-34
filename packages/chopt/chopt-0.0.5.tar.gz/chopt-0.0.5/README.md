# CHOOSE OPTIONS

*A simple CLI checkbox menu interface for choosing options.*

![img](./chopt.gif "Choose Options")

Takes a list of options as an argument and returns a list of selected items from
that list.

Options are chosen by entering their corresponding number (including specifying
ranges in the form 1..5 or 1-5), or using globbing to match option strings.

## INSTALLATION

`pip install chopt`

## CLI USAGE

```
usage: chopt [-h] options [options ...]

Create a checkbox menu from a list of options.

positional arguments:
  options     Options for the menu.

optional arguments:
  -h, --help  show this help message and exit
```

## PYTHON USAGE

```python
from chopt import chopt

my_list = [ 'item1', 'item2', 'item3' ]

chosen = chopt(my_list)

some_interesting_function(chosen)
```

## EXAMPLES

`chopt $(ls ~/src/chopt)`

`chopt $(tail -n 10 /usr/share/dict/words)`

`chopt options{1..12}`
