def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False

def test_leap_year():
    assert is_leap_year(2000) == True
    assert is_leap_year(2004) == True
    assert is_leap_year(2400) == True
    assert is_leap_year(1600) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False
    assert is_leap_year(2500) == False
    assert is_leap_year(1700) == False

if __name__ == "__main__":
    test_leap_year()
    print("All tests passed!")

