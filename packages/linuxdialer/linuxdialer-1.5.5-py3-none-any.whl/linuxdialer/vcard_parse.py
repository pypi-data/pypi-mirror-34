#    vcard_parse.py
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
Module contains vCard file parsing
"""

import vobject
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (QFont)
from PyQt5.QtWidgets import (QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton)
from vobject.base import ParseError

from linuxdialer import Window as DialerWindow


class Window(QWidget):
    """
    Window containting vCard information
    """

    def __init__(self, vcard_path):
        super().__init__()
        status_font = QFont()
        status_font.setPointSize(12)

        small_font = QFont()
        small_font.setPointSize(10)

        outer_box = QVBoxLayout()
        close_button = QHBoxLayout()
        close = QPushButton('Close')
        close.clicked.connect(self.exit_app)
        close_button.addStretch(1)
        close_button.addWidget(close)
        close_button.addStretch(1)
        status = QLabel()
        status.setFont(status_font)
        status.setAlignment(Qt.AlignCenter)
        outer_box.addWidget(status)
        with open(vcard_path, 'r') as file:
            vcard_data = file.read()
        if vcard_data is '':
            status.setText('Not a valid vCard file!')
            status.setStyleSheet("QLabel {color : red; }")
            outer_box.addLayout(close_button)
        else:
            try:
                v = vobject.readOne(vcard_data)
                tels = len(v.tel_list)
            except ParseError:
                status.setText('Not a valid vCard file!')
                status.setStyleSheet("QLabel {color : red; }")
                outer_box.addLayout(close_button)
            except AttributeError:
                status.setText('No phone number found!')
                status.setStyleSheet("QLabel {color : red; }")
                outer_box.addLayout(close_button)
            else:
                if tels is 1:
                    status.setText(str(tels) + ' Phone number found :')
                else:
                    status.setText(str(tels) + ' Phone numbers found :')
                status.setStyleSheet("QLabel {color : green; }")
                tel = []
                for i in range(tels):
                    hbox = QHBoxLayout()
                    type_label = QLabel(*v.tel_list[i].__getattr__('type_paramlist'))
                    type_label.setStyleSheet("QLabel {color : blue; }")
                    type_label.setFont(small_font)
                    tel_number = QLabel(v.tel_list[i].valueRepr())
                    tel_number.setFont(small_font)
                    tel.append(tel_number)
                    open_button = QPushButton('Open')
                    open_button.setFont(small_font)
                    hbox.addWidget(type_label)
                    hbox.addSpacing(20)
                    hbox.addWidget(tel_number)
                    hbox.addStretch(1)
                    hbox.addWidget(open_button)
                    open_button.clicked.connect(lambda state, idx=i: self.onclick_open(tel[idx].text()))
                    outer_box.addLayout(hbox)
        self.setMinimumWidth(400)
        self.setLayout(outer_box)
        self.setWindowTitle("Linux Dialer")

    def onclick_open(self, tel):
        """
        Action while pressing open button
        :param tel: tel number
        :return: None
        """
        window = DialerWindow(tel)
        window.show()

    def exit_app(self):
        """
        Action while pressing close button
        :return: None
        """
        self.close()
