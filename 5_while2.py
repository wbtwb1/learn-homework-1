"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {}

def ask_user(answers_dict):
    """
    Замените pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    ask_user(questions_and_answers)

# Через цикл for
dict = {
    'Как дела?' : 'Хорошо!', 'Что делаешь?':'Программирую', 'Пойдешь обедать?': 'Конечно' 
}
for q, a in dict.items():
        print (q)
        print (a)

dialogue = {
    'Как дела?' : 'Хорошо!', 'Что делаешь?':'Программирую', 'Пойдешь обедать?': 'Конечно' 
}
while True:
    ask_user = input ('Введите вопрос: ')
    if ask_user == 'Как дела?':
        print ('Хорошо!')
    if ask_user == 'Что делаешь?':
        print ('Программирую')  
    if ask_user == 'Пойдешь обедать?':
        print ('Конечно')  
        break
