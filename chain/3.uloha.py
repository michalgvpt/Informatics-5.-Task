def vowels(chain):
    vow = 'aeiou'
    a = True
    for i in chain:
        if i in vow:
            a = True
        else:
            a = False
        break
    return print(a)

vowels(str(input('Chain: ')))