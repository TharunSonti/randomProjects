from bs4 import BeautifulSoup
import mechanize

#started 9:35 pm 24/9/2016

bookslist = []
locations = ['carindale', '']
#url = 'https://elibcat.library.brisbane.qld.gov.au/'
url = 'https://elibcat.library.brisbane.qld.gov.au/uhtbin/cgisirsi/?ps=yJltL1y7Mr/ZZELIBCAT/136260035/60/1308/X'
#http://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

#http://stackoverflow.com/questions/4888463/how-to-install-mechanize-for-python-2-7
#sudo apt-get install python-mechanize


br = mechanize.Browser()
#br.set_all_readonly(False)    # allow everything to be written to
#br.set_handle_robots(False)   # ignore robots
#br.set_handle_refresh(False)  # can sometimes hang without this
#br.addheaders = [('User-agent', 'Firefox')]

response = br.open(url)
print response.read() 

####Get error
#Traceback (most recent call last):
#  File "librarybooks.py", line 22, in <module>
#    response = br.open(url)
#  File "/usr/lib/python2.7/dist-packages/mechanize/_mechanize.py", line 203, in open
#    return self._mech_open(url, data, timeout=timeout)
#  File "/usr/lib/python2.7/dist-packages/mechanize/_mechanize.py", line 255, in _mech_open
#    raise response
#mechanize._response.httperror_seek_wrapper: HTTP Error 403: request disallowed by robots.txt


########meaning i need to run line of code about robots.. 
