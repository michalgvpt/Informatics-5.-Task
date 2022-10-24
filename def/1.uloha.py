def rectangle(width,symbol):
    print(symbol*width)
    print(symbol+' '*(width-2)+symbol)
    print(symbol*width)

rectangle(int(input('Give number: ')),input('Give symbol: '))