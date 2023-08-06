#-------------------------------------------------------------------------
# Copyright (c) DATA ARTIST
# All rights reserved.
#
# MIT License:
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#--------------------------------------------------------------------------
'''
Created on 2018. 7. 25.

@author: kim
'''

import boto3

import requests
from bs4 import BeautifulSoup
from bs4.builder import _htmlparser

class Scrap ():
    '''
    web scapper
    '''
    def __init__ (self):
        #self.url = url
        self.headers  = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36"}
        
    def test (self) :
        return 'hello Scrap'
    
    def url_scraping(self, url) :
        try:
            html = requests.get(url, headers=self.headers, verify=False, timeout=5)
            #html.encoding = response.apparent_encoding
            if html.status_code == 200 and html is not None:
                return html
            else:
                return 1
            
        except Exception as e:
            return 1
        
    
if  __name__=="__main__" :
    scp = Scrap(
        url = [
            "https://www.amazon.co.jp/gp/bestsellers/electronics/387464011/"
        ],
    )
    ret = scp.url_scraping()
    print(ret)
 
