pspec
=====

[![Build Status](https://travis-ci.org/bfirsh/pspec.png?branch=master)](https://travis-ci.org/bfirsh/pspec)

Python testing for humans, built with [Attest](http://packages.python.org/Attest/).

Tests shouldn't just be for computers to check your code runs correctly. They can also be used by humans to understand what your code does.

pspec tests are designed to be parsed by humans. They look a bit like this:

```python
from pspec import describe, assert_raises
import random

with describe('random'):
    with describe('shuffle'):
        def it_does_not_lose_any_elements():
            seq = range(10)
            random.shuffle(seq)
            seq.sort()
            assert seq == range(10)

        def it_raises_an_exception_for_an_immutable_sequence():
            with assert_raises(TypeError):
                random.shuffle((1, 2, 3))

    with describe('choice'):
        def it_picks_an_element_that_is_in_the_sequence():
            seq = range(10)
            assert random.choice(seq) in seq
```

(Compare with a [similar example for the built-in unittest module](http://docs.python.org/library/unittest.html#basic-example).)

They are run with the `pspec` command:

    $ pspec random_spec



Development install
-------------------

    $ pip install -r requirements.txt
    $ python setup.py develop

Test suite
----------

    $ pspec spec

Goals
-----

**Note:** pspec is still in its infancy. Don't expect it to be useful yet. 

Here's some stuff I want it to do:

 - Beautiful test reports with coloured string diffs. (Similar to [Mocha's](http://visionmedia.github.com/mocha/#string diffs))
 - Contexts, before/after hooks, etc.

It's going to be simple, Pythonic and use minimal magic.


