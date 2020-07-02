def jumble():
    new_str = ''
    letters = 'abcdefghijklmnopqrstuvwxyz'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    x = input()
    a = []
    for j in range(len(x)):
        a.append(x[j])
    for i in range(len(a)):
        if a[i] in 'aeiou':
            new_str += a[i]
        elif a[i] == 'z':
            new_str += 'zuz'
        else:
            index = consonants.find(a[i])
            third = consonants[index + 1]
            first = a[i]
            if a[i] in 'bc':
                second = 'a'
            elif a[i] in 'dfg':
                second = 'e'
            elif a[i] in 'hjkl':
                second = 'i'
            elif a[i] in 'mnpqr':
                second = 'o'
            else:
                second = 'u'
            new_str = new_str + first + second + third

    return new_str


f = jumble()
print(f)

