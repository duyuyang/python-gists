class Person(object):
	def __init__(self, name):
		self.name = name

	def printName(self):
		print self.name

class Student(Person):
	def __init__(self, name, stuId):
		super(Student, self).__init__(name)
		self.stuId = stuId

stu = Student('Adrew', '2837')
stu.printName()
