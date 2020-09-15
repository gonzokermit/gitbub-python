import math

radius = float(input('Radius of the Circle: '))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print(f'The Area with Radius {radius} is {area}')
print(f'The Circumference with {radius} is {circumference}')

#Mit Aufrunden
print('The Area with Radius' ,radius, 'is' ,round(area,2))
print('The Circumference with' ,radius, 'is' ,round(circumference,2))