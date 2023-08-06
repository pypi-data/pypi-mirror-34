#    test_button_framework_qt.py
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



from PyQt5 import QtCore

from linuxdialer import Window
from . import hello_once, hello_twice


def test_button_framework(qtbot):
    """
    Test if buttons are created or not. custom buttons data is provided
    :param qtbot: fixture to simulate user interaction with Qt widgets
    :return: None
    """
    data = (hello_once, hello_twice)
    widget = Window('tel:+919988776655', data)
    qtbot.addWidget(widget)

    qtbot.mouseClick(widget.button[0], QtCore.Qt.LeftButton)
    qtbot.mouseClick(widget.button[1], QtCore.Qt.LeftButton)
    assert len(widget.button) == 2
    assert widget.button[0].toolTip() == 'Print Phonenumber Once'
    assert widget.button[1].toolTip() == 'Print Phonenumber Twice'
