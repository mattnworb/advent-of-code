from problem04 import *

example = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""


def test_parse_passports():
    passports = parse_passports(example)
    expected = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    assert passports[0] == expected
    # assert [is_valid(p) for p in passports] == [True, False, True, False]


def test_is_valid():
    p1 = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    assert is_valid(p1) == True

    p2 = {
        "iyr": "2013",
        "ecl": "amb",
        "cid": "350",
        "eyr": "2023",
        "pid": "028048884",
        "hcl": "#cfa07d",
        "byr": "1929",
    }
    assert is_valid(p2) == False


def test_example1():
    passports = parse_passports(example)
    assert [is_valid(p) for p in passports] == [True, False, True, False]
