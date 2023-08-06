########################################################################
#
# model.py
#
# Copyright (C) 2018 Antonio Ceballos Roa
#
#   This file is part of Simcore.
#
#   Simcore is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   Simcore is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with Simcore.  If not, see <https://www.gnu.org/licenses/>.
#
########################################################################

import abc

class Model(abc.ABC):
    """Abstract model
    """

    def __init__(self):
        pass

    @abc.abstractmethod
    def step(self, deltatime=1):
        """Apply model's law for a step worth of time

        Arguments:
          deltatime - time in seconds to apply
        """
        pass
