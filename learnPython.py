mylist = [1,2,3]
ml = len(mylist)
class Book():
	def __init__(self,title,author,pages):

		self.title = title
		self.author = author
		self.pages = pages
	def __str__(self):
		return f"{self.title} by {self.author}"
		
b = Book('Python Rocks','Jose',200)
print(b)