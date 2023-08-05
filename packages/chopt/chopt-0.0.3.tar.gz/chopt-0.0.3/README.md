# CHOOSE OPTIONS

*A simple CLI checkbox menu interface for choosing options.*

Takes a list of options as an argument and returns a list of selected items from
that list.

Options are chosen by entering their corresponding number, or using
wildcards/globbing to match entries.

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

![img](./img/scrot0.png "Choose")

![img](./img/scrot1.png "Result")

`chopt option1 option2 option3`

![img](./img/scrot2.png "Choose")

![img](./img/scrot3.png "Result")
