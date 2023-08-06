#    truecaller.py
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
Module for Truecaller Implementation
"""
from pathlib import Path
from webbrowser import open

from phonenumbers.phonenumberutil import region_code_for_country_code

name = 'Truecaller'
icon = Path(__file__).parent / 'icons' / 'truecaller.png'


def generate_url(phonenumber_obj):
    """
    Generate truecaller search url.
    :param country_code: country code to generate two letter ISO code.
    :param phonenumber: phone number
    :return: truecaller search url
    """
    country_code = phonenumber_obj.country_code
    phonenumber = str(phonenumber_obj.national_number)

    iso_code = region_code_for_country_code(int(country_code)).lower()
    url = 'https://www.truecaller.com/search/' + iso_code + '/' + phonenumber
    return url


def launch(parent, phonenumber_obj):
    """
    Open truecaller search url in default browser.

    :param parent: Unused
    :param phonenumber_obj: PhoneNumber class object
    :return: None
    """
    open(generate_url(phonenumber_obj))
