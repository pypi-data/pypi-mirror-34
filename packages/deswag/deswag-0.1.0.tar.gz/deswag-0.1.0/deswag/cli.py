"""deswag cli front end"""
import argparse
import yaml

from deswag import templater


def get_args():
    parser = argparse.ArgumentParser(
        description="Convert OpenAPI definitions.")
    parser.add_argument(
        '--schema',
        help='filename of OpenAPI schema to convert (yaml)',
        required=True)
    parser.add_argument(
        '--template',
        help='filename of template to apply for conversion',
        required=True)
    parser.add_argument(
        '--output',
        help='name of file to output',
        required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    schema_text = open(args.schema).read()
    schema_data = yaml.load(schema_text)
    tmpl_text = open(args.template).read()

    output = templater.Templater(tmpl_text).render(schema_data)
    out_file = open(args.output, 'w')
    out_file.write(output)
