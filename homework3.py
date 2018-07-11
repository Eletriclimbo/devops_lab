import psutil
import time
import yaml
import json


def cpu_load():
    return psutil.cpu_percent(0.1, True)


def memory():
    return psutil.disk_usage('/home').free >> 20


def v_mem():
    return psutil.virtual_memory().free >> 20


def io_check():
    return psutil.disk_io_counters().write_count


def network():
    return psutil.net_io_counters().packets_sent


def out():
    print(" CPU: ", cpu_load(), " Free memory: ", memory(),
          " Mb ", " Free VM: ", v_mem(),
          " Mb ", " IO (write_count): ", io_check(),
          " Network (packets sent): ", network())


with open("conf.yaml", 'r') as stream:
    my_conf = yaml.load(stream)
interval = my_conf['interval']
output = my_conf['output']

if output == 'txt':
    for j in range(3):
        k = j+1
        print("SNAPSHOT ", k, ": ", " TIME :", time.strftime("%H:%M:%S"), " CPU: ",
              cpu_load(), " Free memory: ", memory(), "Mb", " Free VM: ", v_mem(),
              "Mb", " IO (write_count): ",
              io_check(), " Network (packets sent): ",
              network(), file=open("output.txt", "a"))
        print("SNAPSHOT ", k, ": ", " TIME :", time.strftime("%H:%M:%S"), " CPU: ",
              cpu_load(), " Free memory: ", memory(), "Mb", " Free VM: ", v_mem(),
              "Mb", " IO (write_count): ",
              io_check(), " Network (packets sent): ", network())
        time.sleep(1 * interval)
aa = list()
if output == 'json':
    for j in range(3):
        k = j + 1
        json_d = {
            'SNAPSHOT ': k,
            'TIME': time.strftime("%H:%M:%S"),
            'CPU': cpu_load(),
            'Free memory': memory(),
            'Free VM': v_mem(),
            'IO (write_count)': io_check(),
            'Network (packets sent)': network(),
        }
        print("YEES")
        aa.append(json_d)
        print(aa)
        time.sleep(1 * interval)

with open('json_data.json', 'a+') as sec:
    json.dump(aa, sec)
