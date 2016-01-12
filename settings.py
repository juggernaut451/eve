from auth import Authenticate
MONGO_DBNAME = "eve"
#AUTH_FIELD = 'username'
RESOUCE_METHODS = ['GET']
DOMAIN = {
    'signup': {
        'resource_methods': ['POST'],
        'schema': {
            'firstname': {
                'type': 'string',
                'required' : True,
            },
            'lastname': {
                'type': 'string',
                'required': True,
            },
            'username': {
                'type': 'string',
                 'unique': True,
            },
            'password': {
                'type': 'string',
                'required': True,
            },
            'phone': {
                'type': 'string',
                'required': True,
            },
            
        },

    },
    'login' : {
    'authentication': Authenticate,
    'datasource': {
        'source': 'signup',
        },
    'resource_methods': ['GET'],
    'cache_control': '',
    'cache_expires': 0,
    #'extra_response_fields': ['token'],
    
    'schema': {     
            'username': {
                'type': 'string',
                'required': True,
            },
            'password': {
                'type': 'string',
                'required': True,
            },
            'token': {
             'type': 'string',
             'required': True,
         }
            
        },
    'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
            }
    },
}
