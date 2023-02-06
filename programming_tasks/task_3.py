# 15 minutes
def return_right_string(num: int) -> str:
    if num % 10 == 1:
        return str(num) + ' компьютер'
    
    if num % 10 in range(2, 5):
        return str(num) + ' компьютера'
    
    return str(num) + ' компьютеров'

print(return_right_string(25))