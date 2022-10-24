def chain(index:int,word:str):
    if index >= len(word):
        return print('not in chain')
    else:
        return print(word[index])

chain(int(input('Index: ')),str(input('Chain: ')))