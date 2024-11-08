somma = 0
b = 1
while b > 0:
    x = int(input("Inserire un numero: "))
    if x != 0 :
        somma += x
    else:
        b = b - 1
        print("La somma dei numeri inseriti è: ", somma)

