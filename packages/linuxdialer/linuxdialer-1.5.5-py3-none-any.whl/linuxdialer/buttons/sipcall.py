#    sipcall.py
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
Module for VoIP call Implementation.
"""
import subprocess
from pathlib import Path

from phonenumbers import format_number, PhoneNumberFormat

name = "VoIP call"
icon = Path(__file__).parent / 'icons' / 'call.png'
apps_required = ('ekiga',)


def launch(parent, phonenumber_obj):
    """
    Open VoIP client (Ekiga) to call
    :param parent: reference of main pop-up window
    :param phonenumber_obj: Phonenumber class object
    :return: None
    """
    phonenumber = format_number(phonenumber_obj, PhoneNumberFormat.E164)  # phonenumber in E164 format
    subprocess.call(['ekiga', '-c', phonenumber])
