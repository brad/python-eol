"""
Copyright 2010 Brad Pitcher <bradpitcher@gmail.com>

    This file is part of python-eol.

    python-eol is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    python-eol is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with python-eol.  If not, see <http://www.gnu.org/licenses/>.
"""

import urllib
from xml.dom import minidom

EXEMPLARS_URL = 'http://www.eol.org/exemplars.xml'
SEARCH_URL = 'http://www.eol.org/search.xml?q=%s'
PAGE_URL = 'http://www.eol.org/pages/%i.xml'
IMAGES_URL = 'http://www.eol.org/pages/%i/images/%i.xml'
VIDEOS_URL = 'http://www.eol.org/pages/%i/videos/%i.xml'

class eol:
    def __get_xml_doc(self, url):
        socket = urllib.urlopen(url)
        doc = minidom.parse(socket)
        socket.close()
        return doc

    def exemplars(self):
        return self.__get_xml_doc(EXEMPLARS_URL)

    def search(self, search_term):
        return self.__get_xml_doc(SEARCH_URL % search_term)

    def page(self, page_id):
        return self.__get_xml_doc(PAGE_URL % page_id)

    def images(self, page_id, page_num):
        return self.__get_xml_doc(IMAGES_URL % (page_id, page_num))

    def videos(self, page_id, page_num):
        return self.__get_xml_doc(VIDEOS_URL % (page_id, page_num))
