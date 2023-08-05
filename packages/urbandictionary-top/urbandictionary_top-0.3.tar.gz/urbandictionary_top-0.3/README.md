# urbandictionary_top-python
A dead-simple module that fetches the top definition of a term from urbandictionary.


## Installation

### Using pip

```bash
$ pip install urbandictionary_top
```


### Manual

- Clone this repository or download urbandictionary_top.py
- Put urbandictionary_top.py somewhere you'd like to use it


## Usage

```bash
$ python
```

```python
>>> from urbandictionary_top import udtop
>>> term = udtop('term')
>>> print(term)
```
```text
Term is a word. A term is a term. The term term is a word that describes a body or building of letters formed into a descriptive compilation that stands for something, giving it substance.
Terms include: Every word o this website, save symbols and numerics:§ ‹>*#%@ and 129385, respectively.

Example: The term term is a term
```
```python
>>> term.definition
'Term is a word. A term is a term. The term term is a word that describes a body or building of letters formed into a descriptive compilation that stands for something, giving it substance.\nTerms include: Every word o this website, save symbols and numerics:§ ‹>*#%@ and 129385, respectively.'
>>> term.example
'The term term is a term'
```
