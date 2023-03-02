a = input()
b = input()
if a == b:
    print("password is correct")
else:
    print("password is not correct")


n = int(input())
if 36 < n <= 54:
       if n % 2:
           print("боковое нижнее")
       else:
           print("боковое верхнее")
elif n % 2:
    print("купе нижнее")
else:
    print("купе верхнее")



 year = int(input())
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        print("високосный")
 else:
        print("не високосный")



a=input("1 цвет")
b=input("2 цвет")
if a=="красный" and  b=="желтый" or a=="желтый" and b=="красный":
    print("оранжевый")
elif a=="красный" and  b=="синий" or a=="синий" and b=="красный":
    print("фиолетовый")
elif a=="желтый" and  b=="синий" or a=="синий" and b=="желтый":
    print("зеленый")
else:
    print("error")



a = int(input())
n= ''
for x in range(a):
    n += input()
    n +=" "
    # или n=str(n)+ str(" ") +str(input())
print (n)
