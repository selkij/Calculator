def calcul(operation):
    op = operation.replace(' ', '')
    if "*" in operation:
        return Multiply(op.split('*'))
    if "+" in operation:
        return Add(op.split('+'))
    if "-" in operation:
        return Substract(op.split('-'))
    if "/" in operation:
        return Divide(op.split('/'))


def Multiply(inputs):
    r = int(inputs[0])

    del input[0]
    
    #for each numbers in 'inputs', r * 'nbr'
    for nbr in inputs:
        r *= int(nbr)

    return r


def Add(inputs):
    r = int(inputs[0])

    del input[0]
    
    #for each numbers in 'inputs', r * 'nbr'
    for nbr in inputs:
        r += int(nbr)

    return r


def Divide(inputs):
    if "0" in inputs:
        print("0")
        return 0

    r = int(inputs[0])
    del input[0]
    
    #for each numbers in 'inputs', r * 'nbr'
    for nbr in inputs:
        r /= int(nbr)

    return r


def Substract(inputs):
    r = int(inputs[0])
    del input[0]
    
    #for each numbers in 'inputs', r * 'nbr'
    for nbr in inputs:
        r -= int(nbr)

    return r

print("Calculatrice:")
while True:
    calcul(input())
