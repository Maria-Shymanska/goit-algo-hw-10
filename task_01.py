# Завдання 1. Оптимізація виробництва
'''Компанія виробляє два види напоїв: "Лимонад" і "Фруктовий сік".
Для виробництва цих напоїв використовуються різні інгредієнти та обмежена кількість обладнання.
Задача полягає у максимізації виробництва, враховуючи обмежені ресурси.
Умови завдання:

1."Лимонад" виготовляється з "Води", "Цукру" та "Лимонного соку".
2."Фруктовий сік" виготовляється з "Фруктового пюре" та "Води".
3.Обмеження ресурсів: 100 од. "Води", 50 од. "Цукру", 30 од. "Лимонного соку" та 40 од. "Фруктового пюре".
4.Виробництво одиниці "Лимонаду" вимагає 2 од. "Води", 1 од. "Цукру" та 1 од. "Лимонного соку".
5.Виробництво одиниці "Фруктового соку" вимагає 2 од. "Фруктового пюре" та 1 од. "Води".'''

import pulp

# Оголошуємо задачу
problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

# Змінні рішення
lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Continuous')
fruit_juice = pulp.LpVariable('FruitJuice', lowBound=0, cat='Continuous')

# Об'єктивна функція (максимізація загальної кількості продуктів)
problem += lemonade + fruit_juice, "Total_Production"

# Обмеження на ресурси
problem += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"
problem += 1 * lemonade <= 50, "Sugar_Constraint"
problem += 1 * lemonade <= 30, "LemonJuice_Constraint"
problem += 2 * fruit_juice <= 40, "FruitPuree_Constraint"

# Розв'язуємо задачу
problem.solve()

# Результати
print(f"Status: {pulp.LpStatus[problem.status]}")
print(f"Optimal number of Lemonade to produce: {pulp.value(lemonade)}")
print(f"Optimal number of Fruit Juice to produce: {pulp.value(fruit_juice)}")
