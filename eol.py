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
