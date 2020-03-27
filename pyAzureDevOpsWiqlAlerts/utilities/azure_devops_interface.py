#! python3

class azure_devops_interface:

    def __init__(self):
        print('azure_devops_interface constructor called')

    def passthrough_method(self, name):
        print(f'passthrough_method called. hi, {name}!')