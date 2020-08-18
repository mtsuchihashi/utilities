# /usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import os

from jinja2 import Template, Environment, FileSystemLoader



def generate_parser(description=""):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('template', help='')
    parser.add_argument('--out',  help='')

    return parser


if __name__ == '__main__':
    parser = generate_parser()
    args = parser.parse_args()
    if not args.out:
        filename, ext = os.path.splitext(args.template)
        args.out = filename+".py"

    env = Environment(loader=FileSystemLoader('.', encoding='utf_8'))
    template = env.get_template(args.template)
    with open('./setup.snp') as f:
        d = f.read()

    with open('./test01.snp') as f:
        d2 = f.read()

    data = {
        'test_module': 'foobar',
        'test_target': 'FooBar',
        'modules': [
        {'name' : 'sys'},
        {'name' : 'os', 'target': 'path'},
        ],
        'setups': d.split('\n'),
        'testees': d2.split('\n'),
        }

    print(template.render(data))

