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

    with describe('sample'):
        def it_raises_an_exception_for_a_sample_size_larger_than_the_sequence():
            with assert_raises(ValueError):
                random.sample(range(10), 20)

        def it_chooses_elements_that_are_in_the_sequence():
            seq = range(10)
            for element in random.sample(seq, 5):
                assert element in seq


