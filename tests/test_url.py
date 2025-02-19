# -*- coding: utf-8 -*-

"""
STATIC WORDPRESS: WordPress as Static Site Generator
A Python Package for Converting WordPress Installation to a Static Website
https://github.com/serpwings/static-wordpress

    tests\test_url.py
    
    Copyright (C) 2020-2025 Faisal Shahzad <info@serpwings.com>

<LICENSE_BLOCK>
The contents of this file are subject to version 3 of the 
GNU General Public License (GPL-3.0). You may not use this file except in
compliance with the License. You may obtain a copy of the License at
https://www.gnu.org/licenses/gpl-3.0.txt
https://github.com/serpwings/static-wordpress/blob/master/LICENSE


Software distributed under the License is distributed on an "AS IS" basis,
WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the
specific language governing rights and limitations under the License.
</LICENSE_BLOCK>
"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++
# INTERNAL IMPORTS
# +++++++++++++++++++++++++++++++++++++++++++++++++++++

from staticwordpress.core.crawler import Crawler
from staticwordpress.core.constants import URL


def test_url_valid():
    my_url = Crawler(loc_="http://staticwp.local", typ_=URL.HOME)
    assert my_url.is_valid == True


def test_url_valid_2():
    my_url = Crawler(loc_="staticwp.local", typ_=URL.HOME)
    assert my_url.is_valid == True


def test_url_valid_3():
    my_url = Crawler(loc_="staticwp", typ_=URL.HOME)
    assert my_url.is_valid == False


def test_url_valid_4():
    my_url = Crawler(loc_="http://staticwp.local/test", typ_=URL.FOLDER)
    assert my_url.is_valid == True
