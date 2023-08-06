# CHOOSE OPTIONS

*A simple CLI checkbox menu interface for choosing options.*

![img](./chopt.gif "Choose Options")

Takes a list of options as an argument and returns a list of selected items from
that list.

Options are chosen by entering their corresponding number or name. Multiple
options can be selected in one go. Choices should be separated by spaces.

Also supported is specifying ranges of numbers, in the form *x..y* or *x-y*
(where *x* and *y* are item numbers from the list, eg) 1..5 or 1-5).

Additionally you can use *..x* or *-x* to specify everything up to the number
*x*, and *x..* or *x-* to specify everything from the number *x* until the last
element.

Finally one can use wildcard globbing to match option name strings. For instance
**.py* would match all files with the extension *.py*.

Reserved words are *toggle*, *reset*, *accept* and *quit* (case insensitive). They can
be used to carry out those respective actions. Typing just the first letter also
carries out that action - ie) *t*, toggles all, *r*, resets, etc.

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

`chopt $(shuf -n 100 /usr/share/dict/words)`

`chopt options{1..100}`
