#mPythonType:0
from mpython import *
import time

timelist = []
acc_record = []
timecount = 0

accelerometer.set_range(accelerometer.RANGE_16G)

while True:
    timelist.append(timecount)
    
    z = accelerometer.get_z()
    print('z:'+str(z)+":")
    acc_record.append(z)
    
    time.sleep_ms(100)
    timecount += 0.1
    
    if button_a.was_pressed():
        break
    

print('结束测试')
print('timelist:'+str(timelist)+":")
print('acc_record:'+str(acc_record)+":")