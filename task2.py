#  напиать функцию, которая считает либо площадь либо объём шара, которая может
#  принять параметр is3d (False по умолчанию) и fix (int, 2 по умолчанию)

from task2_ans import square

print(square(3))
print(square(3, fix=5))
print(square(3, is3d=True, fix=3))

