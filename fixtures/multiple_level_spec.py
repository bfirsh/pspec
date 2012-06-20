from pspec import describe
import random

with describe('random'):
    with describe('choice'):
        def it_chooses():
            seq = range(10)
            assert random.choice(seq) in seq
