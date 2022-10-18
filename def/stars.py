def stars(rows:int):
    for i in range(rows):
        print((((rows-i-1)*'  ')+(2*i+1)*'* ')[:-1])

stars(int(input('Number of rows: ')))