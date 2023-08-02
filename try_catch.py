def divide_by(a, b):
    return a / b

try:
    ans = divide_by(40, 0)
except ZeroDivisionError:
    print("Zero division")
except Exception as e:
    print(e)