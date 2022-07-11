def letter_combination(digits):
    tab = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqr', 8: 'tuv', 9: 'wxyz'}
    res = []

    combinations = 1
    for digit in digits:
        combinations *= len(tab[int(digit)])

    column = 0
    while combinations > 1:
        if column == 0:
            for s in tab[int(digits[column])]:
                for i in range(combinations // len(tab[int(digits[column])])):
                    res.append(s)
        else:
            index = 0
            while index < len(res):        # the while loop renew the letters to be placed.
                for s in tab[int(digits[column])]:
                    for i in range(combinations // len(tab[int(digits[column])])):
                        res[index] += s
                        index += 1

        combinations //= len(tab[int(digits[column])])
        column += 1

    return res


print(letter_combination("23"))
print(letter_combination("2"))
