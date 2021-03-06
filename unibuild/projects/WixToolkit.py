# Copyright (C) 2015 Sebastian Herbord. All rights reserved.
#
# This file is part of Mod Organizer.
#
# Mod Organizer is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mod Organizer is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mod Organizer.  If not, see <http://www.gnu.org/licenses/>.


from config import config
from unibuild import Project
from unibuild.modules import github

WixToolSet_Version_Binary = config['WixToolSet_Version_Binary']

Project("WixToolkit") \
    .depend(github.Release("wixtoolset", "wix3", "wix{}rtm".format(WixToolSet_Version_Binary),
                           "wix{}-binaries".format(WixToolSet_Version_Binary))
            .set_destination("WixToolkit"))
