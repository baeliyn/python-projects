import spellcheck

alpha = "Checking the length & structure of the sentence."

def test_length(input_value):

    assert spellcheck.word_count(alpha) < 10
    assert spellcheck.char_count(alpha) < 50

def test_struc(input_value):

    assert spellcheck.first_char(alpha).isupper()
    assert spellcheck.last_char(alpha) == "."
