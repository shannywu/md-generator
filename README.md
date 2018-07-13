# Markdown Generator

A Python package for generating markdown.

## Prerequisite
- Python 3.6

## Usage

- Start with
```python
import mdgenerator as mg
```

- Add text
```python
text = mg.Text()
print(text.add_heading('test', 5))
print(text.add_italics('test'))
print(text.add_bold('test'))
print(text.add_emphasis('test'))
print(text.add_blockquotes('test'))
```
Result:
```
##### test
*test*
**test**
**_test_**
> test
```

- Add List
```python
_list = mg.List()
print(_list.add_list(['a', 'b', 'c'], ordered=False))
```
Result:
```
- a
- b
- c
```

- Add Table
```python
table = mg.Table()
print('\n')
print(table.add_row(['English', 'Chinese']))
print(table.add_sep_row(cols=2))
print(table.add_row(['Apple', '蘋果']))
print(table.add_row(['Banana', '香蕉']))
print(table.add_row(['Cherry', '櫻桃']))
```
Result:
```
|English|Chinese|
|----|----|
|Apple|蘋果|
|Banana|香蕉|
|Cherry|櫻桃|
```
