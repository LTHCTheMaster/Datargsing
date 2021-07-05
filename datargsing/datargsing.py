from typing import Union

class datargsing_Error:
    def __init__(self, error_content: str, debug: bool = False):
        print('\n'+error_content+'\n')
        if not debug:
            exit()

class datargsing_Complete:
    def __init__(self, debug: bool = False):
        if debug:
            print('\n Complete \n')

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

class CSV_Manage:
    def __init__(self):
        pass

    def get_from_file(self, path: str, separator: str = ',', debug: bool = False) -> Union[tuple, datargsing_Error]:
        """
        return tuple (descriptors/entries, values) if completion
        """
        if path.endswith('.csv'):
            try:
                file = open(file=path, mode='r')
                descriptors = file.readline().rstrip().split(separator)
                values = [i.rstrip().split(separator) for i in file.readlines()]
                content = (descriptors, values)
                return content
            except:
                return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a CSV file (extension check)', debug=debug)
    
    def set_to_file(self, path: str, content: tuple, separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        if path.endswith('.csv'):
            try:
                descriptors = separator.join(content[0])
                cur = open(file=path, mode='w')
                cur.write(descriptors)
                for i in content[1]:
                    values_line = '\n' + separator.join(i)
                    cur.write(values_line)
                cur.close()
                return datargsing_Complete(debug=debug)
            except:
                try:
                    descriptors = separator.join(content[0])
                    cur = open(file=path, mode='w')
                    cur.write(descriptors)
                    for i in content[1]:
                        values_line = '\n' + separator.join(i)
                        cur.write(values_line)
                    cur.close()
                    return datargsing_Complete(debug=debug)
                except:
                    return datargsing_Error(error_content='Can\'t create the file', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a CSV file (extension check)', debug=debug)
        
    def get_from_file_like_csv(self, path: str, separator: str = ',', debug: bool = False) -> Union[tuple, datargsing_Error]:
        """
        return tuple (descriptors/entries, values) if completion
        """
        try:
            file = open(file=path, mode='r')
            descriptors = file.readline().rstrip().split(separator)
            values = [i.rstrip().split(separator) for i in file.readlines()]
            content = (descriptors, values)
            return content
        except:
            return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
    
    def set_to_file_like_csv(self, path: str, content: tuple, separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        try:
            descriptors = separator.join(content[0])
            cur = open(file=path, mode='w')
            cur.write(descriptors)
            for i in content[1]:
                values_line = '\n' + separator.join(i)
                cur.write(values_line)
            cur.close()
            return datargsing_Complete(debug=debug)
        except:
            try:
                descriptors = separator.join(content[0])
                cur = open(file=path, mode='w')
                cur.write(descriptors)
                for i in content[1]:
                    values_line = '\n' + separator.join(i)
                    cur.write(values_line)
                cur.close()
                return datargsing_Complete(debug=debug)
            except:
                return datargsing_Error(error_content='Can\'t create the file', debug=debug)

class CSV_JSON_Convert:
    def __init__(self):
        self.jm = JSON_Manage()
        self.cm = CSV_Manage()

    def csv_json_get_set(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        csv_content = self.cm.get_from_file(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            json_r = self.jm.set_to_file(path=path_json, content=json_format, debug=debug)
            if type(json_r) == datargsing_Complete:
                return datargsing_Complete(debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def csv_json_get(self, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[dict, datargsing_Error]:
        csv_content = self.cm.get_from_file(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            return json_format
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_csv_get_set(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        json_content = self.jm.get_from_file(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                csv_r = self.cm.set_to_file(path=path_csv, content=(descriptors, values), separator=csv_separator, debug=debug)
                if type(csv_r) == datargsing_Complete:
                    return datargsing_Complete(debug=debug)
                else:
                    return datargsing_Error('Cannot read correct parameters', debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_csv_get(self, path_json: str,  debug: bool = False) -> Union[tuple, datargsing_Error]:
        json_content = self.jm.get_from_file(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                return (descriptors, values)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def csv_like_json_get_set(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        csv_content = self.cm.get_from_file_like_csv(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            json_r = self.jm.set_to_file(path=path_json, content=json_format, debug=debug)
            if type(json_r) == datargsing_Complete:
                return datargsing_Complete(debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def csv_json_like_get_set(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        csv_content = self.cm.get_from_file(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            json_r = self.jm.set_to_file_like_json(path=path_json, content=json_format, debug=debug)
            if type(json_r) == datargsing_Complete:
                return datargsing_Complete(debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def csv_like_json_like_get_set(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        csv_content = self.cm.get_from_file_like_csv(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            json_r = self.jm.set_to_file_like_json(path=path_json, content=json_format, debug=debug)
            if type(json_r) == datargsing_Complete:
                return datargsing_Complete(debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def csv_like_json_get(self, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[dict, datargsing_Error]:
        csv_content = self.cm.get_from_file_like_csv(path=path_csv, separator=csv_separator, debug=debug)
        if type(csv_content) == tuple:
            json_format = {}
            for i in range(len(csv_content[0])):
                json_format[csv_content[0][i]] = []
                for j in csv_content[1]:
                    json_format[csv_content[0][i]].append(j[i])
            return json_format
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_like_csv_get_set(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        json_content = self.jm.get_from_file_like_json(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                csv_r = self.cm.set_to_file(path=path_csv, content=(descriptors, values), separator=csv_separator, debug=debug)
                if type(csv_r) == datargsing_Complete:
                    return datargsing_Complete(debug=debug)
                else:
                    return datargsing_Error('Cannot read correct parameters', debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_csv_like_get_set(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        json_content = self.jm.get_from_file(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                csv_r = self.cm.set_to_file_like_csv(path=path_csv, content=(descriptors, values), separator=csv_separator, debug=debug)
                if type(csv_r) == datargsing_Complete:
                    return datargsing_Complete(debug=debug)
                else:
                    return datargsing_Error('Cannot read correct parameters', debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_like_csv_like_get_set(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        json_content = self.jm.get_from_file_like_json(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                csv_r = self.cm.set_to_file_like_csv(path=path_csv, content=(descriptors, values), separator=csv_separator, debug=debug)
                if type(csv_r) == datargsing_Complete:
                    return datargsing_Complete(debug=debug)
                else:
                    return datargsing_Error('Cannot read correct parameters', debug=debug)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
    
    def json_like_csv_get(self, path_json: str,  debug: bool = False) -> Union[tuple, datargsing_Error]:
        json_content = self.jm.get_from_file_like_json(path=path_json, debug=debug)
        if type(json_content) == dict:
            descriptors = []
            associated = []
            good = 0
            num = 0
            for i in json_content:
                num += 1
                if type(json_content[i]) == list:
                    num2 = len(json_content[i])
                    good2 = 0
                    for j in json_content[i]:
                        if type(j) == str:
                            good2 += 1
                    if num2 == good2:
                        good += 1
                        associated.append(json_content[i])
                        descriptors.append(i)
            if good == num:
                values = []
                for i in range(len(associated[0])):
                    values.append([])
                    for j in associated:
                        values[i].append(j[i])
                return (descriptors, values)
            else:
                return datargsing_Error('Cannot read correct parameters', debug=debug)
        else:
            return datargsing_Error('Cannot read correct parameters', debug=debug)
