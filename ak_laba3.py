def a():
    y=int(input())
    n=""
    for x in range(y):
        n=str(n) + str(" ") +str(input())
    print(n)
a()

def b():
    a=str(input())
    n=""
    while a!= "stop":
        n= str(n) + a + (" ")
        a=str(input())
    print(n)
b()

def c():
    slovo=input()
    for i in slovo:
        if "ф" in slovo:
            print("Ого!Это редкое слово!")
            break
        elif "Ф" in slovo:
            print("Ого!Это редкое слово!")
            break
        else:
            print("Эх, это не очень редкое слово...")
            break
c()

def d():
    from random import randint
    n=0
    while n<3:
        a=int(randint(0,10))
        b=int(randint(0,10))
        print(a , "+",  b , "=")
        c=int(input("Запишите ответ"))
        if a+b!=c:
            n=n+1
    if n==3:
        print("Конец игры")
d()
