import serial
import matplotlib.pyplot as plt
# import keyboard

ser = serial.Serial(  # 下面这些参数根据情况修改
    port='COM13',
    baudrate=115200,
    parity=serial.PARITY_ODD,
    stopbits=serial.STOPBITS_TWO,
    bytesize=serial.SEVENBITS
)

data = ''


# 处理列表元素——字符串变成数字
def listcope(a, loc1: int, loc2: int):
    b = a.split(", ")
    del b[loc1]
    del b[loc2]
    b = list(map(float, b))
    return b



# 视重转化
def gravity_cal(m, acceleration_z):
    _force = []
    for i, a in enumerate(acceleration_z):
        F = m * a * -1
        _force.append(F)
    
    return _force



# 绘制图表
def plotpaint(x_axis, y_axis):
    fig, ax = plt.subplots()
    ax.plot(x_axis, y_axis, c='black')
    plt.title('ApparentMass-Time graph', fontsize=20)
    plt.tick_params(axis='both',which='major',labelsize=14)
    plt.xlabel('Time/s', fontsize=16)
    plt.ylabel('ApparentMass/kg', fontsize=16)

    plt.show()



while True:
    data = ser.readline()
    data = str(data)
    datalist = data.split(':')

    if datalist[0] == "b'timelist":
        timelist = datalist.pop(1)
    elif datalist[0] == "b'acc_record":
        acc_record = datalist.pop(1)
        break

    print(data)

ser.close()
# print(acc_record)
# print(timelist)


acc_record = listcope(acc_record, 0, -1)
timelist = listcope(timelist, 0, -1)

gravity_test = gravity_cal(60, acc_record)

plotpaint(timelist, gravity_test)