from eve import Eve
from eve.auth import TokenAuth
from eve.auth import BasicAuth
import random
import string

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        # print (resource)
        # print (method) 
        # print (username)
        
        if resource == 'login' and method == 'GET':
            # print("asdas")
            # try:
                signup = app.data.driver.db['signup']
            # except Exception as p:
            #     print(p)
            
            # print (username)
            signup = signup.find_one({'username': username,'password':password})
            # print(signup['username'])
            #self.set_request_auth_value(user['username'])

            if signup:
                # print("asd")
                return True
            else:
                return False
                
        elif resource == 'user' and method == 'POST':
            # print (username)
            # print (password)
            return username == 'admin' and password == 'password'
        else:
            return True


class RolesAuth(TokenAuth):
    def check_auth(self, token,  allowed_roles, resource, method):
        print (resource)
        print (method) 
        print (token)
        # use Eve's own db driver; no additional connections/resources are
        # used
        accounts = app.data.driver.db['user']
        lookup = {'token': token}
        print(lookup)
        return account

def add_token(documents):
    # Don't use this in production:
    # You should at least make sure that the token is unique.
    for document in documents:
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                    for x in range(10)))
 
if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.on_insert_signup += add_token
    app.run()
