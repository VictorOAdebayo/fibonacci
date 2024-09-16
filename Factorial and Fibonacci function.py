def generate_num(num):
    array = []
    for i in range(num + 1):
        array.append(i)
    return array

def fibonacci(lst):
    addition = 0
    fib = []
    for j in range(0, len(lst) - 1):
        addition = lst[j] + lst[j + 1]
        lst[j], lst[j + 1] = lst[j + 1], addition
        fib.append(addition)
    return fib
print(fibonacci(generate_num(100)))
        
    
