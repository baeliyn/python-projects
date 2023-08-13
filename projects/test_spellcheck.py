import pytest
import spellcheck

alpha = "Checking the length & structure of the sentence."

@pytest.fixture
def input_value():
    input = alpha
    return input

def test_length(input_value):

    assert spellcheck.word_count(input_value) < 10
    assert spellcheck.char_count(input_value) < 50

def test_struc(input_value):

    assert spellcheck.first_char(input_value).isupper()
    assert spellcheck.last_char(input_value) == "."
