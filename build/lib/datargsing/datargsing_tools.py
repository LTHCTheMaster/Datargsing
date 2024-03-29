# -*- coding: utf-8 -*-

"""
Datargsing Tools Module
"""

class datargsing_Failure:
	"""
	Datargsing Failure Class
	"""
	def __init__(self):
		"""
		Datargsing Failure Class
		"""
		pass

class Datargsing_Engine:
	"""
	Datargsing Engine Class
	"""
	def __init__(self):
		"""
		Datargsing Engine Class
		"""
		pass

	def locate(self, main: str, wanted: str) -> int | datargsing_Failure:
		"""
		Return the index of the first {wanted} in {main}
		"""
		assert type(main) == str, "{ main } must be a str"
		assert type(wanted) == str, "{ wanted } must be a str"
		if wanted in main:
			return main.find(wanted)
		else:
			return datargsing_Failure()

	def locate_all(self, main: str, wanted: str) -> int | list[int] | datargsing_Failure:
		"""
		Return all indexes of {wanted} in {main}
		"""
		assert type(main) == str, "{ main } must be a str"
		assert type(wanted) == str, "{ wanted } must be a str"
		current = main
		upd = 0
		out: list[int] = []
		finished = False
		while not finished:
			temp = self.locate(main=current, wanted=wanted)
			if type(temp) == datargsing_Failure:
				finished = True
			else:
				out.append(temp+upd)
				current = current[temp+1::]
				upd = len(main) - len(current)
		if out == []:
			return datargsing_Failure()
		if len(out) == 1:
			return out[0]
		return out
