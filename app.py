from eve import Eve
from auth import add_token
if __name__ == '__main__':
    app = Eve()
    app.on_insert_signup += add_token
    app.run()