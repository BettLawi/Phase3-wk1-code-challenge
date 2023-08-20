def positive_check(a,b,c):
    positive_sum = sum(num for num in [a,b,c] if num > 0)
    if positive_sum >= 2:
        return True
    else:
        return False    
print(positive_check(1,-2,4))    