# Ввод списка оценок по геометрии
grades = []
for i in range(24):
    grade = int(input(f"Введите оценку ученика {i + 1}: "))
    grades.append(grade)

# Подсчет количества учеников с оценкой "5" без использования условного оператора
count_of_fives = grades[:grades.index(grades[0] - 1)].count(5)

print("Количество учеников с оценкой '5':", count_of_fives)
