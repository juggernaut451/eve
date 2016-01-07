from eve import Eve
from eve.auth import TokenAuth
from eve.auth import BasicAuth
import random
import string

class Authenticate(BasicAuth):
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        if resource == 'user' and method == 'GET':
            user = app.data.driver.db['user']
            user = user.find_one({'username': username,'password':password})
            if user:
                return True
            else:
                return False

def add_token(documents):
    # Don't use this in production:
    # You should at least make sure that the token is unique.
    for document in documents:
        document["token"] = (''.join(random.choice(string.ascii_uppercase)
                                    for x in range(10)))
 
if __name__ == '__main__':
    app = Eve(auth=Authenticate)
    app.on_insert_user += add_token
    app.run()
