from shellsort import *

def display_records(records, title="Список квартиросъемщиков"):
    """Отображение записей в виде списка"""
    print(f"{title.upper()}")
    
    if not records:
        print("Нет данных для отображения")
        return
    
    for i, record in enumerate(records, 1):
        print(f"{i}. ФИО: {record[0]} {record[1]} {record[2]}")
        print(f"   Адрес: ул. {record[3]}, д.{record[4]}, кв.{record[5]}")
        print(f"   Этаж: {record[6]}")
        print(f"   Площадь: общая {record[7]:.1f} м², жилая {record[8]:.1f} м²")
        print(f"   Прописано: {record[9]} человек")
        print(f"   Льготы: {'Да' if record[10] else 'Нет'}\n")
    
    print(f"Всего записей: {len(records)}\n")


def save_report(records, filename, title="Отчет"):
    """Сохранение отчета в файл в виде списка"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(f"{title}\n")
            
            for i, record in enumerate(records, 1):
                file.write(f"{i}. ФИО: {record[0]} {record[1]} {record[2]}\n")
                file.write(f"   Адрес: ул. {record[3]}, д.{record[4]}, кв.{record[5]}\n")
                file.write(f"   Этаж: {record[6]}\n")
                file.write(f"   Площадь: общая {record[7]:.1f} м², жилая {record[8]:.1f} м²\n")
                file.write(f"   Прописано: {record[9]} человек\n")
                file.write(f"   Льготы: {'Да' if record[10] else 'Нет'}\n")
            
            file.write(f"\nВсего записей: {len(records)}\n")
        
        print(f"Отчет сохранен в файл: {filename}")
    
    except Exception as e:
        print(f"Ошибка при сохранении отчета: {e}")


def report1_full_list(database):
    """
    ОТЧЕТ 1: Полный список всех квартиросъёмщиков
    Сортировка: количество прописанных (↓) + адрес (↑)
    """
    print("\nФОРМИРОВАНИЕ ОТЧЕТА 1")
    print("Сортировка: количество прописанных (по убыванию) + адрес (по возрастанию)\n")
    
    records = database.copy()
    
    def get_sort_key(record):
        """
        Ключ для сортировки: сначала по прописанным (убывание), потом по адресу (возрастание)
        Для убывания используем отрицательное число
        """
        # Ключ для адреса
        street = record[3].lower()
        
        # Номер дома
        house = record[4]
        house_num = 0
        house_digits = ''.join(filter(str.isdigit, str(house)))
        if house_digits:
            house_num = int(house_digits)
        
        # Номер квартиры
        apartment = record[5]
        apartment_num = 0
        apartment_digits = ''.join(filter(str.isdigit, str(apartment)))
        if apartment_digits:
            apartment_num = int(apartment_digits)
        
        # Возвращаем кортеж: (-прописанные для убывания, улица, дом, квартира)
        return (-record[9], street, house_num, apartment_num)
    
    # сортировка с многоуровневым ключом
    records = shell_sort(records, key_func=get_sort_key, reverse=False)
    
    display_records(records, "ОТЧЕТ 1: Полный список квартиросъёмщиков")
    return records


def report2_with_benefits(database):
    """
    ОТЧЕТ 2: Список квартиросъёмщиков с льготами
    Сортировка: этаж (↑) + прописанные (↓) + общая площадь (↑)
    """
    print("\nФОРМИРОВАНИЕ ОТЧЕТА 2\n")
    
    filtered = [record for record in database if record[10]]
    print(f"Найдено квартиросъёмщиков с льготами: {len(filtered)}")
    
    if not filtered:
        print("Нет записей для отчета!")
        return []
    
    def get_sort_key(record):
        """
        Ключ для сортировки:
        - этаж (возрастание)
        - прописанные (убывание) - используем отрицательное число
        - площадь (возрастание)
        """
        return (record[6], -record[9], record[7])
    
    # сортировка с многоуровневым ключом
    filtered = shell_sort(filtered, key_func=get_sort_key, reverse=False)
    
    display_records(filtered, "ОТЧЕТ 2: Квартиросъёмщики с льготами")
    return filtered


def report3_by_area_range(database):
    """
    ОТЧЕТ 3: Квартиры в диапазоне площади
    Сортировка: льготы (↑) + общая площадь (↓)
    """
    print("\nФОРМИРОВАНИЕ ОТЧЕТА 3\n")
    
    while True:
        try:
            n1_input = float(input("Введите минимальную площадь N1 (м²): "))
            n2_input = float(input("Введите максимальную площадь N2 (м²): "))
            
            if n1_input < 0 or n2_input < 0:
                print("Площадь не может быть отрицательной. Попробуйте снова.")
                continue
            
            if n1_input > n2_input:
                n1_input, n2_input = n2_input, n1_input
                print(f"Диапазон автоматически изменен на: {n1_input}-{n2_input} м²")
            
            break
        
        except ValueError:
            print("Ошибка: введите числовые значения. Попробуйте снова.")
    
    filtered = [record for record in database if n1_input <= record[7] <= n2_input]
    print(f"Найдено квартир площадью {n1_input}-{n2_input} м²: {len(filtered)}")
    
    if not filtered:
        print("Нет записей для отчета!")
        return []
    
    def get_sort_key(record):
        """
        Ключ для сортировки:
        - льготы (возрастание: False=0, True=1)
        - площадь (убывание) - используем отрицательное число
        """
        return (0 if not record[10] else 1, -record[7])
    
    # сортировка с многоуровневым ключом
    filtered = shell_sort(filtered, key_func=get_sort_key, reverse=False)
    
    title = f"ОТЧЕТ 3: Квартиры площадью {n1_input}-{n2_input} м²"
    display_records(filtered, title)
    return filtered, n1_input, n2_input
def show_statistics(database):
    """Показать статистику по базе данных"""
    if not database:
        print("База данных пуста!")
        return
    
    total = len(database)
    with_benefits = sum(1 for record in database if record[10])
    total_area = sum(record[7] for record in database)
    total_living_area = sum(record[8] for record in database)
    total_people = sum(record[9] for record in database)
    
    print("\nСТАТИСТИКА БАЗЫ ДАННЫХ\n")
    print(f"Всего квартиросъёмщиков: {total}")
    print(f"С льготами: {with_benefits} ({with_benefits/total*100:.1f}%)")
    print(f"Без льгот: {total - with_benefits} ({(total-with_benefits)/total*100:.1f}%)")
    print(f"Общая площадь всех квартир: {total_area:.1f} м²")
    print(f"Общая жилая площадь: {total_living_area:.1f} м²")
    print(f"Всего прописано человек: {total_people}")
    print(f"Средняя площадь на квартиру: {total_area/total:.1f} м²")
    print(f"Среднее количество человек на квартиру: {total_people/total:.1f}\n")
