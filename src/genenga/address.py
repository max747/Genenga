# -*- coding: utf-8 -*-
"""
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012,2013 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import csv

class Address(object):

    def __init__(self, infile):
        self.address_file = infile

    def address(self):
        address = []
        with open(self.address_file) as f:
            csv_reader = csv.reader(f)

            for l in csv_reader:
                # check a printing flag
                if l[0] == '0':
                    continue

                if len(l) == 8:
                    address.append(
                        {"last_name":   l[1],
                         "first_name1": l[2],
                         "first_name2": l[3],
                         "address":     l[4],
                         "address2":    l[5],
                         "address3":    l[6],
                         "no1":         l[7][0],
                         "no2":         l[7][1],
                         "no3":         l[7][2],
                         "no4":         l[7][3],
                         "no5":         l[7][4],
                         "no6":         l[7][5],
                         "no7":         l[7][6],
                         })
                else:
                    address.append(
                        {"last_name":   l[1],
                         "first_name1": l[2],
                         "first_name2": l[3],
                         "address":     l[4],
                         "address2":    l[5],
                         "no1":         l[6][0],
                         "no2":         l[6][1],
                         "no3":         l[6][2],
                         "no4":         l[6][3],
                         "no5":         l[6][4],
                         "no6":         l[6][5],
                         "no7":         l[6][6],
                         })
        return address
