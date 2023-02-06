# 30 minutes
def print_multiplication_table(num: int) -> str:
    for i in range(1, num + 1):
        for j in range(1, num + 1):
            print(f'{i * j:4}', end='')
            
        print()
        
print_multiplication_table(5)