"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
#task3 FOR 1.1
list = [1,5,3,8,5,11,7,23,9,10]
for number in list:
    number += 1
    print (number)

#task3 FOR 1.2
a = 'Hello Moto'
for word in a:
    print (word)

# task3 FOR 1.3 
student_scores = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5a', 'scores': [3,4,5,5,3]},
    {'school_class': '7a', 'scores': [3,3,4,5,2]},
]
scores_sum = 0
for scores in (student_scores[0]['scores'])+(student_scores[1]['scores'])+(student_scores[1]['scores']):
    scores_sum = scores_sum + scores
scores_avg = scores_sum/ len ((student_scores[0]['scores'])+(student_scores[1]['scores'])+(student_scores[1]['scores']))
print (f'Средний балл по всей школе: {scores_avg}')

for scores in student_scores[0]['scores']:
    scores_avg = sum (student_scores [0]['scores'])/ len ((student_scores[0]['scores']))
    print (f'Средний балл по 4а классу: {scores_avg}')
    break 
for scores in student_scores[1]['scores']:
    scores_avg = sum (student_scores [1]['scores'])/ len ((student_scores[0]['scores']))
    print (f'Средний балл по 5а классу: {scores_avg}')
    break 
for scores in student_scores[2]['scores']:
    scores_avg = sum (student_scores [2]['scores'])/ len ((student_scores[0]['scores']))
    print (f'Средний балл по 7а классу: {scores_avg}')
    break 


# print (f'Средняя оценка 4а класса: {(sum(student_scores[1]['scores'])/len(student_scores[1]['scores'])})
