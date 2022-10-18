def line(n, text=''):
    if text != '':
        text = ' ' + text + ' '
    half1 = (n - len(text)) // 2
    half2 = n - len(text) - half1
    print('*' * half1 + text + '*' * half2)

width=40
line(width)
line(width, 'Ján Botto')
line(width, 'Žltá ľalija')
line(width, '-')
line(width, 'Stojí stojí mohyla')
line(width, 'Na mohyle zlá chvíľa')
line(width, 'na mohyle tŕnie chrastie')
line(width, 'a v tom tŕní chrastí rastie')
line(width)