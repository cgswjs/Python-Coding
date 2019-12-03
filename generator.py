#Generator keeps track on the last outupt yielded
def create_cube(n):
	for x in range(n):
		yield x**3

#no list held only yield last number so less memory used
for x in create_cube(10):
	print(x)

#----------------------------------------------------
#Fibonacci sequence is a good example of generator
def gen_fibon(n):

	a = 1
	b = 1
	for i in range(n):
		yield a
		a,b = b,a+b

for number in gen_fibon(10):
	print(number)

#---------------------------------------
#iter function
s = 'hello'
s_iter = iter(s)
print(next(s_iter))#call the next output