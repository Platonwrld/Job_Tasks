# 3 minutes
from typing import List


cities = ['Москва', 'Санкт-Петербург', 'Воронеж']

def convert_array_to_string(lst: List) -> str:
    return ', '.join(lst) + '.'


print(convert_array_to_string(cities)) # -> Москва, Санкт-Петербург, Воронеж.