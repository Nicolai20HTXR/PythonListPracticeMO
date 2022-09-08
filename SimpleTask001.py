import random

arrA = []
arrB = []

for i in range(1000):
    arrA.append(random.randrange(0,100))

print("1000 Tilfældig tal mellem 0 og 100: \n")
print(arrA)

for i in range(10):
    arrA.append(int(input(str(i+1)+": Tilføj tal:\n")))

for i in arrA:
    if i <=60 and i >= 50:
        arrB.append(i)
print("\n\n\n Liste over talene fra list A mellem 50 og 60: \n")
print(arrB)

for i in arrB:
    arrA.remove(i)
print("\n\n\n Liste A med talene mellem 50 og 60 fjernet: \n")
print(arrA)



sorting = True
while sorting:
    prevCounter = 0
    for i in range(len(arrA)):
        if i < len(arrA)-1:
            if arrA[i]>arrA[i+1]:
                temp = arrA[i]
                arrA[i] = arrA[i+1]
                arrA[i+1] = temp
                prevCounter+=1
    if(prevCounter==0):
        sorting = False
    
print("\n\n\n Sorteret list A: \n")
print(arrA)
