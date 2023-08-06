# This program is free software: you can redistribute it and/or modify
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
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
# (C) 2018 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>

from kicad.pcbnew.boarditem import BoardItem
from kicad.pcbnew.net import Net

from kicad._native import _pcbnew


class Via(BoardItem):
    def __init__(self, via):
        assert isinstance(via, _pcbnew.VIA)
        super(Via, self).__init__(via)

    def get_native(self):
        """Get native object from the low level API

        :return: :class:`pcbnew.VIA`
        """
        return self._obj

    @property
    def net(self):
        """Net of the Via

        :return: :class:`kicad.pcbnew.Net`
        """
        return Net(self._obj.GetNet())

    def __repr__(self):
        return "kicad.pcbnew.Via({})".format(self._obj)

    def __str__(self):
        return "kicad.pcbnew.Via(\"{}\")".format(self.net.name)
