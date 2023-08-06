INVALID_SCHEMA = {"swagger": "no"}

VALID_20_SCHEMA_REQUIRED_ONLY = {
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Swagger Petstore",
  },
  "paths": {
  },
}

VALID_20_SCHEMA = {
  "swagger": "2.0",
  "info": {
    "version": "1.0.0",
    "title": "Swagger Petstore",
    "description": "A sample API that uses a petstore as an example to demonstrate features in the swagger-2.0 specification",
    "termsOfService": "http://swagger.io/terms/",
    "contact": {
      "name": "Swagger API Team"
    },
    "license": {
      "name": "MIT"
    }
  },
  "host": "petstore.swagger.io",
  "basePath": "/api",
  "schemes": [
    "http"
  ],
  "consumes": [
    "application/json"
  ],
  "produces": [
    "application/json"
  ],
  "paths": {
    "/pets": {
      "get": {
        "description": "Returns all pets from the system that the user has access to",
        "produces": [
          "application/json"
        ],
        "responses": {
          "200": {
            "description": "A list of pets.",
            "schema": {
              "type": "array",
              "items": {
                "$ref": "#/definitions/Pet"
              }
            }
          }
        }
      }
    },
    "x-test-field": "some value"
  },
  "definitions": {
    "Pet": {
      "type": "object",
      "required": [
        "id",
        "name"
      ],
      "properties": {
        "id": {
          "type": "integer",
          "format": "int64"
        },
        "name": {
          "type": "string"
        },
        "tag": {
          "type": "string"
        }
      }
    }
  }
}

PETSTORE_TEMPLATE = """import flask

app = flask.Flask(__name__)
{% for path, pathitem in paths.items() %}
{% for method, operation in pathitem.items() %}
@app.route('{{ [basePath, path]|join|replace('{', '<')|replace('}', '>') }}', methods=['{{ method }}'])
def route{{ path|replace('/', '_')|replace('{', '_')|replace('}', '_') }}_{{ method }}():
    # insert business logic for {{ method }} on {{ path }} here
    return "Not Implemented", 501

{% endfor %}
{% endfor %}
"""

PETSTORE_DATA = {
    'swagger': '2.0',
    'info': {
        'version': '1.0.0',
        'title': 'Swagger Petstore',
        'description': 'A sample API that uses a petstore as an example to demonstrate features in the swagger-2.0 specification',
        'termsOfService': 'http://swagger.io/terms/',
        'contact': {
            'name': 'Swagger API Team'},
        'license': {'name': 'MIT'}
    },
    'host': 'petstore.swagger.io',
    'basePath': '/api',
    'schemes': ['http'],
    'consumes': ['application/json'],
    'produces': ['application/json'],
    'paths': {
        '/pets': {
            'get': {
                'description': 'Returns all pets from the system that the user has access to',
                'produces': ['application/json'],
                'responses': {
                    '200': {
                        'description': 'A list of pets.',
                        'schema': {
                            'type': 'array',
                            'items': {'$ref': '#/definitions/Pet'}
                        }
                    }
                }
            }
        }
    },
    'definitions': {
        'Pet': {
            'type': 'object',
            'required': ['id', 'name'],
            'properties': {
                'id': {
                    'type': 'integer',
                    'format': 'int64'
                },
                'name': {'type': 'string'},
                'tag': {'type': 'string'}
            }
        }
    }
}

PETSTORE_PYTHON = """import flask

app = flask.Flask(__name__)


@app.route('/api/pets', methods=['get'])
def route_pets_get():
    # insert business logic for get on /pets here
    return "Not Implemented", 501


"""
