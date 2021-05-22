"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    """
    Замените pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    hello_user()

while True:
    hello_user = input('Как дела?')
    try: 
        hello_user == ()
    except (KeyboardInterrupt):
        print ('Пока')      
    if hello_user == ('Хорошо'):
        break