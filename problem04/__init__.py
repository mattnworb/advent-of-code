from typing import List, Dict
import re

# The automatic passport scanners are slow because they're having trouble
# detecting which passports have all required fields. The expected fields are as
# follows:
#
# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
#
# Passport data is validated in batch files (your puzzle input). Each passport
# is represented as a sequence of `key:value` pairs separated by spaces or
# newlines. Passports are separated by blank lines.


def parse_passports(text: str) -> List[Dict[str, str]]:
    passports = []

    for passport in text.split("\n\n"):
        if not passport:
            continue

        fields = {}
        for pair in passport.split():
            k, v = pair.split(":")
            fields[k] = v
        passports.append(fields)

    return passports


def is_valid(passport: Dict[str, str], check_fields_valid=False) -> bool:
    # "cid" is not reqiured in part 1
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    if not required_fields.issubset(passport.keys()):
        return False

    if not check_fields_valid:
        # stop
        return True

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.

    checks = {
        "byr": lambda text: is_int(text) and 1920 <= int(text) <= 2002,
        "iyr": lambda text: is_int(text) and 2010 <= int(text) <= 2020,
        "eyr": lambda text: is_int(text) and 2020 <= int(text) <= 2030,
        "hgt": _check_hgt,
        "hcl": lambda text: re.fullmatch(r"#[0-9a-f]{6}", text) is not None,
        "ecl": lambda text: text in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"},
        "pid": lambda text: is_int(text) and len(text) == 9,
    }

    return all(func(passport[field]) for field, func in checks.items())


def is_int(text: str) -> bool:
    return text.isdigit()


def _check_hgt(text: str):
    m = re.fullmatch(r"(\d+)(cm|in)", text)
    if m:
        num = int(m.group(1))
        if m.group(2) == "cm":
            return 150 <= num <= 193
        if m.group(2) == "in":
            return 59 <= num <= 76

    return False
