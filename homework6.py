import os
import json
import yaml


def my_version():
    tmp = os.popen('python -V').read().strip()
    return tmp


def virtual_env():
    tmp = os.popen('pyenv versions').read().strip().split("\n")
    result = [i for i in tmp if i.startswith('*')]
    k = ''.join(result)
    return k


def ex_location():
    tmp = os.popen('which python').read().strip()
    return tmp


def pip_loc():
    tmp = os.popen('which pip').read().strip()
    return tmp


def python_path():
    tmp = os.popen('echo $PYTHONPATH').read().strip()
    return tmp


def inst_pack():
    tmp = os.popen('pip list').read().strip()
    return tmp


def site_pack_location():
    tmp = os.popen('python -m site').read().strip()
    return tmp


json_d = {
    'Python version': my_version(),
    'Virtual environment': virtual_env(),
    'Executable location': ex_location(),
    'Python Path': python_path(),
    'Install packages': inst_pack().split('\n'),
    'Site-packages location': site_pack_location().split('\n'),
    'Pip location': pip_loc(),
}

with open('json_data_6.json', 'a+') as sec:
    json.dump(json_d, sec)


with open("yaml_data_6.yaml", 'a') as yml_file:
    yaml.dump(json_d, yml_file, explicit_start=True, default_flow_style=False)
