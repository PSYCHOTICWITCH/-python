def shell_sort(array, key_func=None, reverse=False):
    """
    Реализация сортировки методом Шелла с поддержкой многоуровневой сортировки
    """
    n = len(array)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            
            # Сравниваем элементы с учетом всех ключей
            while j >= gap:
                current = array[j - gap]
                
                # Сравниваем значения
                if key_func:
                    temp_val = key_func(temp)
                    current_val = key_func(current)
                    
                    # Если нужно сравнить по нескольким критериям
                    if isinstance(temp_val, tuple) and isinstance(current_val, tuple):
                        comparison_result = 0
                        for k in range(len(temp_val)):
                            if current_val[k] != temp_val[k]:
                                if not reverse:
                                    comparison_result = 1 if current_val[k] > temp_val[k] else -1
                                else:
                                    comparison_result = -1 if current_val[k] > temp_val[k] else 1
                                break
                        
                        if comparison_result > 0:  # current > temp (для возрастания)
                            array[j] = array[j - gap]
                            j -= gap
                        else:
                            break
                    else:
                        # Для одиночных ключей
                        if (not reverse and current_val > temp_val) or (reverse and current_val < temp_val):
                            array[j] = array[j - gap]
                            j -= gap
                        else:
                            break
                else:
                    # Сортировка без ключевой функции
                    if (not reverse and current > temp) or (reverse and current < temp):
                        array[j] = array[j - gap]
                        j -= gap
                    else:
                        break
            
            array[j] = temp
        
        gap //= 2
    
    return array
