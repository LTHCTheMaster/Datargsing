from typing import Union
from time import sleep

class datargsing_Error:
    def __init__(self, error_content: str, debug: bool = False):
        print('\n'+error_content+'\n')
        sleep(2)
        if not debug:
            exit()

class datargsing_Complete:
    def __init__(self, debug: bool = False):
        if debug:
            print('\n Complete \n')
            sleep(1)

class JSON_Manage:
    def __init__(self):
        pass
    
    def get_from_file(self, path: str, debug: bool = False) -> Union[dict, datargsing_Error]:
        if path.endswith('.json'):
            try:
                return eval(open(file=path, mode='r').read().replace('true', 'True').replace('false', 'False'))
            except:
                return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a JSON file (extension check)', debug=debug)
    
    def set_to_file(self, path: str, content: dict, debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        if path.endswith('.json'):
            try:
                cur = open(file=path, mode='w')
                cur.write(str(content).replace('True', 'true').replace('False', 'false').replace("'", '"'))
                cur.close()
                return datargsing_Complete(debug=debug)
            except:
                try:
                    cur = open(file=path, mode='xw')
                    cur.write(str(content).replace('True', 'true').replace('False', 'false').replace("'", '"'))
                    cur.close()
                    return datargsing_Complete(debug=debug)
                except:
                    return datargsing_Error(error_content='Can\'t create the file', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a JSON file (extension check)', debug=debug)
    
    def get_from_file_like_json(self, path: str, debug: bool = False) -> Union[dict, datargsing_Error]:
        try:
            temp = eval(open(file=path, mode='r').read().replace('true', 'True').replace('false', 'False'))
            if type(temp) == dict:
                return temp
            else:
                return datargsing_Error(error_content='The file isn\'t a JSON like file', debug=debug)
        except:
            return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
    
    def set_to_file_like_json(self, path: str, content: dict, debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        try:
            cur = open(file=path, mode='w')
            cur.write(str(content).replace('True', 'true').replace('False', 'false').replace("'", '"'))
            cur.close()
            return datargsing_Complete(debug=debug)
        except:
            try:
                cur = open(file=path, mode='xw')
                cur.write(str(content).replace('True', 'true').replace('False', 'false').replace("'", '"'))
                cur.close()
                return datargsing_Complete(debug=debug)
            except:
                return datargsing_Error(error_content='Can\'t create the file', debug=debug)
