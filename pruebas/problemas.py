def orden_arreglo(numbers):
    # Sorting list of Integers in ascending
    numbers.sort()
    print(numbers)
    return numbers

def personas_mayores(info):
    total = 0
    for p in info:
        if p["edad"] >= 18:
            total += 1
    print(total)
    return total

'''
orden_arreglo(numbers = [1, 3, 4, 2, 5])
personas_mayores(
    info = [
    {"nombre":"Amairani", "edad":21},
    {"nombre":"Petra", "edad":22},
    {"nombre":"Mario", "edad":17}, 
    {"nombre":"Jaime", "edad":24},
    {"nombre":"Martina", "edad":15},
    {"nombre":"Martina", "edad":18}
    ])
'''