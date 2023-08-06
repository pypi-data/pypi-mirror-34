# -*- coding: utf-8 -*-
import argparse


class ArgsUtils:
    def __init__(self, description='parser desc'):
        self.parser = argparse.ArgumentParser(description=description)

    def setArg(self, name, type, required=True, help="say some help"):
        if type == bool:
            type = ArgsUtils.bool_handle
        self.parser.add_argument(name, type=type, required=required, help=help)
        return self

    def get(self):
        return self.parser.parse_args()

    @staticmethod
    def bool_handle(v):
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected.')
