# -*- coding: utf-8 -*-

"""
Datargsing Main Module
"""

from datargsing.datargsing_core import datargsing_Complete, datargsing_Error, JSON_Manage as jmC, CSV_Manage as cmC, CSV_JSON_Convert as cjcC
from datargsing.datargsing_tools import datargsing_Failure, Datargsing_Engine
from random import randint
from datargsing.datargsing_version import __version__

class CSV_JSON_Manager:
	"""
	Datargsing CSV And JSON Managing and Converting Class
	"""
	def __init__(self):
		"""
		Datargsing CSV And JSON Managing and Converting Class
		"""
		self.JM = jmC()
		self.CM = cmC()
		self.CJC = cjcC()

	def get_from_json(self, path: str, debug: bool = False) -> dict | datargsing_Error:
		"""
		Get From A JSON (Formated/Like or .json) File:
		  -> path : (str) the path of the json (formated/like or .json) file
		  -> debug : (bool) [False] a debug state for Error Class
		=> Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
		"""
		assert type(path) == str, "{ path } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path.endswith('.json'):
			return self.JM.get_from_file(path=path,debug=debug)
		else:
			return self.JM.get_from_file_like_json(path=path,debug=debug)

	def get_from_csv(self, path: str, separator: str = ',', debug: bool = False) -> tuple | datargsing_Error:
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
		assert type(path) == str, "{ path } must be a str"
		assert type(separator) == str, "{ separator } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path.endswith('.csv'):
			return self.CM.get_from_file(path=path,separator=separator,debug=debug)
		else:
			return self.CM.get_from_file_like_csv(path=path,separator=separator,debug=debug)

	def set_to_json(self, path: str, content: dict, debug: bool = False) -> datargsing_Complete | datargsing_Error:
		"""
		Set To A JSON (Formated/Like or .json) File:
		  -> path : (str) the path of the json (formated/like or .json) output file
		  -> debug : (str) [False] a debug state for Error Class and Completion Class
		=> Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
		"""
		assert type(path) == str, "{ path } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path.endswith('.json'):
			return self.JM.set_to_file(path=path,content=content,debug=debug)
		else:
			return self.JM.set_to_file_like_json(path=path,content=content,debug=debug)

	def set_to_csv(self, path: str, content: tuple, separator: str = ',', debug: bool = False) -> datargsing_Complete | datargsing_Error:
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
		assert type(path) == str, "{ path } must be a str"
		assert type(separator) == str, "{ separator } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path.endswith('.csv'):
			return self.CM.set_to_file(path=path,content=content,separator=separator,debug=debug)
		else:
			return self.CM.set_to_file_like_csv(path=path,content=content,separator=separator,debug=debug)

	def write_json_from_csv(self, path_csv: str, path_json: str, csv_separator: str = ',', debug: bool = False) -> datargsing_Complete | datargsing_Error:
		"""
		Write The JSON Formated CSV Content From A CSV (Formated/Like or .csv) File To A JSON (Formated/Like or .json) File:
		  -> path_csv : (str) the path of the csv (formated/like or .csv) file
		  -> path_json : (str) the path of the json (formated/like or .json) output file
		  -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) file
		  -> debug : (str) [False] a debug state for Error Class and Completion Class
		=> Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
		"""
		assert type(path_csv) == str, "{ path_csv } must be a str"
		assert type(path_json) == str, "{ path_json } must be a str"
		assert type(csv_separator) == str, "{ csv_separator } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path_csv.endswith('.csv'):
			if path_json.endswith('.json'):
				return self.CJC.csv_json_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
			else:
				return self.CJC.csv_json_like_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
		else:
			if path_json.endswith('.json'):
				return self.CJC.csv_like_json_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)
			else:
				return self.CJC.csv_like_json_like_get_set(path_csv=path_csv,path_json=path_json,csv_separator=csv_separator,debug=debug)

	def write_csv_from_json(self, path_json: str, path_csv: str, csv_separator: str = ',', debug: bool = False) -> datargsing_Complete | datargsing_Error:
		"""
		Write The CSV Formated JSON Content From A JSON (Formated/Like or .json) File To A CSV (Formated/Like or .csv) File:
		  -> path_json : (str) the path of the json (formated/like or .json) file
		  -> path_csv : (str) the path of the csv (formated/like or .csv) output file
		  -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) output file
		  -> debug : (str) [False] a debug state for Error Class and Completion Class
		=> Return a (datargsing_Complete) object or a (datargsing_Error) object {For more details: view (datargsing_Complete) info and/or (datargsing_Error) info}
		"""
		assert type(path_csv) == str, "{ path_csv } must be a str"
		assert type(path_json) == str, "{ path_json } must be a str"
		assert type(csv_separator) == str, "{ csv_separator } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path_json.endswith('.json'):
			if path_csv.endswith('.csv'):
				return self.CJC.json_csv_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
			else:
				return self.CJC.json_csv_like_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
		else:
			if path_csv.endswith('.csv'):
				return self.CJC.json_like_csv_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)
			else:
				return self.CJC.json_like_csv_like_get_set(path_json=path_json,path_csv=path_csv,csv_separator=csv_separator,debug=debug)

	def get_json_from_csv(self, path_csv: str, csv_separator: str = ',', debug: bool = False) -> dict | datargsing_Error:
		"""
		Get The JSON Formated CSV Content From A CSV (Formated/like or .csv) File:
		  -> path_csv : (str) the path of the csv (formated/like or .csv) file
		  -> csv_separator : (str) [','] the separator in the csv (formated/like or .csv) file
		  -> debug : (str) [False] a debug state for Error Class
		=> Return a (dict) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}
		"""
		assert type(path_csv) == str, "{ path_csv } must be a str"
		assert type(csv_separator) == str, "{ csv_separator } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path_csv.endswith('.csv'):
			return self.CJC.csv_json_get(path_csv=path_csv,csv_separator=csv_separator,debug=debug)
		else:
			return self.CJC.csv_like_json_get(path_csv=path_csv,csv_separator=csv_separator,debug=debug)

	def get_csv_from_json(self, path_json: str, debug: bool = False) -> tuple | datargsing_Error:
		"""
		Get The CSV Formated JSON Content From A JSON (Formated/Like or .json) File:
		  -> path_json : (str) the path of the json (formated/like or .json) file
		  -> debug : (str) [False] a debug state for Error Class
		=> Return a (tuple) object or a (datargsing_Error) object {For more details: view (datargsing_Error) info}

		=-=-> output tuple format:

		  -> Index 0 : a list with descriptors/entries
		  -> Index 1 : a list of (sub-)list, each (sub-)list is a line under descriptors/entries
		"""
		assert type(path_json) == str, "{ path_json } must be a str"
		assert type(debug) == bool, "{ debug } must be a bool"
		if path_json.endswith('.json'):
			return self.CJC.json_csv_get(path_json=path_json,debug=debug)
		else:
			return self.CJC.json_like_csv_get(path_json=path_json,debug=debug)

