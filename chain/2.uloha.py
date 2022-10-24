def number(sentence):
    a = '0123456789'
    empty = ''
    for i in sentence:
        if i in a:
            empty += i
    return print(len(empty))

number(str(input('Sentence: ')))