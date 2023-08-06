# Copyright 2018 Brandon Schlueter
# This file is part of boron.
#
# Boron is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import print_function

import argparse
import sys

import bjoern


class BoronApp:

    def __init__(self, app, description, default_config_file=''):
        self.description = description
        self.default_config_file = default_config_file
        self.app = app

    def parse_args(self, description, default_config_file):
        parser = argparse.ArgumentParser(description=description)
        parser.add_argument(
            '-a', '--host',
            type=str,
            default='0.0.0.0',
            help='A host listen on.')
        if default_config_file:
            parser.add_argument(
                '-c', '--config-file',
                type=argparse.FileType('r'),
                help='Specify the path to a configuration file.')
        parser.add_argument(
            '-p', '--port',
            type=int,
            help='A port to listen on.')
        parser.add_argument(
            '-r', '--reuse-port',
            action='store_true',
            help='Enables SO_REUSEPORT if available.')
        parser.add_argument(
            '-s', '--socket',
            type=str,
            help='A socket to listen on.')

        return (parser, parser.parse_args())

    def main(self):
        parser, args = self.parse_args(self.description, self.default_config_file)

        # TODO allow port, socket, and host config from config file
        if not (args.socket or args.port):
            print('Either a socket or port must be specified.\n', file=sys.stderr)
            parser.print_help(sys.stderr)
            exit(2)

        listen_address = args.socket if args.socket else ':'.join([args.host, str(args.port)])

        try:
            bjoern.listen(self.app(), args.host or args.socket, args.port, reuse_port=args.reuse_port)
            print('Listening at {listen_address}'.format(listen_address=listen_address), file=sys.stderr)
            bjoern.run()
        except KeyboardInterrupt:
            print('\rExit requested', file=sys.stderr)
            exit()


def main():
    import boron
    from .wsgi import WSGIApp

    app = BoronApp(WSGIApp, boron.description, boron.default_config_file)
    app.main()