class Tools:
	"""
	Datargsing Tools Class
	"""
	def __init__(self):
		"""
		Datargsing Tools Class
		"""
		self.de = Datargsing_Engine()

	def location(self, main: str, wanted: str) -> int | list[int] | datargsing_Failure:
		"""
		Return the single index (or all indexes) of {wanted} in {main}
		"""
		assert type(main) == str, "{ main } must be a str"
		assert type(wanted) == str, "{ wanted } must be a str"
		temp = self.de.locate_all(main=main, wanted=wanted)
		if type(temp) == datargsing_Failure:
			return datargsing_Failure()
		else:
			return temp

	def count(self, main: str, wanted: str) -> int:
		"""
		Return the number of {wanted} in {main}
		"""
		assert type(main) == str, "{ main } must be a str"
		assert type(wanted) == str, "{ wanted } must be a str"
		temp = self.location(main=main,wanted=wanted)
		if type(temp) == datargsing_Failure:
			return 0
		elif type(temp) == int:
			return 1
		else:
			return len(temp)

	def get_one_random_location(self, main: str, wanted: str) -> int | datargsing_Failure:
		"""
		Return one random location of {wanted} in {main}
		"""
		assert type(main) == str, "{ main } must be a str"
		assert type(wanted) == str, "{ wanted } must be a str"
		temp = self.location(main=main,wanted=wanted)
		if type(temp) == datargsing_Failure:
			return datargsing_Failure()
		elif type(temp) == int:
			return temp
		else:
			return temp[randint(0,len(temp)-1)]
