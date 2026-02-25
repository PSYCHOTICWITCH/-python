def load_database(filename="database.txt"):
    """
    Загрузка базы данных из текстового файла.
    Каждая строка в файле должна содержать данные в формате:
    фамилия имя отчество улица дом квартира этаж общая_площадь жилая_площадь прописанольготы
    """
    database = []
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) == 11:
                        # Преобразуем строки в нужные типы данных
                        record = (
                            parts[0].strip(),      # фамилия
                            parts[1].strip(),      # имя
                            parts[2].strip(),      # отчество
                            parts[3].strip(),      # улица
                            int(parts[4].strip()), # дом
                            int(parts[5].strip()), # квартира
                            int(parts[6].strip()), # этаж
                            float(parts[7].strip()), # общая площадь
                            float(parts[8].strip()), # жилая площадь
                            int(parts[9].strip()), # прописано
                            parts[10].strip().lower() == 'да'  # льготы (bool)
                        )
                        database.append(record)
        
        print(f"Загружено {len(database)} записей из файла {filename}")
        return database
    
    except FileNotFoundError:
        print(f"Файл {filename} не найден. Создана пустая база данных.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
        return []


def save_database(database, filename="database.txt"):
    """Сохранение базы данных в текстовый файл"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for record in database:
                line = (f"{record[0]} {record[1]} {record[2]} {record[3]} "
                       f"{record[4]} {record[5]} {record[6]} {record[7]:.1f} "
                       f"{record[8]:.1f} {record[9]} "
                       f"{'Да' if record[10] else 'Нет'}")
                file.write(line + '\n')
        
        print(f"База данных сохранена в файл {filename} ({len(database)} записей)")
    
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")
