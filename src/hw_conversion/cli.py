'''Command line interface for homework script creation.'''
import argparse
import toml
import logging

from hw_conversion import convert_hw


def _parse_config_file(f):
    parsed = toml.load(f)
    pattern = parsed.get('pattern', None)
    hw_file = parsed.get('hw_file', 'Homework.ipynb')

    return pattern, hw_file


def main(args=None):
    '''Process command-line arguments and run the program'''
    project = argparse.ArgumentParser(description='Convert notebook to script.')
    project.add_argument('-c', '--config', default='config.ini', type=open,
        help='Config file location.')

    parsed_args = project.parse_args(args)
    pattern, hw_file = _parse_config_file(parsed_args.config)

    convert_hw(pattern, hw_file)


if __name__ == '__main__':
    main()