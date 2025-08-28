## Convert time entered in hh, mm and sec into seconds.

h = int(input('Enter the hour:'))
m = int(input('Enter the minute:'))
s = int(input('Enter the second:'))

Hour_sec = h * 3600
Min_sec = m  * 60
Total_sec = Hour_sec + Min_sec + s

print(f'Total Seconds is:{Total_sec}')