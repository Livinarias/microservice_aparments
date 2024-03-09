from functools import reduce

t = [1,3,2,0,7,8,1,3,0,0,6,7,1]

def reorganize(acc, item):
    def update_acc(value):
        if acc[-1] == 'X':
            acc[-1] = value
        else:
            acc[-1] = ''.join(sorted(acc[-1] + value))

    if item == 0:
        acc.append('')
        if acc[-1] == '':
            acc[-1] = 'X'
    else:
        update_acc(str(item))
    return acc

result = reduce(reorganize, t, [''])
print("entra aca",' '.join(result))


