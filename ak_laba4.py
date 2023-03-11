def del3(x):
    a=str("деление выполняется")
    b=str("деление не выполняется")
    return a if int(x) % 3 == 0 else b
print (del3(9))

def del100(x):
    try:
        x=int(input("Введите число"))
        res=100/x
    except ZeroDivisionError:
        res="деление на ноль"
    except ValueError:
        res="это не число"
    return res
print(del100(0))

def magic_number(x):
    x=input("Введите дату")
    day=x[0:2]
    month=x[3:5]
    year=x[-2:]
    return True if int(day) * int(month)==int(year) else False
print (magic_number(0))

def lucky_ticket(x):
    x=input("Введите номер билета")
    if len(x) % 2 !=0 :
        print("Нечетное количесвто цифр")
    else:
        h=len(x)/2
        half1=x[0:int(h)]
        half2=x[int(h):]
        s1=0
        s2=0
        for i in half1:
            s1 +=int(i)
        for i in half2:
            s2 += int(i)
        if s1==s2:
            res="Счастливый"
        else:
            res="Несчастливый"
        return res
print(lucky_ticket(0))
