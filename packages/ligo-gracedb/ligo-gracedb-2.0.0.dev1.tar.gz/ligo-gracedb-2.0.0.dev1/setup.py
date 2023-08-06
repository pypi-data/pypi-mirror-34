# -*- coding: utf-8 -*-
# Copyright (C) Brian Moe, Branson Stephens (2015)
#
# This file is part of gracedb
#
# gracedb is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with gracedb.  If not, see <http://www.gnu.org/licenses/>.

from setuptools import setup, find_packages
from ligo.gracedb import __version__

setup(
  name = "ligo-gracedb",
  version = __version__,
  maintainer = "Tanner Prestegard, Alexander Pace",
  maintainer_email = "tanner.prestegard@ligo.org, alexander.pace@ligo.org",
  description = "Gravitational Wave Candidate Event Database",
  long_description = "The gravitational wave candidate event database (GraceDB) is a system to organize candidate events from gravitational wave searches and to provide an environment to record information about follow-ups. A simple client tool is provided to submit a candidate event to the database.",

  url = "https://wiki.ligo.org/DASWG/GraceDB",
  license = 'GPL',
  namespace_packages = ['ligo'],
  #provides = ['ligo.gracedb'],
  packages = find_packages(),

  install_requires = ['six'],

  package_data = { 'ligo.gracedb.test' : ['data/*', 'test.sh', 'README'] },
  entry_points={
      'console_scripts': [
          'gracedb=ligo.gracedb.cli:main',
      ],
  }

)
