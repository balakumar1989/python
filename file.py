class charerror(Exception):
	def _init_(self):
		self.value="name greaterthan 20 characters"
	def _str_(self):
		return(self.value)
class ageerror(Exception):
	def _init_(self):
		self.value="age out of bounds"
	def _str_(self):
		return(self.value)
class listsizeerror(Exception):
	def _init_(self):
		self.value="list out of bounds"
	def _str_(self):
		return(self.value)
class sportserror(Exception):
	def _init_(self):
		self.value="sports not in list"
	def _str_(self):
		return(self.value)





