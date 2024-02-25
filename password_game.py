import time; from string import punctuation; import pyperclip
print("Original game: neal.fun/password-game")
a="0";languages=[["english","eng"],["russian","ru"]];game = True
days=["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
lang=(input("Select language(Russian/English): ")).lower()
if lang!='quit':
    while (not lang in languages[0]) and (not lang in languages[1]):
        print("Invalid: You are Invalid")
        lang=(input("Select language(Russian/English): ")).lower()
else:
    print('Good bye!')
    quit()
if lang in languages[0]:
    length="Length";ent_password="Enter your password: ";ent_name="Enter your name: "
    signup="Sign up";login="Log in";lose="Your password is wrong.";gameover="Game over.";print(signup)
    name = input(ent_name);win=f"Successful! Welcome, {name}.\nYou won!"
    rule1="Your password must be at least 8 characters"
    rule2="Your password must include a number"
    rule3="Your password must include an uppercase letter"
    rule4="Your password must include a special character"
    rule5="The digits in your password must add up to 40" 
    rule6="Your password must include a day of the week"
    rule7="Your password must include current year"
    rule8="Your password must include the length of your password"
    rule9="Your password must include the key🔑 emoji"
    rule10="Your password must include your name"
    rule11="The length of your password must be even number"
    rule12="Your password must include the current time backwards (Example: 01:02 -> 20:10)"
    confirm="Do you confirm that this is your password?(Yes or Yes) "
elif lang in languages[1]:
    length="Длина";ent_password="Введите пароль: ";ent_name="Введите ваше имя: "
    signup="Регистрация";login="Вход";lose="Неверный пароль.";gameover="Игра окончена.";print(signup)
    name = input(ent_name);win=f"Успешно! Добро пожаловать, {name}.\nВы победили!"
    rule1="Ваш пароль должен быть не менее 8 символов в длину"
    rule2="Ваш пароль должен содержать хоть одну цифру"
    rule3="Ваш пароль должен содержать заглавную букву"
    rule4="Ваш пароль должен содержать любой знак пунктуации"
    rule5="Сумма цифр в вашем пароле должна быть 40"
    rule6="Ваш пароль должен содержать день недели"
    rule7="Ваш пароль должен содержать текущий год"
    rule8="Ваш пароль должен содержать длину вашего пароля"
    rule9="Ваш пароль должен содержать эмодзи ключа🔑"
    rule10="Ваш пароль должен содержать ваше имя"
    rule11="Длина вашего пароля должна быть чётным числом"
    rule12="Ваш пароль должен содержать текущее время наоборот (Пример: 01:02 -> 20:10)"
    confirm="Вы подтверждаете что это ваш пароль?(Да или Да) "
a = input(ent_password)
if "functions":
    def contain_digit(x):
        for char in x:
            if char.isdigit():
                return "True"
                break
    def contain_upper(x):
        for char in x:
            if char.isupper():
                return "True"
                break
    def contain_punctuation(x):
        for char in x:    
            if char in punctuation:
                return "True"
                break
    def digits_summ(x):
        total = 0
        for char in x:
            if char.isdigit():
                total += int(char)
        return total
    def contain_day(x):
        for i in days:
            if i in x.lower():
                return "True"; break
        y="";z=""
        if y in x or z in x:
            return "False"
    def contain_year(x):
        s=int(time.time())
        res = time.localtime(s)
        year = str(res.tm_year)
        if year in x:
            return "True"
    def contain_time(x):
        import time
        s=int(time.time())
        res = time.localtime(s)
        hour = (res.tm_hour)
        min = (res.tm_min)
        if min<10:
            min = "0"+str(min)
        if hour<10:
            hour = "0"+str(hour)
        min=str(min);hour=str(hour)
        time=f"{min[::-1]}:{hour[::-1]}"
        if time in x:
            return "True"
    def even_length(x):
        lx=len(x)
        if (lx%2)==0:
            return "True"
    def cl():
        for i in range(25):
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
#Monday2024001Jamal028!🔑95:71
while game:
    pyperclip.copy(a)
    print(a) if a!="quit" else print("Game over.")
    if a=='quit': print('Game over.');quit()
    elif len(a)<8:
        print(f"{length}: {len(a)}")
        print(rule1)
        a = input(ent_password)
    elif contain_digit(a)!="True": 
        print(f"{length}: {len(a)}")
        print(rule2)
        a = input(ent_password)
    elif contain_upper(a)!="True": 
        print(f"{length}: {len(a)}")
        print(rule3)
        a = input(ent_password)
    elif contain_punctuation(a)!="True":
        print(f"{length}: {len(a)}")
        print(rule4)
        a = input(ent_password)
    elif digits_summ(a)!=40:
        print(f"{length}: {len(a)}")
        print(rule5)
        a = input(ent_password)
    elif contain_day(a)!="True":
        print(f"{length}: {len(a)}")
        print(rule6)
        a = input(ent_password)
    elif contain_year(a)!="True": 
        print(f"{length}: {len(a)}")
        print(rule7)
        a = input(ent_password)
    elif not str(len(a)) in a:
        print(f"{length}: {len(a)}")
        print(rule8)
        a = input(ent_password)
    elif not "🔑" in a:
        print(f"{length}: {len(a)}")
        print(rule9)
        a = input(ent_password)
    elif (not name in a) and (not name.lower() in a):
        print(f"{length}: {len(a)}")
        print(rule10)
        a = input(ent_password)
    elif even_length(a)!="True":
        print(f"{length}: {len(a)}")
        print(rule11)
        a = input(ent_password)
    elif contain_time(a)!="True":
        print(f"{length}: {len(a)}")
        print(rule12)
        a = input(ent_password)  
    else:
        game = False
        break
if not game:
    answer = (input(confirm)).lower()
    if (answer=="yes") or (answer=="да"):
        cl();pyperclip.copy('')
        print(login)
        pw = input(ent_password)
        if pw!=a:
            print(lose);print(gameover)
        else:
            print(win)
    else:
        print(gameover)
