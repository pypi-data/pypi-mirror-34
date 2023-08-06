import flask

app = flask.Flask(__name__)

@app.route('/api/pets', methods=['get'])
def route_pets_get():
    # insert business logic for get on /pets here
    return "Not Implemented", 501


