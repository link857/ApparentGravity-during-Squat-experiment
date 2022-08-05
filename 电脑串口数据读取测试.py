import serial
import keyboard

ser = serial.Serial(  # 下面这些参数根据情况修改
    port='COM13',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

data = ''

while True:
    data = ser.readline()

    if keyboard.is_pressed('y') or data == b'Type "help()" for more information.\r\n':
        break

    data = str(data)
    datalist = data.split(':')

    if datalist[0] == "b'timelist":
        timelist = datalist.pop(1)
    elif datalist[0] == "b'acc_record":
        acc_record = datalist.pop(1)
        break

    print(data)

ser.close()
print(acc_record)
print(timelist)