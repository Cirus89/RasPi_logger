import datetime
import psutil

intrvl = 30 #in seconds

def write_temp(time, temp, fan, cpu):
        with open("/home/pi/Documents/Project_Temp_Logger/cpu_temp_v2.csv", "a") as log:
            log.write(f'\nDateTime,{time},cpu temperature (deg C),{temp},fan speed (rpm),{fan},cpu load over {intrvl} sec (%), {cpu}')

while True:
    temp = str(psutil.sensors_temperatures()['cpu_thermal'][0])[26:-27]
    fan = str(psutil.sensors_fans()['gpio_fan'][0])[-2:-1]
    cpu = str(psutil.cpu_percent(interval=intrvl))
    time = '{:%Y-%m-%d %H:%M:%S %Z}'.format(datetime.datetime.now())
    write_temp(time, temp, fan, cpu)
    #print(f'\nDateTime,{time},cpu temperature (deg C),{temp},fan speed (rpm),{fan},cpu load over {intrvl} sec (%), {cpu}')