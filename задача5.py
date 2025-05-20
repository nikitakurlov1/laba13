def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Вызывается функция: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Пример использования с функцией
@log_function_call
def test_function(x, y):
    return x + y

# Пример использования с методом класса
class TestClass:
    @log_function_call
    def test_method(self, x, y):
        return x * y

if __name__ == "__main__":
    # Тестируем функцию
    result = test_function(5, 3)
    print(f"Результат функции: {result}")
    
    # Тестируем метод
    obj = TestClass()
    result = obj.test_method(4, 2)
    print(f"Результат метода: {result}") 