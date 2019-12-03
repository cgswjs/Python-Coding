#Special Methods Instruction
class Book():
	def __init__(self,title,author,pages):

		self.title = title
		self.author = author
		self.pages = pages

	#Special method that returns strings from class
	def __str__(self):
		return f"{self.title} by {self.author}"

	#Special method that returns length from class
	def __len__(self):
		return self.pages

	#Special method that delete 
	def __del__(self):
		print("A book object has been deleted")

b = Book('Python Rocks','Jose',200)
print(b)
print('{} has {} pages.'.format(b,len(b)))
