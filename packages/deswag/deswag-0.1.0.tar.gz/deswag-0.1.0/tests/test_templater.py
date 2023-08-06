import unittest

from deswag import templater

from . import constants as c


class TestOpenAPIv2Schema(unittest.TestCase):
    def setUp(self):
        self.template = c.PETSTORE_TEMPLATE
        self.data = c.PETSTORE_DATA

    def test_render(self):
        expected = c.PETSTORE_PYTHON
        observed = templater.Templater(self.template).render(self.data)
        self.assertEqual(observed, expected)
