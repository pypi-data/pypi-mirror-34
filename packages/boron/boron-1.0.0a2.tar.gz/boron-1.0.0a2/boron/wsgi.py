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


class WSGIApp:

    def __init__(self):
        allowed_http_methods = [
            func.lstrip('handle_http_').upper()
            for func in dir(self)
            if callable(getattr(self, func))
            and func.startswith('handle_http_')
        ]
        allowed_http_methods.remove('UNKNOWN')
        self.allowed_http_methods = allowed_http_methods

    def __call__(self, environ, start_response):
        http_method_handler = getattr(
            self,
            'handle_http_' + environ['REQUEST_METHOD'].lower(),
            self.handle_http_unknown
        )
        return [http_method_handler(environ, start_response).encode()]

    def handle_http_unknown(self, environ, start_response):
        response_headers = [
            ('Content-type', 'text/plain'),
            ('Allow', ', '.join(self.allowed_http_methods))
        ]
        start_response('405 Method Not Allowed', response_headers)
        return 'Unknown HTTP method {method}.'.format(method=environ['REQUEST_METHOD'])
