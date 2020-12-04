from typing import List, Dict

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


def is_valid(passport: Dict[str, str]) -> bool:
    # "cid" is not reqiured in part 1
    required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
    return required_fields.issubset(passport.keys())
