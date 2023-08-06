from __future__ import print_function

import asyncio
import math
import random
from collections import defaultdict
from xml.etree import cElementTree as ET

import aiohttp
import async_timeout


class Rule34_Error(Exception):
    """Rule34 rejected you"""
    def __init__(self, message, *args):
        self.message = message
        super(Rule34_Error, self).__init__(message, *args)


class Request_Rejected(Exception):
    """The Rule34 API wrapper rejected your request"""
    def __init__(self, message, *args):
        self.message = message
        super(Request_Rejected, self).__init__(message, *args)


class SelfTest_Failed(Exception):
    """The self test failed"""
    def __init__(self, message, *args):
        self.message = message
        super(SelfTest_Failed, self).__init__(message, *args)


class Rule34:
    def __init__(self, loop, timeout=10):
        """
        :param loop: the event loop
        :param timeout: how long requests are allowed to run until timing out
        """
        self.session = aiohttp.ClientSession(loop=loop)
        self.timeout = timeout
        self.loop = loop

    def ParseXML(self, rawXML):
        """Parses entities as well as attributes following this XML-to-JSON "specification"
            Using https://stackoverflow.com/a/10077069"""
        if "Search error: API limited due to abuse" in str(rawXML.items()):
            raise Rule34_Error('Rule34 rejected your request due to "API abuse"')

        d = {rawXML.tag: {} if rawXML.attrib else None}
        children = list(rawXML)
        if children:
            dd = defaultdict(list)
            for dc in map(self.ParseXML, children):
                for k, v in dc.items():
                    dd[k].append(v)
            d = {rawXML.tag: {k: v[0] if len(v) == 1 else v for k, v in dd.items()}}
        if rawXML.attrib:
            d[rawXML.tag].update(('@' + k, v) for k, v in rawXML.attrib.items())
        if rawXML.text:
            text = rawXML.text.strip()
            if children or rawXML.attrib:
                if text:
                    d[rawXML.tag]['#text'] = text
            else:
                d[rawXML.tag] = text
        return d

    @staticmethod
    def urlGen(tags=None, limit=None, id=None, PID=None, deleted=None, **kwargs):
        """Generates a URL to access the api using your input:
        :param tags: str ||The tags to search for. Any tag combination that works on the web site will work here. This includes all the meta-tags
        :param limit: str ||How many posts you want to retrieve
        :param id: int ||The post id.
        :param PID: int ||The page number.
        :param deleted: bool||If True, deleted posts will be included in the data
        :param kwargs:
        :return: url string, or None
        All arguments that accept strings *can* accept int, but strings are recommended
        If none of these arguments are passed, None will be returned
        """
        # I have no intentions of adding "&last_id=" simply because its response can easily be massive, and all it returns is ``<post deleted="[ID]" md5="[String]"/>`` which has no use as far as im aware
        URL = "https://rule34.xxx/index.php?page=dapi&s=post&q=index"
        if PID != None:
            if PID > 2000:
                raise Request_Rejected("Rule34 will reject PIDs over 2000")
            URL += "&pid={}".format(PID)
        if limit != None:
            URL += "&limit={}".format(limit)
        if id != None:
            URL += "&id={}".format(id)
        if tags != None:
            tags = str(tags).replace(" ", "+")
            URL += "&tags={}".format(tags)
        if deleted == True:
            URL += "&deleted=show"
        if PID != None or limit != None or id != None or tags != None:
            return URL + "&rating:explicit"
        else:
            return None

    async def totalImages(self, tags):
        """Returns the total amount of images for the tag
        :param tags:
        :return: int
        """
        if self.session.closed:
            self.session = aiohttp.ClientSession(loop=self.loop)
        with async_timeout.timeout(10):
            url = self.urlGen(tags=tags, PID=0)
            async with self.session.get(url=url) as XMLData:
                XMLData = await XMLData.read()
                XMLData = ET.XML(XMLData)
                XML = self.ParseXML(XMLData)
            return int(XML['posts']['@count'])
        return None

    async def getImageURLS(self, tags, fuzzy=False, singlePage=True, randomPID=True, OverridePID=None):
        """gatherrs a list of image URLS
        :param tags: the tags youre searching
        :param fuzzy: enable or disable fuzzy search, default disabled
        :param singlePage: when enabled, limits the search to one page (100 images), default disabled
        :param randomPID: when enabled, a random pageID is used, if singlePage is disabled, this is disabled
        :param OverridePID: Allows you to specify a PID
        :return: list
        """
        if self.session.closed:
            self.session = aiohttp.ClientSession(loop=self.loop)
        if fuzzy:
            tags = tags.split(" ")
            for tag in tags:
                tag = tag + "~"
            temp = " "
            tags = temp.join(tags)
        if randomPID is True and singlePage is False:
            randomPID = False
        num = await self.totalImages(tags)
        if num != 0:
            if OverridePID is not None:
                if OverridePID >2000:
                    raise Request_Rejected("Rule34 will reject PIDs over 2000")
            elif randomPID:
                maxPID = 2000
                if math.floor(num/100) < maxPID:
                    maxPID = math.floor(num/100)
                PID = random.randint(0, maxPID)
            else:
                PID = 0
            imgList = []
            XML = None
            t = True
            tempURL = self.urlGen(tags=tags, PID=PID)
            while t:
                with async_timeout.timeout(10):
                    async with self.session.get(url=tempURL) as XML:
                        XML = await XML.read()
                        XML = ET.XML(XML)
                        XML = self.ParseXML(XML)
                if XML is None:
                    return None
                if len(imgList) >= int(XML['posts']['@count']):  # "if we're out of images to process"
                    t = False  # "end the loop"
                else:
                    for data in XML['posts']['post']:
                        imgList.append(str(data['@file_url']))
                if singlePage:
                    self.session.close()
                    return imgList
                PID += 1
            self.session.close()
            return imgList
        else:
            self.session.close()
            return None
    
    async def getPostData(self, PostID):
        """Returns a dict with all the information available about the post
        :param PostID: The ID of the post
        :return: dict
        """
        if self.session.closed:
            self.session = aiohttp.ClientSession(loop=self.loop)
        url = self.urlGen(id=str(PostID))
        XML =None
        with async_timeout.timeout(10):
            async with self.session.get(url=url) as XML:
                XML = await XML.read()
            self.session.close()
            XML = self.ParseXML(ET.XML(XML))
            data = XML['posts']['post']
            return data
        return None


def selfTest():
    """
    Self tests the script for travis-ci
    """
    loop = asyncio.get_event_loop()
    failed = False
    for i in range(25):
        try:
            r34 = Rule34(loop)
            data = loop.run_until_complete(r34.getImageURLS("straight", singlePage=True))
            if data is not None and len(data) != 0:
                print("Passed run {} with {} images{}".format(i+1, len(data), " "*20), end="\r")
            else:
                failed = True
        except Exception as e:
            loop.close()
            raise SelfTest_Failed("Automated self test failed with this error:\n{}".format(e))
    if failed:
        raise SelfTest_Failed("Automated self test failed to gather images")
    else:
        print("Self Test Passed" + " "*20)
        exit(0)
    exit(1)



if __name__ == "__main__":
    try:
        selfTest()
    except Exception as e:
        print(e)
        exit(1)
