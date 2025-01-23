import pytest
from src.bowling_card import BowlingCard

def test_score_card():
    
    assert BowlingCard("12345123451234512345")
    assert BowlingCard("12345123451234512345").get_rolls() == "12345123451234512345"
    assert BowlingCard("12345123451234512345").get_frames() == [[1, 2], [3, 4], [5, 1], [2, 3], [4, 5], [1, 2], [3, 4], [5, 1], [2, 3], [4, 5]]

def test_hitting_pins_regular():

    pins = "12345123451234512345"
    total = 60

    assert BowlingCard(pins).get_total_score() == total

def test_symbol_zero():

    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90

    assert BowlingCard(pins).get_total_score() == total

    pins = "9-3561368153258-7181"
    total = 82
   
    assert BowlingCard(pins).get_total_score() == total

def test_spare_not_extra():

    pins = "9-3/613/815/-/8-7/8-"
    total = 121

    assert BowlingCard(pins).get_total_score() == total

def test_strike():

    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100

    assert BowlingCard(pins).get_total_score() == total

    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110

    assert BowlingCard(pins).get_total_score() == total

def test_two_strikes(): 
    
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120

    assert BowlingCard(pins).get_total_score() == total

def test_three_strikes():
    
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141

    assert BowlingCard(pins).get_total_score() == total

def test_one_pin_in_extra_roll():

    pins = "9-3/613/815/-/8-7/8/8"
    total = 131

    assert BowlingCard(pins).get_total_score() == total

    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150

    assert BowlingCard(pins).get_total_score() == total

def test_two_strikes_in_extra_rolls():

    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111

    assert BowlingCard(pins).get_total_score() == total

    pins = "XXXXXXXXXXXX"
    total = 300

    assert BowlingCard(pins).get_total_score() == total

def test_one_strike_in_extra_roll():

    pins = "8/549-XX5/53639/9/X"
    total = 149

    assert BowlingCard(pins).get_total_score() == total

def test_spare_in_extra_roll():

    pins = "X5/X5/XX5/--5/X5/"
    total = 175

    assert BowlingCard(pins).get_total_score() == total

def test_spare_in_extra_roll():

    pins = "X5/X5/XX5/--5/X5/"
    total = 175

    assert BowlingCard(pins).get_total_score() == total

def test_triple_strike_before_extra_rolls():

    pins = "XXXXXXXXXXXX"
    total = 300

    assert BowlingCard(pins).get_total_score() == total
