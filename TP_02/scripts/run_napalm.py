
from traceback import print_t
import run_napalm
import json

def get_inventory():
    pass


def get_json_data_from_file(file):
    pass


def question_41(device):
    pass


def question_42(device):
    pass


def question_45(device):
    pass

def question_46():
    pass


def question_47():
    pass

def question_49():
    pass

if __name__ == "__main__":
    r01 = {
    'host': '172.16.100.62',
    'username': 'cisco',
    'password': 'cisco'
    } 
    driver = get_network_driver('ios')
    device = driver(**r01)
    device.open()
    pass
        