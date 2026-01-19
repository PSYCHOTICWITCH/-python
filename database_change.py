def add_tenant(database):
    """Добавление нового квартиросъемщика"""

    print("\nДОБАВЛЕНИЕ НОВОГО КВАРТИРОСЪЕМЩИКА\n")

    # Ввод данных с проверкой

    while True:
        last_name = input("Фамилия: ")
        if not last_name:
            print("Фамилия не может быть пустой!")
            continue
        try:
            float(last_name)
            print("Фамилия не может быть числом")
            continue
        except:
            break

    while True:
        first_name = input("Имя: ")
        if not first_name:
            print("Имя не может быть пустым!")
            continue
        try:
            float(first_name)
            print("Имя не может быть числом")
            continue
        except:
            break

    
    while True:
            middle_name = input("Отчество: ")
            if not middle_name:
                print("Отчество не может быть пустым!")
                continue
            try:
                float(middle_name)
                print("Отчество не может быть числом")
                continue
            except:
                break

    
    while True:
        street = input("Улица: ")
        if not street:
            print("Улица не может быть пустой!")
            continue
        try:
            float(street)
            print("Улица не может быть числом")
            continue
        except:
            break

        

    while True:
            house = input("Дом: ")
            if not house:
                print("Дом не может быть пустым!")
                continue
            break

    while True:
            apartment = input("Квартира: ")
            if not apartment:
                print("Квартира не может быть пустой!")
                continue
            break

    # Ввод числовых значений с проверкой
    while True:
        try:
            floor = int(input("Этаж: "))
            if floor <= 0:
                print("Этаж должен быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
    
    while True:
        try:
            total_area = float(input("Общая площадь (м²): ").strip())
            if total_area <= 0:
                print("Площадь должна быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: введите числовое значение!")
    
    while True:
        try:
            living_area = float(input("Жилая площадь (м²): ").strip())
            if living_area <= 0 or living_area > total_area:
                print(f"Жилая площадь должна быть положительной и не больше общей ({total_area} м²)!")
                continue
            break
        except ValueError:
            print("Ошибка: введите числовое значение!")
    
    while True:
        try:
            registered = int(input("Количество прописанных человек: ").strip())
            if registered <= 0:
                print("Количество должно быть положительным числом!")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число!")
    
    # Ввод наличия льгот
    while True:
        benefits_input = input("Наличие льгот (да/нет): ").strip().lower()
        if benefits_input in ['да', 'д', 'yes', 'y']:
            has_benefits = True
            break
        elif benefits_input in ['нет', 'н', 'no', 'n']:
            has_benefits = False
            break
        else:
            print("Пожалуйста, введите 'да' или 'нет'")
    
    # Создание новой записи
    new_record = (
        last_name, first_name, middle_name,
        street, house, apartment,
        floor, total_area, living_area,
        registered, has_benefits
    )
    
    database.append(new_record)
    print(f"\nКвартиросъемщик {last_name} {first_name} {middle_name} успешно добавлен!")
    return database


def delete_tenant(database):
    """Удаление квартиросъемщика"""
    if not database:
        print("База данных пуста!")
        return database
    
    print("\nУДАЛЕНИЕ КВАРТИРОСЪЕМЩИКА\n")
    
    # Показываем список для выбора
    print("Список квартиросъемщиков:")
    for i, record in enumerate(database, 1):
        print(f"{i}. {record[0]} {record[1]} {record[2]} - "
              f"{record[3]}, д.{record[4]}, кв.{record[5]}")
    
    # Выбор записи для удаления
    while True:
        try:
            choice = input(f"\nВведите номер записи для удаления (1-{len(database)}) "
                          "или 0 для отмены: ").strip()
            
            if choice == '0':
                print("Удаление отменено.")
                return database
            
            index = int(choice) - 1
            
            if 0 <= index < len(database):
                removed = database.pop(index)
                print(f"Запись удалена: {removed[0]} {removed[1]} {removed[2]}")
                return database
            else:
                print(f"Неверный номер! Введите число от 1 до {len(database)}")
        
        except ValueError:
            print("Ошибка: введите число!")





def change_tenant(database):
    """Изменение квартиросъемщика"""
    if not database:
        print("База данных пуста!")
        return database
    
    print("\nИЗМЕНЕНИЕ КВАРТИРОСЪЕМЩИКА\n")
    
    # Показываем список для выбора
    print("Список квартиросъемщиков:")
    for i, record in enumerate(database, 1):
        print(f"{i}. {record[0]} {record[1]} {record[2]} - "
              f"{record[3]}, д.{record[4]}, кв.{record[5]}")
    
    while True:
        try:
            choice = input(f"\nВведите номер записи для изменения (1-{len(database)}) "
                          "или 0 для отмены: ").strip()
            
            if choice == '0':
                print("Изменение отменено.")
                return database
            
            index = int(choice) - 1
            
            if 0 >= index or index > len(database):
                print(f"Неверный номер! Введите число от 1 до {len(database)}")
                continue
            break
        
        except ValueError:
            print("Ошибка: введите число!")

    while True:
        print("1 - Фамилия")
        print("2 - Имя")
        print("3 - Отчество")
        print("4 - Улица")
        print("5 - Дом")
        print("6 - Квартира")
        print("7 - Этаж")
        print("8 - Общая площадь")
        print("9 - Жилая площадь")
        print("10 - Количество прописанных")
        print("11 - Наличие льготы")
        print("0 - Выход")
            
        option = int(input("Введите, что хотели бы изменить (0 - 11)"))
            
        match option:
                
            case 0:
                print("Изменения сохранены")
                return database
                
            case 1:
                while True:
                    last_name = input("Фамилия: ")
                    if not last_name:
                        print("Фамилия не может быть пустой!")
                        continue
                    try:
                        float(last_name)
                        print("Фамилия не может быть числом")
                        continue
                    except:
                        break
                    
                tenant = list(database.pop(index))
                tenant[0] = last_name
                database.insert(index, tuple(tenant))
                    
            case 2:
                while True:
                    first_name = input("Имя: ")
                    if not first_name:
                        print("Имя не может быть пустым!")
                        continue
                    try:
                        float(first_name)
                        print("Имя не может быть числом")
                        continue
                    except:
                        break
                tenant = list(database.pop(index))
                tenant[1] = first_name
                database.insert(index, tuple(tenant))

            case 3:
                while True:
                    middle_name = input("Отчество: ")
                    if not middle_name:
                        print("Отчество не может быть пустым!")
                        continue
                    try:
                        float(middle_name)
                        print("Отчество не может быть числом")
                        continue
                    except:
                        break
                tenant = list(database.pop(index))
                tenant[2] = middle_name
                database.insert(index, tuple(tenant))
                        
            case 4:
                while True:
                    street = input("Улица: ")
                    if not street:
                        print("Улица не может быть пустой!")
                        continue
                    try:
                        float(street)
                        print("Улица не может быть числом")
                        continue
                    except:
                        break
                tenant = list(database.pop(index))
                tenant[3] = street
                database.insert(index, tuple(tenant))
                    
            case 5:
                while True:
                    house = input("Дом: ")
                    if not house:
                        print("Дом не может быть пустым!")
                        continue
                    break
                tenant = list(database.pop(index))
                tenant[4] = house
                database.insert(index, tuple(tenant))
                    
            case 6:
                while True:
                    apartment = input("Квартира: ")
                    if not apartment:
                        print("Квартира не может быть пустой!")
                        continue
                    break
                tenant = list(database.pop(index))
                tenant[5] = apartment
                database.insert(index, tuple(tenant))
                    
            case 7:
                while True:
                    try:
                        floor = int(input("Этаж: "))
                        if floor <= 0:
                            print("Этаж должен быть положительным числом!")
                            continue
                        break
                    except ValueError:
                        print("Ошибка: введите целое число!")
                tenant = list(database.pop(index))
                tenant[6] = floor
                database.insert(index, tuple(tenant))
                            
            case 8:
                while True:
                    try:
                        total_area = float(input("Общая площадь (м²): ").strip())
                        if total_area <= 0:
                            print("Площадь должна быть положительным числом!")
                            continue
                        break
                    except ValueError:
                        print("Ошибка: введите числовое значение!")
                tenant = list(database.pop(index))
                tenant[7] = total_area
                database.insert(index, tuple(tenant))
                    
            case 9:
                while True:
                    try:
                        living_area = float(input("Жилая площадь (м²): ").strip())
                        if living_area <= 0 or living_area > total_area:
                            print(f"Жилая площадь должна быть положительной и не больше общей ({total_area} м²)!")
                            continue
                        break
                    except ValueError:
                        print("Ошибка: введите числовое значение!")
                tenant = list(database.pop(index))
                tenant[8] = living_area
                database.insert(index, tuple(tenant))
                    
            case 10:
                while True:
                    try:
                        registered = int(input("Количество прописанных человек: ").strip())
                        if registered <= 0:
                            print("Количество должно быть положительным числом!")
                            continue
                        break
                    except ValueError:
                        print("Ошибка: введите целое число!")
                tenant = list(database.pop(index))
                tenant[9] = registered
                database.insert(index, tuple(tenant))
                    
            case 11:
                while True:
                    benefits_input = input("Наличие льгот (да/нет): ").strip().lower()
                    if benefits_input in ['да', 'д', 'yes', 'y']:
                        has_benefits = True
                        break
                    elif benefits_input in ['нет', 'н', 'no', 'n']:
                        has_benefits = False
                        break
                    else:
                        print("Пожалуйста, введите 'да' или 'нет'")
                tenant = list(database.pop(index))
                tenant[10] = benefits_input
                database.insert(index, tuple(tenant))
            case _:
                print("Неверный номер!")
