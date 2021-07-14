def findAge(currentYear, birthYear):
    Age = currentYear - birthYear
    return Age

def inputCurrentandBirthYear ():
    currentYear = int(input("Enter the current year: "))
    birthYear = int(input("Enter year of birth: "))
    return findAge(currentYear, birthYear)

print(inputCurrentandBirthYear ())


