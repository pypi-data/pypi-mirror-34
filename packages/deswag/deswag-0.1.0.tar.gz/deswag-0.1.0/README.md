# deswag

The deswag Python package provides a library and command line tool that can
be used in conjunction with
[OpenAPI](https://github.com/OAI/OpenAPI-Specification) schemas and
[Jinja](http://jinja.pocoo.org/) template files to produce arbitrary output
files. The examples included in this repository demonstrate how this
templating can be used to produce source code representations of the schemas.

## quickstart

The easiest way to start using deswag is by running the examples and examining
the files used and created in the process. We highly recommend the use of the
Python [Virtualenv](https://virtualenv.pypa.io/en/stable/) tool for ease of
deployment and usage.

1. clone repo

1. `pip install .`

1. `deswag -h`

## example

```
deswag --schema examples/petstore-minimal.yaml \
       --template examples/petstore.template \
       --output example.py
```

Try this from the root of the project and then look at what is created in
`example.py`. The file `petstore.template` contains the code structure that
will be applied to the OpenAPI schema `petstore-minimal.yaml`. This code
creates a simple [Flask](https://flask.pocoo.org) server that could be
expanded to provide the API specified in the schema.
