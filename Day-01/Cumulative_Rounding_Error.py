def add_and_subtract(iterations):
    result = 1
    for i in range(iterations):
        result += 1 / 3
    for i in range(iterations):
        result -= 1 / 3
    return result


print("\nCumulative Rounding Error: ")
print(f"1 + 1/3 - 1/3 = {1 + 1/3 - 1/3}")
print(f"add_and_substract(100) : {add_and_subtract(100)}")
print(f"add_and_substract(1000) : {add_and_subtract(1000)}")
print(f"add_and_substract(10000) : {add_and_subtract(10000)}")
