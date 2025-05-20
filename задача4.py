def log_class_instantiation(cls):
    original_init = cls.__init__
    
    def new_init(self, *args, **kwargs):
        print(f"Создается экземпляр класса: {cls.__name__}")
        original_init(self, *args, **kwargs)
    
    cls.__init__ = new_init
    return cls

# Пример использования
@log_class_instantiation
class TestClass:
    def __init__(self, value):
        self.value = value
    
    def get_value(self):
        return self.value

@log_class_instantiation
class AnotherClass:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

if __name__ == "__main__":
    # Создаем экземпляры классов
    obj1 = TestClass(42)
    obj2 = AnotherClass("Test")
    
    # Проверяем работу методов
    print(f"Значение из TestClass: {obj1.get_value()}")
    print(f"Имя из AnotherClass: {obj2.get_name()}") 