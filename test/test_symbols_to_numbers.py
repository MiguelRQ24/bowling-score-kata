import pytest
from src.bowling_card import BowlingCard

def test_symbols_to_numbers():
    assert BowlingCard._BowlingCard__value_X_frame([[1, 2], [3, 4], [5, 1], [10], [4, 5], [1, 2], [3, 4], [5, 1], [2, 3], [4, 5]], 3) == 19
    assert BowlingCard._BowlingCard__value_X_frame([[1, 2], [3, 4], [5, 1], [10], [10], [6, 2], [3, 4], [5, 1], [2, 3], [4, 5]], 3) == 26
    