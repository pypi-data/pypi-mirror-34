import unittest

from deswag import exceptions as ex
from deswag import schemas

from . import constants as c


class TestOpenAPIv2Schema(unittest.TestCase):
    def setUp(self):
        self.source = c.VALID_20_SCHEMA
        self.rsource = c.VALID_20_SCHEMA_REQUIRED_ONLY

    def test_data(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertIsInstance(observed, dict)

    def test_valid_schema(self):
        self.assertIsNone(schemas.OpenAPIv2Schema._validate(self.source))

    def test_invalid_schema(self):
        with self.assertRaises(ex.ValidationError):
            observed = schemas.OpenAPIv2Schema(c.INVALID_SCHEMA)

    def test_swagger(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('swagger' in observed)
        self.assertEquals('2.0', observed.get('swagger'))

    def test_info(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('info' in observed)

    def test_paths(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('paths' in observed)

    def test_host(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('host' in observed)
        self.assertEqual(observed['host'], 'petstore.swagger.io')
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['host'])

    def test_basePath(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('basePath' in observed)
        self.assertEqual(observed['basePath'], '/api')
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['basePath'])

    def test_schemes(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('schemes' in observed)
        self.assertListEqual(observed['schemes'], ['http'])
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['schemes'])

    def test_consumes(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('consumes' in observed)
        self.assertListEqual(observed['consumes'], ['application/json'])
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['consumes'])

    def test_produces(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('produces' in observed)
        self.assertListEqual(observed['produces'], ['application/json'])
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['produces'])

    def test_definitions(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('definitions' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['produces'])

    def test_parameters(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('parameters' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['parameters'])

    def test_responses(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('responses' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['responses'])

    def test_securityDefinitions(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('securityDefinitions' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['securityDefinitions'])

    def test_security(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('security' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['security'])

    def test_tags(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('tags' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['tags'])

    def test_externalDocs(self):
        observed = schemas.OpenAPIv2Schema(self.source).data()
        self.assertTrue('externalDocs' in observed)
        observed = schemas.OpenAPIv2Schema(self.rsource).data()
        self.assertIsNone(observed['externalDocs'])



class TestInfoObjectv2(unittest.TestCase):
    def setUp(self):
        self.source = c.VALID_20_SCHEMA['info']

    def test_data(self):
        observed = schemas.InfoObjectv2(self.source).data()
        self.assertIsInstance(observed, dict)

    def test_data_title(self):
        observed = schemas.InfoObjectv2(self.source).data()
        self.assertTrue('title' in observed)
        self.assertEquals('Swagger Petstore', observed.get('title'))

    def test_data_version(self):
        observed = schemas.InfoObjectv2(self.source).data()
        self.assertTrue('version' in observed)
        self.assertEquals('1.0.0', observed.get('version'))


class TestPathsObjectv2(unittest.TestCase):
    def setUp(self):
        self.source = c.VALID_20_SCHEMA['paths']
    def test_data(self):
        observed = schemas.PathsObjectv2(self.source).data()
        self.assertIsInstance(observed, dict)

    def test_path(self):
        observed = schemas.PathsObjectv2(self.source).data()
        self.assertTrue('/pets' in observed)

    def test_extension(self):
        observed = schemas.PathsObjectv2(self.source).data()
        self.assertTrue('x-test-field' in observed)
        self.assertEqual('some value', observed.get('x-test-field'))


class TestPathItemObjectv2(unittest.TestCase):
    def setUp(self):
        self.source = c.VALID_20_SCHEMA['paths']['/pets']

    def test_data(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertIsInstance(observed, dict)

    def test_ref(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('$ref' in observed)

    def test_get(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('get' in observed)

    def test_put(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('put' in observed)

    def test_post(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('post' in observed)

    def test_delete(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('delete' in observed)

    def test_options(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('options' in observed)

    def test_head(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('head' in observed)

    def test_patch(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('patch' in observed)

    def test_parameters(self):
        observed = schemas.PathItemObjectv2(self.source).data()
        self.assertTrue('parameters' in observed)



