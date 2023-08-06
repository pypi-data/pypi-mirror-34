# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015, 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.
"""Resolve JSON for FundRef funders."""

from __future__ import absolute_import, print_function

import jsonresolver
from invenio_pidstore.resolver import Resolver
from invenio_records.api import Record
from werkzeug.routing import Rule


@jsonresolver.hookimpl
def jsonresolver_loader(url_map):
    """Jsonresolver hook for funders resolving."""
    def endpoint(doi_code):
        pid_value = "10.13039/{0}".format(doi_code)
        _, record = Resolver(pid_type='frdoi', object_type='rec',
                             getter=Record.get_record).resolve(pid_value)
        return record

    pattern = '/10.13039/<doi_code>'
    url_map.add(Rule(pattern, endpoint=endpoint, host='doi.org'))
    url_map.add(Rule(pattern, endpoint=endpoint, host='dx.doi.org'))
