from auth import Basicauth
MONGO_DBNAME = "eve"
#AUTH_FIELD = 'username'
RESOUCE_METHODS = ['GET']
DOMAIN = {
    'signup': {
        'resource_methods': ['POST'],
        'schema': {
            'firstname': {
                'type': 'string',
                'required': True,
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
    'login': {
        'authentication': Basicauth,
        'datasource': {
            'source': 'signup',
        },
        'resource_methods': ['GET'],
        'cache_control': '',
        'cache_expires': 0,

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
