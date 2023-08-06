#    test_truecaller_generate_url.py
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



import pytest
from phonenumbers import parse

from ..truecaller import generate_url

testcases = (
    ('+919829142536', 'https://www.truecaller.com/search/in/9829142536'),
    ('+12024561111', 'https://www.truecaller.com/search/us/2024561111'),
    ('+441632960746', 'https://www.truecaller.com/search/gb/1632960746'),
    ('+16135550124', 'https://www.truecaller.com/search/us/6135550124'),
    ('+611900654321', 'https://www.truecaller.com/search/au/1900654321'),
    ('+353209110146', 'https://www.truecaller.com/search/ie/209110146'),
    ('+3655173903', 'https://www.truecaller.com/search/hu/55173903')
)


@pytest.mark.parametrize('inputs, outputs', testcases)
def test_generate_url(inputs, outputs):
    obs = generate_url(parse(inputs, None))
    print(obs)
    assert obs == outputs
