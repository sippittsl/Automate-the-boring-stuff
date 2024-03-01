#! python3

def capital_indexes(string):
    return [i for i, char in enumerate(string) if char.isupper()]

print(capital_indexes("HeLlO World - MY name is LEE and I WANT to Say HeLlO"))