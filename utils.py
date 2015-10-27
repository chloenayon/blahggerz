import shelve, sqlite3
from pymongo import MongoClient

data_base = 'data'

#database is 'userList'
#table of user is 'users'
#fields: uname, passwd

def authenticate(name,word):
	conn = MongoClient()
        db = conn['userList']
#	q = 'SELECT usersList.user FROM usersList WHERE usersList.pass = %(user)s'
	userN = str(name)
	passW = str(word)
        result = db.users.find({'uname' : userN} , {'passwd': passW})

#	result = c.execute('SELECT DISTINCT usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))

	return loginResponse(result, passW)

def loginResponse(realPass, inputPass):
	for x in realPass:
		if x[0] == inputPass:
			return "success"
		return "fail"
	return "noUser"


def add(uname, pword):
	response = "failed"
	conn = MongoClient()
        db = conn[data_base]
	userN = str(uname)
	passW = str(pword)

        result = db.users.find({'uname' : userN})
#	result = c.execute('SELECT DISTINCT usersList.user,usersList.pass FROM usersList WHERE usersList.user = ?', (userN,))
	for x in result:
		print x[0]
		print userN
		if x[0] == userN:
			response = "taken"
	if response != "taken":
		response = "success"
		inputUser(userN, passW)

	return response

def inputUser(username, password):
	conn = MongoClient()
	db = conn[data_base]
        db.users.insert({'uname' : username , 'passwd' : password})
#	c.execute('INSERT INTO usersList VALUES (?, ?)', (username, password))
	
def addPost(userN, timeT, message):
	conn = MongoClient()
	db = conn[data_base]
	n = findPostNum() + 1
	db.posts.insert({'user' : userN, 'time': timeT, 'msg' : message})
#	c.execute('INSERT INTO postsList VALUES (?, ?, ?, ?)', (user, time, message, n))
	#print("success")
	
def findPostNum():
	conn = MongoClient()
	db = conn[data_base]
	nums = c.execute('SELECT postsList.postNum FROM postsList ORDER BY postsList.postNum DESC')
	for x in nums:
		return x[0]
		break

def deletePost(postN):
	conn = MongoClient()
	db = conn[data_base]
#	c.execute('DELETE FROM postsList WHERE postsList.postNum = ?', (postNum,))
	db.posts.remove({'postNum' : postN})
	print("success")
	
def getPosts():
	conn = MongoClient()
	db = conn[data_base]
	allPosts = db.posts.find({})
#	posts = c.execute("SELECT DISTINCT * FROM postsList ORDER BY postsList.postNum DESC")
	return allPosts

	
