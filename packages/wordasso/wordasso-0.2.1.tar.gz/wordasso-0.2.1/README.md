# wordasso
small python package, several word association function based on datamuse API

## Installation

```
pip install wordasso
```

if it can not install spacy and the model needed automatically, you could fix this by installing it manually

```
pip install spacy
python -m spacy download en_core_web_sm
```
and then

```
pip install wordasso
```

## Usage
these functions are based on datamuse means like API which could be used to query 100 related words of a given word

### syn_words
return related words which has 'synonym' in tags list

```
>>> from wordasso.wordasso import syn_words
>>> print(syn_words("author"))

# output
['writer', 'source', 'generator']
```

### pho_words
return related words which sound like the key word most, default list size is 10.

```
>>> from wordasso.wordasso import pho_words
>>> print(pho_words("author"))

# output
['writer', 'actor', 'authorship', 'writers', 'drafter', 'reporter', 'owner', 'songwriter', 'signer', 'source']

>>> print(pho_words("author", L=5)

# output
['writer', 'actor', 'authorship', 'writers', 'drafter']
```

### ent_words
return Named Entities associated to the related words of the given word.

```
>>> from wordasso.wordasso import ent_words
>>> print(ent_words("author"))

# output
{French, Judeo, Christian, Islam, trustee, Medina, trustee, Judeo, Mecca, Muhammad}
```


