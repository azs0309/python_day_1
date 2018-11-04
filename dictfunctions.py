#!/bin/python
def createUser(username,password,**meta):
  user = {}
  user['username']=username
  user['password']=password
  for k,v in meta.items():
    user[k]=v
  return user
  
user = createUser("sam","",job="Devops Engineer",age="35",country="US")
print(user)

