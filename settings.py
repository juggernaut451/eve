RESOURCE_METHODS = ['GET', 'POST']
DOMAIN = {
    'user': {
        'schema': {
            'firstname': {
                'type': 'string'
            },
            'lastname': {
                'type': 'string'
            },
            'username': {
                'type': 'string',
                 'unique': True
            },
            'password': {
                'type': 'string'
            },
            'phone': {
                'type': 'string'
            },
            'token': {
             'type': 'string',
             
         }
        },
        'extra_response_fields': ['token'],
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
            },
    }
}
