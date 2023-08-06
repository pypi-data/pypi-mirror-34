#    hello_twice.py
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
Information about button 2
"""
from pathlib import Path

from phonenumbers import format_number, PhoneNumberFormat

name = 'Print Phonenumber Twice'
icon = Path(__file__).parent / 'icons' / '2.png'


def say(phonenumber):
    print(phonenumber)
    print(phonenumber)


def launch(ref, phonenumber_obj):
    phonenumber = format_number(phonenumber_obj, PhoneNumberFormat.E164)
    say(phonenumber)
