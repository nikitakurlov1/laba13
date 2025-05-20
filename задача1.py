def isIterable(obj):
    """
    Проверяет, поддерживает ли объект итерационный протокол
    """
    try:
        iter(obj)
        return True
    except TypeError:
        return False

# Тестовые объекты
test_objects = [
    [1, 2, 3],           # список
    (1, 2, 3),           # кортеж
    {1, 2, 3},           # множество
    {'a': 1, 'b': 2},    # словарь
    "Hello",             # строка
    42,                  # число
    True,                # булево значение
    None                 # None
]

# Проверяем каждый объект
for obj in test_objects:
    if isIterable(obj):
        print(f"\nОбъект {obj} поддерживает итерационный протокол:")
        for item in obj:
            print(item, end=' ')
    else:
        print(f"\nОбъект {obj} не поддерживает итерационный протокол") 