#this program should be a basic timer
import time
sec = 0
min = 0
hrs = 0
while True:
    while sec <= 60:
        print hrs , ":" , min, ":" , sec
        sec += 1
        time.sleep(1)
 sec == 0
 min += 1
 if min == 60:
     min == 0
     hrs += 1