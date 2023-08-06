#    cli_runner.py
#    This file is part of Linux Dialer.
#
#    Copyright (C) 2018 Sanjay Prajapat <sanjaypra555@gmail.com>
#
#    Linux Dialer is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Linux Dialer is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Linux Dialer.  If not, see <https://www.gnu.org/licenses/>.



"""
Module that handles command line
"""
import sys
from argparse import ArgumentParser
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from linuxdialer import Window
from linuxdialer.vcard_parse import Window as vCardWindow


def parse():
    parser = ArgumentParser()
    parser.add_argument('-t', '--tel', dest='telnum',
                        help='Parse tel: number', metavar='TEL:')
    parser.add_argument('-v', '--vcard', dest='vcardname',
                        help='Extract phonenumber from vcard', metavar='VCARD')
    parser.add_argument('-a', '--any', dest='anything',
                        help='Try to parse anything', metavar='ANYTHING')
    args = parser.parse_args()

    app = QApplication(sys.argv)
    window = None

    if args.telnum:
        window = Window(args.telnum)
    elif args.vcardname:
        vcard_file = Path(args.vcardname).expanduser()
        if not vcard_file.exists():
            print('No such file!')
            exit(0)

        window = vCardWindow(vcard_file.absolute().__str__())
    elif args.anything:
        arg = str(args.anything)
        if 'tel' in arg:
            window = Window(arg)
        elif Path(arg).expanduser().exists():
            window = vCardWindow(arg)
        else:
            print('File not exist.')
            exit(0)
    if window:
        window.show()
        sys.exit(app.exec_())
    else:
        parser.print_help()
