def a():
    from random import randint
    a=int(randint(0,9))
    b=int(randint(0,9))
    c=int(randint(0,9))
    d=int(randint(0,9))
    e=int(randint(0,9))
    spisok=[a,b,c,d,e]
    num=int(input("Введите число"))
    if num in spisok:
        print("Поздравляю, Вы угадали число","ваше число:", num, "список:", spisok )
    else:
        print("Нет такого числа!", "ваше число:", num, "список:", spisok)

def b():
    spisok=[1,2,3,4,3,5,3]
    cnt=0
    for i in range(len(spisok)-1):
        for j in range(i+1,len(spisok)):
            if spisok[i]==spisok[j]:
                cnt+=1
                print(spisok[i], cnt)
def c():
    week=("Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье")
    v=int((input("Количесвто выходных дней:")))
    for i in week:
        print("Рабочие дни:", *week[:-v], "Выходные дни:", *week[-v:])
        break

def d():
    import random
    from random import sample
    cnt=0
    sp1=["Вдовичева", "Денисов", "Азарян","Банбасов", "Афанасьев","Логинов","Старостина","Трушкова","Закиров","Власов"]
    sp2=["Иванов","Петров","Смирнов","Пушкин","Лермонтов","Толстой","Достоевский","Чехов","Бунин","Булгаков"]
    sport = tuple(sample(sp1, 10)[:5] + sample(sp2, 10)[:5])
    print("1 список:", sp1)
    print("2 список:", sp2)
    print("команда:", sport)
    print(len(sport))
    print(sorted(sport))
    f=str(input("Фамилия:"))
    for i in sport:
        if f.title() in sport:
            print ("присутсвует")
            cnt+=1
            print("Количество совпадений:", cnt)
            break
        else:
            print("нет в команде")
            break
a()
b()
c()
d()




