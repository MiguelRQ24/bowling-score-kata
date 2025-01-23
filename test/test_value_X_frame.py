import pytest
from src.bowling_card import BowlingCard

def test_symbols_to_numbers():
    assert BowlingCard._BowlingCard__symbols_to_numbers(['X']) == [10]
    assert BowlingCard._BowlingCard__symbols_to_numbers(['6', '/']) == [6, 4]
    assert BowlingCard._BowlingCard__symbols_to_numbers(['-', '/']) == [0, 10]
    assert BowlingCard._BowlingCard__symbols_to_numbers(['6', '3']) == [6, 3]
