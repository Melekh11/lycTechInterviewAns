from task2_ans import square  # ваша готовая функция

#  напиать функцию, которая считает либо площадь либо объём шара
#  функция может принять параметр is3d (False по умолчанию) и fix (int, 2 по умолчанию)

print(square(3))  # 28.27
print(square(3, fix=5))  # 28.27433
print(square(3, is3d=True, fix=3))  # 113.097

