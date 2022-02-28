a = True 
while a: 
    ps = input("Напиши пароль") 
    if len(ps) < 8: 
        print("Короткий") 
    elif ps in "123": 
        print("Простой") 
    else: 
        print("OK") 
        a = False 
    print("Пароль отличный") 