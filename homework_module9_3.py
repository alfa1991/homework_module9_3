first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторное выражение для вычисления разницы длин строк из списков first и second, если их длины не равны
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторное выражение для сравнения длин строк из списков first и second (без использования zip)
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Вывод результатов
print(list(first_result))  # Ожидаемый вывод: [1, 2]
print(list(second_result))  # Ожидаемый вывод: [False, False, True]
