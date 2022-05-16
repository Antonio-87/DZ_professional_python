from datetime import datetime

def logger(path):
    def _logger(function):
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            with open(path, 'a', newline='', encoding='utf-8') as file:
                file.write(
                    f"Дата и время вызова функции: {datetime.now().strftime('%d %B %Y %H:%M:%S')};\n"
                    f"Имя фукции: {function.__name__};\n"
                    f"Аргументы: {str(*args, **kwargs)};\n"
                    f"Возвращаемое значение: {list(result)}.\n"
                )
            return result
        return wrapper
    return _logger