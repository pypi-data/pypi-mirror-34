# -*- coding: utf-8 -*-


# PyMeeus: Python module implementing astronomical algorithms.
# Copyright (C) 2018  Dagoberto Salazar
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


"""
.. module:: base
   :synopsis: Basic routines and constants used by the pymeeus module
   :license: GNU Lesser General Public License v3 (LGPLv3)

.. moduleauthor:: Dagoberto Salazar
"""


TOL = 1E-10
"""Internal tolerance being used by default"""


def machine_accuracy():
    """This function computes the accuracy of the computer being used.

    :returns: A tuple containing the number of significant bits in the mantissa
    of a floating number, and the number of significant digits in a decimal
    number.
    :rtype: tuple
    """
    j = 0.0
    x = 2.0
    while x + 1.0 != x:
        j += 1.0
        x *= 2.0
    return (j, int(j*0.30103))


def main():

    # Let's define a small helper function
    def print_me(msg, val):
        print("{}: {}".format(msg, val))

    # Let's print the tolerance
    print_me("The default value for the tolerance is", TOL)

    # Find the accuracy of this computer
    j, d = machine_accuracy()
    print_me("Number of significant BITS in the mantissa\t", j)
    print_me("Number of significant DIGITS in a decimal number", d)


if __name__ == '__main__':

    main()
