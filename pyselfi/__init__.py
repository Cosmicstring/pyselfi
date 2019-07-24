#!/usr/bin/env python
#-------------------------------------------------------------------------------------
# pySELFI v1.1 -- pyselfi/__init__.py
# Copyright (C) 2019-2019 Florent Leclercq.
# 
# This file is part of the pySELFI distribution
# (https://github.com/florent-leclercq/pyselfi/)
# 
# This program is free software: you can redistribute it and/or modify  
# it under the terms of the GNU General Public License as published by  
# the Free Software Foundation, version 3.
# 
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
# General Public License for more details.
# 
# The text of the license is located in the root directory of the source package.
#-------------------------------------------------------------------------------------

"""pyselfi __init__
"""

__author__  = "Florent Leclercq"
__date__    = "2018-2019"
__version__ = "1.1"
__license__ = "GPLv3"

from .selfi import selfi
from .likelihood import likelihood
from .posterior import posterior
from .pool import pool
