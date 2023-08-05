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

"""editor: Text editor based content management."""

import os

from snippy.cause import Cause
from snippy.constants import Constants as Const
from snippy.config.source.parser import Parser
from snippy.content.collection import Collection
from snippy.logger import Logger


class Editor(object):
    """Text editor based content management."""

    _logger = Logger.get_logger(__name__)

    @classmethod
    def read_content(cls, timestamp, template):
        """Read content from editor."""

        source = cls.call_editor(template)
        category = Parser.content_category(source)
        collection = Collection()
        if category in (Const.SNIPPET, Const.SOLUTION, Const.REFERENCE):
            resource = collection.get_resource(category, timestamp)
            resource.data = Parser.content_data(category, source)
            resource.brief = Parser.content_brief(category, source)
            resource.group = Parser.content_group(category, source)
            resource.tags = Parser.content_tags(category, source)
            resource.links = Parser.content_links(category, source)
            resource.category = category
            resource.filename = Parser.content_filename(category, source)
            resource.digest = resource.compute_digest()
            collection.migrate(resource)
        else:
            Cause.push(Cause.HTTP_BAD_REQUEST, 'could not identify edited content category - please keep tags in place')

        return collection

    @classmethod
    def call_editor(cls, template):
        """Run editor session."""

        import tempfile
        from subprocess import call

        # External dependencies are isolated in this method to ease
        # testing. This method is mocked to return the edited text.
        message = Const.EMPTY
        template = template.encode('UTF-8')
        editor = cls._get_editor()
        cls._logger.debug('using %s as editor', editor)
        with tempfile.NamedTemporaryFile(prefix='snippy-edit-') as outfile:
            outfile.write(template)
            outfile.flush()
            try:
                call([editor, outfile.name])
                outfile.seek(0)
                message = outfile.read()
                message = message.decode('UTF-8')
            except OSError as exception:
                Cause.push(Cause.HTTP_INTERNAL_SERVER_ERROR, 'required editor %s not installed %s' % (editor, exception))

        return message

    @classmethod
    def _get_editor(cls):
        """Try to resolve the editor in a secure way."""

        # Running code blindly from environment variable is not safe because
        # the call would execute any command from environment variable.
        editor = os.environ.get('EDITOR', 'vi')

        # Avoid usage other than supported editors as of now for security
        # and functionality reasons. What is the safe way to check the
        # environment variables? What is the generic way to use editor in
        # Windows and Mac?
        if editor != 'vi':
            cls._logger.debug('enforcing vi as default editor instead of %s', editor)
            editor = 'vi'

        return editor
