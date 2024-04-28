import pyperclip
from string import punctuation
from os import system
from datetime import datetime

clear_terminal = lambda: system('clear')
clear_clipboard = lambda: pyperclip.copy('')

print("Original game: neal.fun/password-game")
current_year = str(datetime.now().year)
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

contain_digit = lambda x: any(char.isdigit() for char in x)
contain_upper = lambda x: any(char.isupper() for char in x)
contain_punctuation = lambda x: any(char in punctuation for char in x)
digits_summ = lambda x: sum(int(char) for char in x)
contain_day = lambda x: any(day in x for day in days)
contain_year = lambda x: current_year in x
even_length = lambda x: len(x)%2==0
contain_time = lambda x: datetime.now().strftime("%H:%M")[::-1] in x

#Monday2024001Jamal028!🔑95:71

while game:
    pyperclip.copy(a)
    print(a) if a!="quit" else print("Game over.")
    if a=='quit': print('Game over.');quit()
    elif len(a)<8:
        print(f"{length}: {len(a)}")
        print(rule1)
        a = input(ent_password)
    elif not contain_digit(a): 
        print(f"{length}: {len(a)}")
        print(rule2)
        a = input(ent_password)
    elif not contain_upper(a): 
        print(f"{length}: {len(a)}")
        print(rule3)
        a = input(ent_password)
    elif not contain_punctuation(a):
        print(f"{length}: {len(a)}")
        print(rule4)
        a = input(ent_password)
    elif not digits_summ(a)!=40:
        print(f"{length}: {len(a)}")
        print(rule5)
        a = input(ent_password)
    elif not contain_day(a):
        print(f"{length}: {len(a)}")
        print(rule6)
        a = input(ent_password)
    elif not contain_year(a): 
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
    elif not even_length(a):
        print(f"{length}: {len(a)}")
        print(rule11)
        a = input(ent_password)
    elif not contain_time(a):
        print(f"{length}: {len(a)}")
        print(rule12)
        a = input(ent_password)  
    else:
        game = False
        break
if not game:
    answer = (input(confirm)).lower()
    if (answer=="yes") or (answer=="да"):
        clear_terminal()
        clear_clipboard()
        print(login)
        pw = input(ent_password)
        if pw!=a:
            print(lose);print(gameover)
        else:
            print(win)
    else:
        print(gameover)
