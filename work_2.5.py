import time
import datetime

class Time:

    def __init__(self, name_text):
        self.name_text = name_text
        print(f'Время начало работы {datetime.datetime.utcnow()}')
        self.diff_time = time.time()

    def __enter__(self):
        self.text_s = open(self.name_text, 'w', encoding='utf8' )
        return self.text_s

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.text_s.close()
        self.account = time.time() - self.diff_time

        print(f'\nПродолжительность работы: {self.account}')
        print(f'Время завершения работы {datetime.datetime.utcnow()}')

with Time('number.json') as different_time:
    different_time.write('Засекаем время работы программы')
    time.sleep(1)
