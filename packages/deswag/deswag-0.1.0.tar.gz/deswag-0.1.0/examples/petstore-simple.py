import flask

app = flask.Flask(__name__)


@app.route('/api/pets', methods=['get'])
def route_pets_get():
    # insert business logic for get on /pets here
    return "Not Implemented", 501


@app.route('/api/pets', methods=['post'])
def route_pets_post():
    # insert business logic for post on /pets here
    return "Not Implemented", 501


@app.route('/api/pets/<id>', methods=['get'])
def route_pets_id_get():
    # insert business logic for get on /pets/{id} here
    return "Not Implemented", 501


@app.route('/api/pets/<id>', methods=['delete'])
def route_pets_id_delete():
    # insert business logic for delete on /pets/{id} here
    return "Not Implemented", 501
