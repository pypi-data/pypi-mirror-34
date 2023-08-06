#    test_translate_to_email_qt.py
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



import os

from phonenumbers import parse

from ..translate_to_email import Window


def test_translate_to_email_qt(qtbot):
    """
    Test translate to email Qt GUI
    :param qtbot: fixture to simulate user interaction with Qt widgets
    :return: None
    """
    phonenumber = parse('tel:+16108728537')
    dirname = os.path.dirname(__file__)
    database_testfile = os.path.join(dirname, 'database/db_translate_to_email.db')
    widget = Window(phonenumber, database_testfile)
    qtbot.addWidget(widget)

    assert widget.label.text() == 'Emails found :'
    assert widget.labels[0].text() == 'mrodriguez@yahoo.com'
    assert widget.labels[1].text() == 'mariarodriguez@gmail.com'
