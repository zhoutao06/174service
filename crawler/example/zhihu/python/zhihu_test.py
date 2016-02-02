#!/usr/bin/python

import sys
import urllib,urllib2




def get_request(url):
	i_headers = {
			"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", 
			"Accept": "text/plain"
			}
	req = urllib2.Request(url, headers=i_headers) 
	try:
		page = urllib2.urlopen(req)
		print page.read()
		print len(page.read()) 
	except urllib2.HTTPError, e:
		print "Error Code:", e.code
	except urllib2.URLError, e: 
		print "Error Reason:", e.reason 

if __name__ == '__main__':
	urls = [
		'https://www.zhihu.com/people/jiu-jian',
		'https://www.zhihu.com/people/lu-si-hao-81/about'
		]
	i_headers = {
			"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5", 
			"Accept": "text/plain"
			}
	for header,v in i_headers.iteritems():
		print header,v
	#get_request(urls[1])