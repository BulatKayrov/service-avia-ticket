# Что нужно сделать
Необходимо создать сервис поиска авиабилетов в виде консольного приложения.
Основные функции приложения:
- создание нового рейса;
- вывод информации обо всех рейсах;
- вывод информации о конкретном рейсе.


## Требования к коду

- Из встроенных функций нужно использовать только ввод (input) и вывод
(print).
- Преобразование типов выполнять только на вводе (some_variable =
int(input("Enter some number"))
- Нельзя использовать методы строк и прочие встроенные методы Python.
- Вложенные однотипные циклы недопустимы:
  - for ...:
    - for ...:
- Вложенные разнотипные циклы допустимы для проверки пользовательского
ввода только в основной функции. Уровней вложенности должно быть не
больше двух:
  - for ...:
    - while ...:
- В условиях должно быть не более двух уровней вложенности:
  - if ...:
    - if ...:
- Функция должна возвращать не более одного однотипного значения или не
возвращать ничего:
  - def some_function():
    - if ...:
      - return 1
    - return 0
- Каждая отдельно взятая функция должна выполнять только одно действие:
  - def cubes(number):
    - cube = number ** 3
        - return cube
- Нельзя использовать global.