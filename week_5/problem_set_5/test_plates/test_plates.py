from plates import is_valid


def test_valid_min_length():
    # Minimum length is 2 chars
    assert is_valid("AB")
    assert is_valid("XY")


def test_valid_max_length():
    # Maximum length is 6 chars
    assert is_valid("ABC123")
    assert is_valid("XYZQ12")
    assert is_valid("ABCDEF")


def test_valid_characters():
    # Only alphanumeric allowed; no special chars
    assert is_valid("ABCDEF")
    assert is_valid("AB1234")
    assert is_valid("WXYZ23")


def test_invalid_min_max_length():
    # Less than 2 or more than 6 chars is invalid
    assert not is_valid("A")
    assert not is_valid("AABBCCD")


def test_invalid_non_alphanumeric_chars():
    # Special characters not allowed (spaces, periods, punctuation)
    assert not is_valid("A.B C!")
    assert not is_valid("AB C")
    assert not is_valid("!ABC")
    assert not is_valid("A.BC")
    assert not is_valid("ABC*")


def test_invalid_numbers_placement():
    # Numbers cannot be in the middle, and first digit cannot be zero
    assert not is_valid("AB12CD")   # digits in the middle
    assert not is_valid("XY09AB")   # digit zero as first digit
    assert not is_valid("AB012")    # first digit zero
    assert not is_valid("XY0")      # first digit zero with short plate
    assert not is_valid("AB0")      # first digit zero


def test_invalid_start_letters():
    # Plate must start with two letters
    assert not is_valid("1ABC")
    assert not is_valid("1A")
    assert not is_valid("123")   # all digits, obviously invalid
    assert not is_valid("A1BC")  # Second char not a letter (first char is letter)
    assert not is_valid("12ABC") # First two chars not letters
    assert not is_valid("1!")    # special char as second char
    assert not is_valid("!@#")   # special chars only
    assert not is_valid("A")       # only one char
    assert not is_valid("1")       # single non-letter char
    assert not is_valid("")


def test_empty_plate():
    # Empty plate is invalid
    assert not is_valid("")
