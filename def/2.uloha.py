def line(n, text=''):
    if text != '':
        text = ' ' + text + ' '
    half1 = (n - len(text)) // 2
    half2 = n - len(text) - half1
    print('*' * half1 + text + '*' * half2)

line(int(input("Give width: ")),input("Insert text: "))