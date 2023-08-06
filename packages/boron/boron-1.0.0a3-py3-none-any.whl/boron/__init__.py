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

import os
import sys

from .wsgi import WSGIApp
from .cli import BoronApp


assert WSGIApp
assert BoronApp

version = '1.0.0alpha3'

description = """
    Boron is a framework for simple http applications. I did not intend to write it, but
    created it while writing ghh as a way to isolate the http logic from the business
    logic of that application.
    """

default_config_file = os.path.join(sys.prefix, 'etc/boron/config.yml')
