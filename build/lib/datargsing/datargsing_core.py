from typing import Union

class datargsing_Error:
    """
    Datargsing Error Class:
      -> error_content : (str) error message
      -> debug : (bool) [False] if is False, stop the program
    """
    def __init__(self, error_content: str, debug: bool = False):
        """
        Datargsing Error Class:
          -> error_content : (str) error message
          -> debug : (bool) [False] if is False, stop the program
        """
        print('\n'+error_content+'\n')
        if not debug:
            exit()

class datargsing_Complete:
    """
    Datargsing Completion Class:
      -> debug : (bool) [False] if is True, print a simple message
    """
    def __init__(self, debug: bool = False):
        """
        Datargsing Completion Class:
          -> debug : (bool) [False] if is True, print a simple message
        """
        if debug:
            print('\n Complete \n')

class JSON_Manage:
    """
    Datargsing JSON Managing Class
    """
    def __init__(self):
        """
        Datargsing JSON Managing Class
        """
        pass
    
    def get_from_file(self, path: str, debug: bool = False) -> Union[dict, datargsing_Error]:
        """
        Get From A JSON File:
          -> path : (str) the path of the .json file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
        if path.endswith('.json'):
            try:
                return eval(open(file=path, mode='r').read().replace('true', 'True').replace('false', 'False'))
            except:
                return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
        else:
            return datargsing_Error(error_content='The file isn\'t a JSON file (extension check)', debug=debug)
    
    def set_to_file(self, path: str, content: dict, debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Set To A JSON File:
          -> path : (str) the path of the .json output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Get From A JSON Formated/Like File:
          -> path : (str) the path of the json formated/like file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
        try:
            temp = eval(open(file=path, mode='r').read().replace('true', 'True').replace('false', 'False'))
            if type(temp) == dict:
                return temp
            else:
                return datargsing_Error(error_content='The file isn\'t a JSON like file', debug=debug)
        except:
            return datargsing_Error(error_content='The file doesn\'t exist', debug=debug)
    
    def set_to_file_like_json(self, path: str, content: dict, debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Set To A JSON Formated/Like File:
          -> path : (str) the path of the json formated/like output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
    """
    Datargsing CSV Managing Class
    """
    def __init__(self):
        """
        Datargsing CSV Managing Class
        """
        pass

    def get_from_file(self, path: str, separator: str = ',', debug: bool = False) -> Union[tuple, datargsing_Error]:
        """
        Get From A CSV File:
          -> path : (str) the path of the .csv file
          -> separator : (str) [','] the separator in the .csv file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        
        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
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
        """
        Set To A CSV File:
          -> path : (str) the path of the .csv output file
          -> content : (tuple) the content of the .csv output file
          -> separator : (str) [','] the separator in the .csv output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        
        =-=-> content tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
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
        Get From A CSV Formated/Like File:
          -> path : (str) the path of the csv formated/like file
          -> separator : (str) [','] the separator in the csv formated/like file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        
        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
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
        """
        Set To A CSV Formated/Like File:
          -> path : (str) the path of the csv formated/like output file
          -> content : (tuple) the content of the csv formated/like output file
          -> separator : (str) [','] the separator in the csv formated/like output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        
        =-=-> content tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
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
    """
    Datargsing CSV from/to JSON Converting Class
    """
    def __init__(self):
        """
        Datargsing CSV from/to JSON Converting Class
        """
        self.jm = JSON_Manage()
        self.cm = CSV_Manage()

    def csv_json_get_set(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Write The JSON Formated CSV Content From A CSV File To A JSON File:
          -> path_csv : (str) the path of the .csv file
          -> path_json : (str) the path of the .json output file
          -> csv_separator : (str) [','] the separator in the .csv file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Get The JSON Formated CSV Content From A CSV File:
          -> path_csv : (str) the path of the .csv file
          -> csv_separator : (str) [','] the separator in the .csv file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
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
        """
        Write The CSV Formated JSON Content From A JSON File To A CSV File:
          -> path_json : (str) the path of the .json file
          -> path_csv : (str) the path of the .csv output file
          -> csv_separator : (str) [','] the separator in the .csv output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Get The CSV Formated JSON Content From A JSON File:
          -> path_json : (str) the path of the .json file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        
        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
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
        """
        Write The JSON Formated CSV Content From A CSV Formated/Like File To A JSON File:
          -> path_csv : (str) the path of the csv formated/like file
          -> path_json : (str) the path of the .json output file
          -> csv_separator : (str) [','] the separator in the csv formated/like file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Write The JSON Formated CSV Content From A CSV File To A JSON Formated/Like File:
          -> path_csv : (str) the path of the .csv file
          -> path_json : (str) the path of the json formated/like output file
          -> csv_separator : (str) [','] the separator in the .csv file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Write The JSON Formated CSV Content From A CSV Formated/Like File To A JSON Formated/Like File:
          -> path_csv : (str) the path of the csv formated/like file
          -> path_json : (str) the path of the json formated/like output file
          -> csv_separator : (str) [','] the separator in the csv formated/like file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Get The JSON Formated CSV Content From A CSV Formated/Like File:
          -> path_csv : (str) the path of the csv formated/like file
          -> csv_separator : (str) [','] the separator in the csv formated/like file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
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
        """
        Write The CSV Formated JSON Content From A JSON Formated/Like File To A CSV File:
          -> path_json : (str) the path of the json formated/like file
          -> path_csv : (str) the path of the .csv output file
          -> csv_separator : (str) [','] the separator in the .csv output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Write The CSV Formated JSON Content From A JSON File To A CSV Formated/Like File:
          -> path_json : (str) the path of the .json file
          -> path_csv : (str) the path of the csv formated/like output file
          -> csv_separator : (str) [','] the separator in the csv formated/like output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Write The CSV Formated JSON Content From A JSON Formated/Like File To A CSV Formated/Like File:
          -> path_json : (str) the path of the json formated/like file
          -> path_csv : (str) the path of the csv formated/like output file
          -> csv_separator : (str) [','] the separator in the csv formated/like output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
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
        """
        Get The CSV Formated JSON Content From A JSON Formated/Like File:
          -> path_json : (str) the path of the json formated/like file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        
        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
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
