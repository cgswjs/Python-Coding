import io
import sys
import urllib.request
from difflib import get_close_matches
# res=urllib.request.urlopen('http://www.baidu.com')
# htmlBytes=res.read()
# print(htmlBytes.decode('utf-8'))
import mysql.connector

#solve unicode problem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') 

#connect to a online remote database
con = mysql.connector.connect(

	user = "ardit700_student",
	password = "ardit700_student",
	host = "108.167.140.122",
	database = "ardit700_pm1database"
	)

#create a cursor to query
cursor = con.cursor()

# word = input("Enter word: ")
word = 'Apple'


# #send a query to database named Dictionary for all data
# query = cursor.execute("SELECT * FROM Dictionary")

#send a query to database named Dictionary for specific data
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)


#get all data
results = cursor.fetchall()
#print fetched tuple data
if results:
	i=0
	for result in results:
		i+=1
		print('{}: '.format(word))
		print('Definition{}. {}'.format(i, result[1].title()))


else:
	#Implement code from app
	query = cursor.execute("SELECT * FROM Dictionary")
	data = cursor.fetchall()
	data_key = []
	for key in range(len(data)):
		data_key.append(data[key][0])
	closestWord = get_close_matches(word, data_key)
	query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %closestWord[0])
	results = cursor.fetchall()
	print('This Word Does Not Exist and Closest Word Is %s' %closestWord[0])
	print('---------------------------------------------------------------')
	print('{}: '.format(closestWord[0].upper()))
	i=0;
	for result in results:
		i+=1
		print('Definition{}. {}'.format(i, result[1].title()))


