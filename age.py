def discover_age(birthyear, year):
    return year - birthyear


assert discover_age(1991, 2050) == 59

print(discover_age(1996, 2060))