import pytest
import re

dataFile = open('../Data/Day4.txt')
dataLines = [str(i) for i in dataFile.read().splitlines()]

def SolvePart1(dataLines: str) -> int:
    return len(GetValidPasswords(dataLines))

def SolvePart2(dataLines: str) -> int:
    passwords = GetValidPasswords(dataLines)

    passportList = []
    passport = ""
    dataLines.append("") # additional empty line eof
    for line in dataLines:
        if line == "":
            passportList.append(passport)
            passport = ""
        else:
            passport = passport + " " + line

    validationTable =  [[r'(byr:)(19[2-9][0-9]|200[0-2])', 2], \
                        [r'(iyr:)(201[0-9]|2020)', 2], \
                        [r'(eyr:)(202[0-9]|2030)', 2], \
                        [r'(hgt:)(1[5-8][0-9]cm|19[0-3]cm|59in|6[0-9]in|7[0-6]in)', 2], \
                        [r'(hcl:)(#[a-f0-9]{6})', 2], \
                        [r'(ecl:)(amb|blu|brn|gry|grn|hzl|oth)', 2], \
                        [r'(pid:)([0-9]{9}) ', 2]]
    validPasswords = 0
    for password in passportList:
        validations = 0
        for validation in validationTable:
            matches = re.search(validation[0], password)
            if matches:
                if len(matches.groups()) == validation[1]:
                    validations = validations + 1
        if validations == 7:
            validPasswords = validPasswords + 1
    return validPasswords

def GetValidPasswords(dataLines: str) -> []:
    passportList = []
    passport = ""
    dataLines.append("") # additional empty line eof
    for line in dataLines:
        if line == "":
            passportList.append(passport)
            passport = ""
        else:
            passport = passport + " " + line
    validPassportList = []
    for passport in passportList:
        if IsPasswordValid(passport):
            validPassportList.append(passport)
    return validPassportList


#(\w+):(\d{4})


def IsPasswordValid(password: str) -> bool:
    matches = re.findall(r'(\w+):(#|\w+)', password)
    if len(matches) == 8:
        return True
    match = re.search(r'(cid):', password)
    if len(matches) == 7 and not match:
        return True
    return False

print (SolvePart2(dataLines))
##print (SolvePart2(data_lines))
