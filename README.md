# bonk

A bongo.cat wrapper made in Python 3.

## Requirements

See [requirements.txt](requirements.txt)

You also need [geckodriver](https://github.com/mozilla/geckodriver) on your system path.

## Example

First, `git clone https://github.com/creepinson/bonk`.
Next, `cd bonk`.

Now you can run the example file:

```python
python3 -m bongo.example
```

This example opens a firefox browser instance, then plays the C note on the keyboard 10 times with a 0.25 second delay in between.

## API Usage

```python
from .bongo import Bongo, Notes

bongo = Bongo()
bongo.note(Notes.C).play(0.25, 10)

```
