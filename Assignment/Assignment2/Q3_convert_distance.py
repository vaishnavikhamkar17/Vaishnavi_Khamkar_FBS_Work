## Convert distance given in feet and inches into meter and centimeter.

feet = int(input('Enter the distant in feet:'))
inches = int(input('Enter the distant in inches:'))

total_inches = (feet * 12) + inches
meters = total_inches * 0.0254
centimeters = meters * 100

print(f'Distance in meters:{meters}')
print(f'Distance in centimeters:{centimeters}')


