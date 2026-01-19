from database import *
from database_change import *
from reports import *

def main_menu():
    """Главное меню программы"""
    print("\nПРОГРАММА 'КВАРТИРОСЪЕМЩИК'")
    print("Сортировка методом Шелла\n")
    print("1. Показать все записи")
    print("2. Отчет 1: Полный список (прописанные↓, адрес↑)")
    print("3. Отчет 2: Квартиросъёмщики с льготами")
    print("4. Отчет 3: Квартиры по диапазону площади")
    print("5. Добавить нового квартиросъемщика")
    print("6. Удалить квартиросъемщика")
    print("7. Изменить данные о существующем квартиросъемщике")
    print("8. Статистика")
    print("9. Сохранить отчет в файл")
    print("10. Сохранить базу данных")
    print("0. Выход\n")


def main():
    """Основная функция программы"""
    database = load_database()

    # Переменные для хранения последних отчетов
    last_report1 = []
    last_report2 = []
    last_report3 = []
    last_n1 = last_n2 = 0
    
    print(f"\nБаза данных загружена. Всего записей: {len(database)}")
    
    while True:
        main_menu()
        choice = input("\nВыберите действие (0-10): ").strip()

        match choice:
            case "0":
                while True:
                    try:
                        save_choice = int(input("Сохранить изменения в базе данных перед выходом? (да - 1/нет - 0): "))
                        if save_choice != 1 and save_choice != 0:
                            print("Ошибка ввода. Попробуйте еще раз.")
                            continue
                        break
                    except:
                        print("Ошибка ввода. Попробуйте еще раз")

                if save_choice == 1:
                    save_database(database)
                print("\nВыход из программы. До свидания!")
                break
                return
        
            case "1":
                display_records(database, "ВСЕ ЗАПИСИ")

            case "2":
                last_report1 = report1_full_list(database)

            case "3":
                last_report2 = report2_with_benefits(database)
                
            case "4":
                result = report3_by_area_range(database)
                if result:
                    last_report3, last_n1, last_n2 = result
                    
            case "5":
                database = add_tenant(database)
                
            case "6":
                database = delete_tenant(database)

            case "7":
                database = change_tenant(database)
                
            case "8":
                show_statistics(database)
                
            case "9":
                if not (last_report1 or last_report2 or last_report3):
                    print("Сначала сформируйте хотя бы один отчет!")
                    continue
                
                print("\n" + "="*50)
                print("СОХРАНЕНИЕ ОТЧЕТА В ФАЙЛ")
                print("="*50)
                
                if last_report1:
                    print("1. Сохранить Отчет 1")
                if last_report2:
                    print("2. Сохранить Отчет 2")
                if last_report3:
                    print("3. Сохранить Отчет 3")
                print("0. Назад")
                
                save_choice = input("Выберите отчет для сохранения: ").strip()
                
                if save_choice == "1" and last_report1:
                    save_report(last_report1, "report1.txt", "ОТЧЕТ 1: Полный список")
                elif save_choice == "2" and last_report2:
                    save_report(last_report2, "report2.txt", "ОТЧЕТ 2: С льготами")
                elif save_choice == "3" and last_report3:
                    title = f"ОТЧЕТ 3: Квартиры площадью {last_n1}-{last_n2} м²"
                    save_report(last_report3, "report3.txt", title)
                elif save_choice == "0":
                    continue
                else:
                    print("Неверный выбор или отчет не сформирован.")
            case "10":
                save_database(database)

            case _:
                print("Неверный выбор. Попробуйте еще раз.")

        input("\nНажмите Enter для продолжения...")



