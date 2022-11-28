import math
from datetime import datetime
current_date_and_time = datetime.now()
print(f"{current_date_and_time:%y-%m-%d}")

#Gathers the dimensions of the tire from the User.
width = float(input('Enter the width of the tire in mm: '))
ratio = float(input('Enter the aspect ratio of the tire: '))
diameter = float(input('Enter the diameter of the wheel in inches: '))

#Splitting up the formula to make it easier to write the math (Personally at least)
radical = (2540 * diameter + width * ratio)
radical_2 = (math.pi * width**2 * ratio)
volume = ((radical * radical_2) / 10000000000)

#Rounds the volume to 2 decimals.
volume = round(volume, 2)
print(f'The volume of the tire is {volume} liters.')

#Records the inputs and the output to the volumes.txt file.
with open('volumes.txt', 'at') as volumes_file:print(f'{current_date_and_time}, {width}, {ratio}, {diameter}, {volume}', file=volumes_file)