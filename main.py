def is_correct_number_flight(num: str, len_str: int) -> bool:
    """Проверка номера рейса на корректность содержания len_str символов"""
    count = 0
    for i in num:
        count += 1

    if count == len_str:
        return True
    else:
        return False


def is_correct_date(date: str, len_date: int) -> bool:
    """Проверка даты вылета на корректность содержания len_date символов"""
    count = 0
    for i in date:
        count += 1
    if count == len_date:
        return True
    else:
        return False


def is_correct_time_in(data: str, len_date: int) -> bool:
    """Проверка время вылета на корректность содержания len_date символов"""
    count = 0
    for i in data:
        count += 1
    if count == len_date:
        return True
    else:
        return False


def is_correct_time_out(data: str) -> bool:
    """Проверка времени перелета на отстутствия отрицательных чисел"""
    count = 0
    for i in data:
        count += 1
        if i == '-' and count == 1:
            return False
        else:
            if count == 2:
                return True


def is_correct_iata_air_in_out(data: str, digit: int) -> bool:
    """Проверка Код ИАТА на корректность содержания digit символов"""
    count = 0
    for i in data:
        count += 1
    if count == digit:
        return True
    else:
        return False


def is_correct_price(data: str) -> bool:
    """Проверка стоимости на корректность содержания digit символов"""
    count = 0
    for i in data:
        count += 1
        if i == '-' and count == 1:
            return False
        else:
            return True


def save_data(data1=None):
    storage = data1
    return storage


def print_flight():
    data = save_data()
    result = ''
    count = 0
    for i in data:
        count += 1
        if i == ' ' and count == 1:
            print('Информация о рейсах отсутствует')
            break
        elif i != '|':
            result += i
        else:
            print('Информация о рейсе:' + result + '\n')
            result = ''


def start():
    print('\nВведите данные рейса: ')
    number_flight = input('ХХХХ - номер рейса: ')
    date_sorties = input('ДД/ММ/ГГГГ - дата рейса: ')
    time_sorties = input('ЧЧ:ММ - время вылета: ')
    time_fly = input('ХХ.ХХ - длительность перелета: ')
    airport_sorties = input('ХХХ - аэропорт вылета: ')
    airport_arrival = input('ХХХ - аэропорт назвачения: ')
    price_sorties = input('.ХХ - стоимость билета (>0): ')
    if is_correct_number_flight(number_flight, 4) and is_correct_date(date_sorties, 10) and \
            is_correct_time_in(time_sorties, 5) and is_correct_time_out(time_fly) and \
            is_correct_iata_air_in_out(airport_sorties, 3) and is_correct_iata_air_in_out(airport_arrival, 3) and \
            is_correct_price(price_sorties):
        storage = number_flight + ' ' + date_sorties + ' ' + time_sorties + ' ' + time_fly + ' ' + airport_sorties + \
                  ' ' + airport_arrival + ' ' + price_sorties
        print(f'Информация о рейсе {storage}* добавлена')
        return storage + '|'
    else:
        print('Ошибка ввода данных. Повторите ввод\n')


def search_to_numbers(text: str, storage: str):
    res = ''
    for i in storage:
        if i != '|':
            res += i
        elif text in res:
            return f'Информация о рейсе: {res} '
        else:
            res = ''
    return f'Рейс {text} не найден'


if __name__ == '__main__':
    save_storage = ''
    while True:
        # save_storage = ''
        print('\nГлавное меню:\n')
        print(1, ' - ввод рейса')
        print(2, ' - вывод всех рейсов')
        print(3, ' - поиск рейса по номеру')
        print(0, ' - завершение работы\n')
        action = int(input('Введите номер пункта меню: '))
        if action == 1:
            save_storage += start()

        elif action == 2:
            result = ''
            count = 0
            if save_storage == '':
                print('Информация о рейсах отсутствует')
            else:
                for i in save_storage:
                    count += 1
                    if i == '|':
                        print('Информация о рейсе: ' + result)
                        result = ''
                    else:
                        result += i
        elif action == 3:
            data = input('Введите номер рейса в формате ХХХХ: ')
            new_data = search_to_numbers(text=data, storage=save_storage)
            print(new_data)
        else:
            break


