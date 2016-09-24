from bs4 import BeautifulSoup
import mechanize

#started 9:35 pm 24/9/2016

bookslist = []
locations = ['carindale', '']
#url = 'https://elibcat.library.brisbane.qld.gov.au/'
#url = 'https://elibcat.library.brisbane.qld.gov.au/uhtbin/cgisirsi/?ps=yJltL1y7Mr/ZZELIBCAT/136260035/60/1308/X'  #didn't work - just hung for a little while and i couldn't be bothered waiting?
#http://www.pythonforbeginners.com/cheatsheet/python-mechanize-cheat-sheet

url = 'https://www.google.com'   #worked -form on this loaded. 

#http://stackoverflow.com/questions/4888463/how-to-install-mechanize-for-python-2-7
#sudo apt-get install python-mechanize


br = mechanize.Browser()

####accidentally pasted this line 
#br.set_all_readonly(False)    # allow everything to be written to   
####causes error
#### AttributeError: mechanize._mechanize.Browser instance has no attribute set_all_readonly (perhaps you forgot to .select_form()?)

#br.set_handle_robots(False)   # ignore robots
#get this error if I forget this for google.com
Traceback (most recent call last):
  File "librarybooks1.py", line 30, in <module>
    response = br.open(url)
  File "/usr/lib/python2.7/dist-packages/mechanize/_mechanize.py", line 203, in open
    return self._mech_open(url, data, timeout=timeout)
  File "/usr/lib/python2.7/dist-packages/mechanize/_mechanize.py", line 255, in _mech_open
    raise response
mechanize._response.httperror_seek_wrapper: HTTP Error 403: request disallowed by robots.txt


response = br.open(url)

#print response.read() 

for form in br.forms():
    print "Form name:", form.name
    print form
