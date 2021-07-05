from datargsing.datargsing_core import datargsing_Complete, datargsing_Error, JSON_Manage as jmC, CSV_Manage as cmC, CSV_JSON_Convert as cjcC
from typing import Union

class CSV_JSON_Manager:
    """
    Datargsing CSV And JSON Managing and Converting Class
    """
    def __init__(self):
        """
        Datargsing CSV And JSON Managing and Converting Class
        """
        self.jm = jmC()
        self.cm = cmC()
        self.cjc = cjcC()
    
    def get_from_json(self, path: str, debug: bool = False) -> Union[dict, datargsing_Error]:
        """
        Get From A JSON (Formated/Like or .json) File:
          -> path : (str) the path of the json (formated/like or .json) file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
        if path.endswith('.json'):
            return self.jm.get_from_file(path=path,debug=debug)
        else:
            return self.jm.get_from_file_like_json(path=path,debug=debug)
    
    def get_from_csv(self, path: str, separator: str = ',', debug: bool = False) -> Union[tuple, datargsing_Error]:
        """
        Get From A CSV (Formated/Like or .csv) File:
          -> path : (str) the path of the csv (formated/like or .csv) file
          -> separator : (str) [','] the separator in the csv (formated/like or .csv) file
          -> debug : (bool) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}

        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
        if path.endswith('.csv'):
            return self.cm.get_from_file(path=path,separator=separator,debug=debug)
        else:
            return self.cm.get_from_file_like_csv(path=path,separator=separator,debug=debug)
    
    def set_to_json(self, path: str, content: dict, debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Set To A JSON (Formated/Like or .json) File:
          -> path : (str) the path of the json (formated/like or .json) output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
        if path.endswith('.json'):
            return self.jm.set_to_file(path=path,content=content,debug=debug)
        else:
            return self.jm.set_to_file_like_json(path=path,content=content,debug=debug)
    
    def set_to_csv(self, path: str, content: tuple, separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Set To A CSV (Formated/Like or .csv) File:
          -> path : (str) the path of the csv (formated/like or .csv) output file
          -> content : (tuple) the content of the csv (formated/like or .csv) output file
          -> separator : (str) [','] the separator in the csv (formated/like or .csv) output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}

        =-=-> content tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
        if path.endswith('.csv'):
            return self.cm.set_to_file(path=path,content=content,separator=separator,debug=debug)
        else:
            return self.cm.set_to_file_like_csv(path=path,content=content,separator=separator,debug=debug)
    
    def write_json_from_csv(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Write The JSON Formated CSV Content From A CSV (Formated/Like or .csv) File To A JSON (Formated/Like or .json) File:
          -> path_csv : (str) the path of the csv (formated/like or .csv) file
          -> path_json : (str) the path of the json (formated/like or .json) output file
          -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
        if path_csv.endswith('.csv'):
            if path_json.endswith('.json'):
                return self.cjc.csv_json_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
            else:
                return self.cjc.csv_json_like_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
        else:
            if path_json.endswith('.json'):
                return self.cjc.csv_like_json_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
            else:
                return self.cjc.csv_like_json_like_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
    
    def write_csv_from_json(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[datargsing_Complete, datargsing_Error]:
        """
        Write The CSV Formated JSON Content From A JSON (Formated/Like or .json) File To A CSV (Formated/Like or .csv) File:
          -> path_json : (str) the path of the json (formated/like or .json) file
          -> path_csv : (str) the path of the csv (formated/like or .csv) output file
          -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) output file
          -> debug : (str) [False] a debug state for Error Class and Completion Class
        => Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
        """
        if path_json.endswith('.json'):
            if path_csv.endswith('.csv'):
                return self.cjc.json_csv_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
            else:
                return self.cjc.json_csv_like_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
        else:
            if path_csv.endswith('.csv'):
                return self.cjc.json_like_csv_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
            else:
                return self.cjc.json_like_csv_like_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
    
    def get_json_from_csv(self, path_csv: str, csv_separator: str = ',', debug: bool = False) -> Union[dict, datargsing_Error]:
        """
        Get The JSON Formated CSV Content From A CSV (Formated/like or .csv) File:
          -> path_csv : (str) the path of the csv (formated/like or .csv) file
          -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
        """
        if path_csv.endswith('.csv'):
            return self.cjc.csv_json_get(path_csv=path_csv,csv_separator=csv_separator,debug=debug)
        else:
            return self.cjc.csv_like_json_get(path_csv=path_csv,csv_separator=csv_separator,debug=debug)
    
    def get_csv_from_json(self, path_json: str, debug: bool = False) -> Union[tuple, datargsing_Error]:
        """
        Get The CSV Formated JSON Content From A JSON (Formated/Like or .json) File:
          -> path_json : (str) the path of the json (formated/like or .json) file
          -> debug : (str) [False] a debug state for Error Class
        => Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}

        =-=-> output tuple format:

          -> Index 0 : a list with descriptors/entries
          -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
        """
        if path_json.endswith('.json'):
            return self.cjc.json_csv_get(path_json=path_json,debug=debug)
        else:
            return self.cjc.json_like_csv_get(path_json=path_json,debug=debug)
