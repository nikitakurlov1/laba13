class DynamicClass:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        attributes = [f"{key}={value}" for key, value in self.__dict__.items()]
        return f"DynamicClass({', '.join(attributes)})"

# Пример использования
if __name__ == "__main__":
    # Создаем экземпляр класса с динамическими атрибутами
    obj = DynamicClass(name="Test", value=42, is_active=True)
    
    # Выводим все атрибуты объекта
    print("Атрибуты объекта:")
    for attr_name in dir(obj):
        if not attr_name.startswith('__'):
            attr_value = getattr(obj, attr_name)
            print(f"{attr_name}: {attr_value}")
    
    # Изменяем атрибуты динамически
    setattr(obj, 'new_attribute', 'New Value')
    print("\nПосле добавления нового атрибута:")
    print(obj) 