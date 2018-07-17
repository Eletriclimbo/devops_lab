import json
import psutil
import time
import yaml


class Geu(object):
    @staticmethod
    def cpu_load():
        return psutil.cpu_percent(0.1, True)

    @staticmethod
    def memory():
        return psutil.disk_usage('/home').free >> 20

    @staticmethod
    def v_mem():
        return psutil.virtual_memory().free >> 20

    @staticmethod
    def io_check():
        return psutil.disk_io_counters().write_count

    @staticmethod
    def network():
        return psutil.net_io_counters().packets_sent


with open("conf.yaml", 'r') as stream:
    my_conf = yaml.load(stream)
interval = my_conf['interval']
output = my_conf['output']

if output == 'txt':
    for j in range(3):
        k = j + 1
        print("SNAPSHOT ", k, ": ", " TIME :",
              time.strftime("%H:%M:%S"), " CPU: ",
              Geu.cpu_load(), " Free memory: ",
              Geu.memory(), "Mb", " Free VM: ", Geu.v_mem(),
              "Mb", " IO (write_count): ",
              Geu.io_check(), " Network (packets sent): ",
              Geu.network(), file=open("output.txt", "a"))
        print("SNAPSHOT ", k, ": ", " TIME :",
              time.strftime("%H:%M:%S"), " CPU: ",
              Geu.cpu_load(), " Free memory: ",
              Geu.memory(), "Mb", " Free VM: ", Geu.v_mem(),
              "Mb", " IO (write_count): ",
              Geu.io_check(), " Network (packets sent): ", Geu.network())
        time.sleep(1 * interval)
aa = []
if output == 'json':
    for j in range(3):
        k = j + 1
        json_d = {
            'SNAPSHOT ': k,
            'TIME': time.strftime("%H:%M:%S"),
            'CPU': Geu.cpu_load(),
            'Free memory': Geu.memory(),
            'Free VM': Geu.v_mem(),
            'IO (write_count)': Geu.io_check(),
            'Network (packets sent)': Geu.network(),
        }
        aa.append(json_d)
        print(aa)
        time.sleep(1 * interval)

with open('json_data.json', 'a+') as sec:
    json.dump(aa, sec)
