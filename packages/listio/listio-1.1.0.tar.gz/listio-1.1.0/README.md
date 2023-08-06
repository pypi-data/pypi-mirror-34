# ListIO

Read/write lists and maps (two dimensional lists) from/to files.

- Lists are stored as plain text files with one list item per line.
- Maps (two dimensional lists) are stored as CSV.

When reading a list or map, lines starting with a hash sign (`#`) are considered
to be comments and therefore ignored.

## Installation

Install ListIO using pip:

```
pip install listio
```

## Usage

### Lists

#### Writing

```python
import listio

listio.write_list(
    'mylist.txt',
    ['foo', 'bar', 'baz']
)
```

mylist.txt now contains:

```
foo
bar
baz
```

#### Reading

mylist.txt:

```
First item
second item
foo
# this is a comment
bar
```

Read `mylist.txt` as an iterator:

```python
>>> import listio
>>> mylist = listio.read_list('mylist.txt')
>>> list(mylist)
['First item', 'second item', 'foo', 'bar']
```

### Maps

#### Writing

```python
import listio

listio.write_map(
    'mymap.csv,
    [['foo bar', 'baz', 'x'], [1, 2, 3]]
)
```

mymap.csv now contains:

```
foo bar;baz;x
1;2;3
```

The default CSV delimiter is `;` and lineterminator `\n`. You can change this:

``` python
listio.write_map(
    'mymap.csv,
    [['foo bar', 'baz', 'x'], [1, 2, 3]],
    delimiter=',',
    lineterminator='\r\n'
)
```

### Reading

mymap.csv:

```csv
First column;"second column";3
# this is a comment
"next;item,";foo;bar
```

Read `mymap.csv` as an iterator:

```python
>>> import listio
>>> mymap = listio.read_map('mymap.csv')
>>> list(mymap)
[['First column', 'second column', '3'], ['next;item,', 'foo', 'bar']]
```

The default CSV delimiter is `;` and lineterminator `\n`. You can change this:

``` python
>>> listio.read_map('mymap.csv', delimiter=',', lineterminator='\r\n')
```

## Examples

See [tests/test_listio.py](tests/test_listio.py) for more usage examples.

## Contributing

See [NOTICE](./NOTICE) and [LICENSE](./LICENSE) for license information.
