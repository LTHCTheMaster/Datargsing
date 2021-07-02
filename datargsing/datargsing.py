from typing import Union
from time import sleep

class datargsing_Error:
    def __init__(self, error_content: str, debug: bool = False):
        print('\n'+error_content+'\n')
        sleep(2)
        if not debug:
            exit()

class JSON_Manage:
    def __init__(self):
        pass
    
    def get_from_file(self, path: str, debug: bool = False) -> Union[dict, datargsing_Error]:
        if path.endswith('.json'):
            try:
                temp = eval(open(file=path, mode='r').read().replace('true', 'True').replace('false', 'False'))
                return temp
            except:
                return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a JSON file (extension check)', debug=debug)
