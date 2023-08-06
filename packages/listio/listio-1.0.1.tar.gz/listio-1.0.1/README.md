# ListIO

Read/write lists and maps (two dimensional lists) from/to files.

Lists are stored as plain text -- one value per line.

Maps (two dimensional lists) are stored as CSV.

When reading a list or map from a file, lines starting with a hash sign (`#`) are considered to be comments and ignored.

## Installation

Install using setuptools:

```
python setup.py install
```

## Usage

See [tests/test_listio.py](tests/test_listio.py) for a working example.

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

```python
import listio

mylist = listio.read_list('mylist.txt')
```

Variable `mylist` now contains an iterator. If we print it:

```python
print(list(mylist))
```

the result is:

```python
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

### Reading

mymap.csv:

```csv
First column;"second column";3
# this is a comment
"next;item,";foo;bar
```

```python
import listio

mymap = listio.read_map('mymap.csv')
```

Variable `mymap` now contains an iterator. If we print it:

```python
print(list(mymap))
```

the result is:

```python
[['First column', 'second column', '3'], ['next;item,', 'foo', 'bar']]
```

## Contributing

See [NOTICE](./NOTICE) and [LICENSE](./LICENSE) for license information.
