def power_set(string, i=0, current=''):
    if i == len(string):
        print(current, end=' ')
        return
    power_set(string, i+1, current+string[i])
    power_set(string, i+1, current)


if __name__ == '__main__':
    power_set('abc')
    print()
    power_set('xyz')
