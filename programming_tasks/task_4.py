# 20 minutes
def is_num_prime_or_not(num: int) -> bool:
    if num <= 1:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

print(is_num_prime_or_not(12))