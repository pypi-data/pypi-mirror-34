#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Snippy - command, solution, reference and code snippet manager.
#  Copyright 2017-2018 Heikki J. Laaksonen  <laaksonen.heikki.j@gmail.com>
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""constants: Globals constants for the tool."""

import sys


class Constants(object):  # pylint: disable=too-few-public-methods
    """Globals constants."""

    SPACE = ' '
    EMPTY = ''
    COMMA = ','
    NEWLINE = '\n'

    # Python 2 and 3 compatibility.
    PYTHON2 = sys.version_info.major == 2
    if PYTHON2:
        TEXT_TYPE = unicode  # noqa pylint: disable=undefined-variable
        BINARY_TYPE = str
    else:
        TEXT_TYPE = str
        BINARY_TYPE = bytes

    # Content categories.
    SNIPPET = 'snippet'
    SOLUTION = 'solution'
    REFERENCE = 'reference'
    ALL = 'all'
    UNKNOWN_CONTENT = 'unknown'

    # Content delimiters
    DELIMITER_DATA = NEWLINE
    DELIMITER_TAGS = ','
    DELIMITER_LINKS = NEWLINE

    # Default values for content fields.
    DEFAULT_GROUP = 'default'
