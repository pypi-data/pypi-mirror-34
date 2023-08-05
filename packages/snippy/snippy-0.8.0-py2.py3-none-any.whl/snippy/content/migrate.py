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

"""migrate: Import and export management."""

from __future__ import print_function

import json
import os.path

import yaml

from snippy.cause import Cause
from snippy.config.config import Config
from snippy.constants import Constants as Const
from snippy.content.collection import Collection
from snippy.logger import Logger
from snippy.meta import __homepage__
from snippy.meta import __version__


class Migrate(object):
    """Import and export management."""

    _logger = Logger.get_logger(__name__)

    @classmethod
    def dump(cls, collection, filename):
        """Dump collection into file."""

        if not Config.is_supported_file_format():
            cls._logger.debug('file format not supported for file %s', filename)

            return

        if collection.empty():
            cls._logger.debug('no content to be exported')

            return

        cls._logger.debug('exporting contents %s', filename)
        with open(filename, 'w') as outfile:
            try:
                dictionary = {'meta': {'updated': Config.utcnow(),
                                       'version': __version__,
                                       'homepage': __homepage__},
                              'data': collection.dump_dict(Config.remove_fields)}
                if Config.is_operation_file_text:
                    for resource in collection.resources():
                        template = resource.dump_text(Config.templates)
                        outfile.write(template)
                        outfile.write(Const.NEWLINE)
                elif Config.is_operation_file_json:
                    json.dump(dictionary, outfile)
                    outfile.write(Const.NEWLINE)
                elif Config.is_operation_file_yaml:
                    yaml.safe_dump(dictionary, outfile, default_flow_style=False)
                else:
                    cls._logger.debug('unknown export file format')
            except (IOError, TypeError, ValueError, yaml.YAMLError) as exception:
                cls._logger.exception('fatal failure to generate formatted export file "%s"', exception)
                Cause.push(Cause.HTTP_INTERNAL_SERVER_ERROR, 'fatal failure while exporting content to file')

    @classmethod
    def dump_template(cls, category):
        """Dump content template into file."""

        filename = Config.get_operation_file()
        resource = Collection.get_resource(category, Config.utcnow())
        template = resource.dump_text(Config.templates)
        cls._logger.debug('exporting content template %s', filename)
        with open(filename, 'w') as outfile:
            try:
                outfile.write(template)
            except IOError as exception:
                cls._logger.exception('fatal failure in creating %s template file "%s"', category, exception)
                Cause.push(Cause.HTTP_INTERNAL_SERVER_ERROR, 'fatal failure while exporting template {}'.format(filename))

    @classmethod
    def load(cls, filename):
        """Load dictionary from file."""

        collection = Collection()
        if not Config.is_supported_file_format():
            cls._logger.debug('file format not supported for file %s', filename)

            return collection

        cls._logger.debug('importing contents from file %s', filename)
        if os.path.isfile(filename):
            with open(filename, 'r') as infile:
                try:
                    if Config.is_operation_file_text:
                        collection = Config.get_collection(text=infile.read())
                    elif Config.is_operation_file_json:
                        dictionary = json.load(infile)
                        collection.load_dict(dictionary)
                    elif Config.is_operation_file_yaml:
                        dictionary = yaml.safe_load(infile)
                        collection.load_dict(dictionary)
                    else:
                        cls._logger.debug('unknown import file format')
                except (TypeError, ValueError, yaml.YAMLError) as exception:
                    cls._logger.exception('fatal exception while loading file "%s"', exception)
                    Cause.push(Cause.HTTP_INTERNAL_SERVER_ERROR, 'fatal failure while importing content from file')

        else:
            Cause.push(Cause.HTTP_NOT_FOUND, 'cannot read file {}'.format(filename))

        return collection
