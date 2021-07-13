### examples of autolinks that don't work on GH Pages.
[--skip](#--skip) |
[-s short form of --skip](#-s-short-form-of---skip) |
[--fail-nocode](#--fail-nocode)


## --skip

This command
<!--phmdoctest-label skip-command-->

## -s short form of --skip

This is the same command as above using the short `-s` form of the --skip option
in two places.

## --fail-nocode

This option produces a pytest file that will always
fail when no Python code or session blocks are found.

### examples of autolinks that might work.  Just use on "-".
[-skip2](#-skip2) |
[-s short form of -skip2](#-s-short-form-of--skip2) |
[-fail-nocode2](#-fail-nocode2) |
[arg--skip3](#arg--skip3)

## -skip2

This command
<!--phmdoctest-label skip-command-->

## -s short form of -skip2

This is the same command as above using the short `-s` form of the --skip option
in two places.

## -fail-nocode2

This option produces a pytest file that will always
fail when no Python code or session blocks are found.

## arg--skip3

This command
<!--phmdoctest-label skip-command-->





### Examples of code and session blocks

This file (project.md) has some example code and session blocks
including a doctest directive example.

It is placed at the project root level for use
by the .travis.yml example in README.md.


#### An example with a blank line in the output

No <BLANKLINE> directive is needed in the output block of a Python
code block output block pair.
 
```python
def greeting(name: str) -> str:
    return 'Hello' + '\n\n' + name
print(greeting('World!'))
```

Here is the output it produces.
```
Hello

World!
```

The fenced block below has `python3` as the info string.
 
```python3
def greeting(name: str) -> str:
    return 'Hello' + '\n\n' + name
print(greeting('World!'))
```

Here is the output it produces.
```
Hello

World!
```


#### Interactive Python session requires `<BLANKINE>` in the expected output 

Blank lines in the expected output must be replaced with `<BLANKLINE>`.
To see the `<BLANKLINE>` navigate to [project.md unrendered][1]. 

The fenced block below has `pycon` as the info string.

```pycon
>>> print('Hello\n\nWorld!')
Hello
<BLANKLINE>
World!
```

Here is the same block with `py` as the info string.

```py
>>> print('Hello\n\nWorld!')
Hello
<BLANKLINE>
World!
```

Here is the same block with `python` as the info string.

```python
>>> print('Hello\n\nWorld!')
Hello
<BLANKLINE>
World!
```

Here is the same block with no info string.

```
>>> print('Hello\n\nWorld!')
Hello
<BLANKLINE>
World!
```


#### Interactive Python session with doctest directive 

Here is an interactive Python session showing an
expected exception and use of the doctest directive
`IGNORE_EXCEPTION_DETAIL`.


```pycon
>>> int('def')    #doctest:+IGNORE_EXCEPTION_DETAIL   
Traceback (most recent call last):
    ...
ValueError:
```

#### Session with `py` as the fenced code block info_string

```py
>>> coffee = 5
>>> coding = 5
>>> enjoyment = 10
>>> print(coffee + coding)
10
>>> coffee + coding == enjoyment
True
```
