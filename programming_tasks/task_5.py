# 20 minute
from typing import List


def find_duplicates(arr1: List, arr2: List) -> List:
    result = []
    
    for i in arr1:
        if arr1.count(i) >= 2 and arr2.count(i) >= 2:
            if i not in result:
                result.append(i)
            
    return result