#    vcard.py
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
Module for performing vCard operations
"""
from vobject import vCard


def _set(var, data):
    """
    Unpack tuple and set vcard attr and type_param.
    :param var: vcard attr
    :param data: tuple -> (value, type_param)
    :return: None
    """
    value, type = data
    var.type_param = type
    var.value = value


def create_vcard(uid, name, phonenumber, email, address):
    """
    Method for creating vcard from given information.
    :param uid: A Primary key that is used in GNOME-Contacts/Evolution database to identify a contact uniquely
    :param name: Name of contact
    :param phonenumber: phonenumber tuple -> (phonenumber, type)
    :param email: email tuple -> (email, type)
    :param address: address tuple -> (address, type)
    :return: vcard data
    """
    vcard = vCard()
    vcard.add('uid')
    vcard.uid.value = uid
    vcard.add('fn')
    vcard.fn.value = ' '.join(filter(None, (name.given, name.additional, name.family)))
    vcard.add('n')
    vcard.n.value = name
    if phonenumber:
        vcard.add('tel')
        _set(vcard.tel, phonenumber)
    if email:
        vcard.add('email')
        _set(vcard.email, email)
    if address:
        vcard.add('adr')
        _set(vcard.adr, address)
    return vcard.serialize()
