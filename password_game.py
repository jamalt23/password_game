import pyperclip
from string import punctuation
from os import system
from datetime import datetime

clear_terminal = lambda: system('clear')
clear_clipboard = lambda: pyperclip.copy('')

print("Original game: neal.fun/password-game")
days = ["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье",
        "monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
lang=(input("Select language(Russian/English): ")).lower()
if lang!='quit':
    while not lang in ('russian', 'ru', 'english', 'en'):
        print("Invalid: You are Invalid")
        lang=(input("Select language(Russian/English): ")).lower()
else:
    print('Good bye!')
    quit()

MESSAGES_EN = {
    'length': 'Length', 'ent_password': 'Enter your password: ', 'ent_name': 'Enter your name: ',
    'signup': 'Sign up', 'login': 'Log in', 'lose': 'Your password is wrong.', 'gameover': 'Game over.',
    'confirm': 'Do you confirm that this is your password?(Yes or Yes) ',
    'rule1': 'Your password must be at least 8 characters',
    'rule2': 'Your password must include a number',
    'rule3': 'Your password must include an uppercase letter',
    'rule4': 'Your password must include a special character',
    'rule5': 'The digits in your password must add up to 40',
    'rule6': 'Your password must include a day of the week',
    'rule7': 'Your password must include current year',
    'rule8': 'Your password must include the length of your password',
    'rule9': 'Your password must include the key🔑 emoji',
    'rule10': 'Your password must include your name',
    'rule11': 'The length of your password must be even number',
    'rule12': 'Your password must include the current time backwards (Example: 01:02 -> 20:10)',
    'win': 'Successful! Welcome, {}.\nYou won!'
}
MESSAGES_RU = {
    'length': 'Длина', 'ent_password': 'Введите пароль: ', 'ent_name': 'Введите ваше имя: ',
    'signup': 'Регистрация', 'login': 'Вход', 'lose': 'Неверный пароль.', 'gameover': 'Игра окончена.',
    'confirm': 'Вы подтверждаете что это ваш пароль?(Да или Да) ',
    'rule1': 'Ваш пароль должен быть не менее 8 символов в длину',
    'rule2': 'Ваш пароль должен содержать хоть одну цифру',
    'rule3': 'Ваш пароль должен содержать заглавную букву',
    'rule4': 'Ваш пароль должен содержать любой знак пунктуации',
    'rule5': 'Сумма цифр в вашем пароле должна быть 40',
    'rule6': 'Ваш пароль должен содержать день недели',
    'rule7': 'Ваш пароль должен содержать текущий год',
    'rule8': 'Ваш пароль должен содержать длину вашего пароля',
    'rule9': 'Ваш пароль должен содержать эмодзи ключа🔑',
    'rule10': 'Ваш пароль должен содержать ваше имя',
    'rule11': 'Длина вашего пароля должна быть чётным числом',
    'rule12': 'Ваш пароль должен содержать текущее время обратное (Пример: 01:02 -> 20:10)',
    'win': 'Успешно! Добро пожаловать, {}.\nВы победили!'
}

if lang in ("english","en"):
    messages = MESSAGES_EN
elif lang in ("russian","ru"):
    messages = MESSAGES_RU

print(messages['signup'])
name = input(messages['ent_name'])
messages['win'] = messages['win'].format(name)

#Monday2024001Jamal028!🔑95:71

contain_digit = lambda x: any(char.isdigit() for char in x)
contain_upper = lambda x: any(char.isupper() for char in x)
contain_punctuation = lambda x: any(char in punctuation for char in x)
digits_summ = lambda x: sum(int(char) for char in x if char.isdigit())
contain_day = lambda x: any(day.lower() in x.lower() for day in days)
contain_year = lambda x: str(datetime.now().year) in x
even_length = lambda x: len(x)%2==0
contain_time = lambda x: datetime.now().strftime("%H:%M")[::-1] in x

class Password:
    def __init__(self: object, password: str):
        self.password = password
        self.length = len(password)
        self.length_rule = len(password) >= 8 # rule 1
        self.contain_digit = contain_digit(password) # rule 2
        self.contain_upper = contain_upper(password) # rule 3
        self.contain_punctuation = contain_punctuation(password) # rule 4
        self.digits_summ = digits_summ(password) # rule 5
        self.contain_day = contain_day(password) # rule 6
        self.contain_year = contain_year(password) # rule 7
        self.contain_key = '🔑' in password # rule 9
        self.contain_name = name in password # rule 10
        self.even_length = even_length(password) # rule 11
        self.contain_time = contain_time(password) # rule 12
        self.rules = [self.length_rule, self.contain_digit, self.contain_upper, self.contain_punctuation,
                      self.digits_summ, self.contain_day, self.contain_year, self.contain_key,
                      self.contain_name, self.even_length, self.contain_time]

    def __str__(self: object) -> str:
        return self.password

    def is_valid(self: object) -> bool:
        return all(self.rules)

    def check_rules(self: object) -> bool | str:
        for rule in self.rules:
            rule_message = messages[f'rule{self.rules.index(rule)+1}']
            if not rule:
                return rule_message
        return True

password = Password(input(messages['ent_password']))

while True:
    pyperclip.copy(password.password)
    print(password) if password!="quit" else print("Game over.")
    if password.is_valid():
        break
    else:
        print(password.check_rules())
        password = Password(input(messages['ent_password']))

answer = (input(messages['confirm'])).lower()
if answer in ('yes', 'y', 'да'):
    clear_terminal()
    clear_clipboard()
    print(messages['login'])
    if input(messages['ent_password'])!=password:
        print(messages['lose'], messages['gameover'], sep='\n')
    else:
        print(messages['win'])
else:
    print(messages['gameover'])
