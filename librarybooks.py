from bs4 import BeautifulSoup
import mechanize

#started 9:35 pm 24/9/2016

bookslist = []


url = 'https://elibcat.library.brisbane.qld.gov.au/uhtbin/cgisirsi/?ps=ohIqbErG80/ZZELIBCAT/1640104/60/1308/X'
#worked but then failed later? 

#I'll have to go to main page then follow the link? 
#url = 'https://elibcat.library.brisbane.qld.gov.au'

#http://stackoverflow.com/questions/4888463/how-to-install-mechanize-for-python-2-7
#sudo apt-get install python-mechanize


print url

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this

response = br.open(url)
#print response.read() 

for link in br.links():
    print link.text, link.url
    
for form in br.forms():
    print "Form name:", form.name
    #print form

#Form name: new_session
#Form name: loginform
#Form name: searchform
#Form name: reset_query_form
#Form name: url_form

#form we want is search form

br.select_form("searchform")

i = 0
for control in br.form.controls:
    i = i+ 1

    if i == 1: 
        control.value = "48 laws of power"
    
    if i == 2:
        control.value = ["TI^TITLE^TITLES^Title Processing^title"]
    
    #so i can load the page with the book then search for the libary name on this page? 
    #if i == 4:
    #    control.value = ["CARINDALE"] 
    
    print control 
    
response = br.submit()
print response.read()

#<TextControl(searchdata1=)>
#<SelectControl(srchfield1=[*GENERAL^SUBJECT^GENERAL^^words or phrase, AU^AUTHOR^AUTHORS^Author Processing^author, TI^TITLE^TITLES^Title Processing^title, SU^SUBJECT^SUBJECTS^^subject, SER^SERIES^TITLES^Title Processing^series, PER^PERTITLE^TITLES^Title Processing^periodical title])>
#<SubmitControl(<None>=Search) (readonly)>
#<SelectControl(library=[*ALL, SALL, ANNERLEY, ARC, ASHGROVE, BANYO, BRACKENRDG, BRISBANE S, BULIMBA, CARINA, CARINDALE, CHERMSIDE, COOPERS PL, CORINDA, EVERTON PA, FAIRFIELD, GARDEN CIT, GRANGE, HAMILTON, HOLLAND PA, INALA, INDOOROOPI, KENMORE, MITCHELTON, MOBILE, MT COOT-TH, MT GRAVATT, MT OMMANEY, NEW FARM, NUNDAH, SANDGATE, STONES COR, SUNNY BANK, TOOWONG, WEST END, WYNNUM, ZILLMERE])>

#print br.form.controls[0].type()    #doesn't work

####error when using single quotes e.g.  'book thief' instead of double quotes?
#Traceback (most recent call last):
#  File "librarybooks3.py", line 44, in <module>
#    control.value = ['the book theif']
#  File "/usr/lib/python2.7/dist-packages/mechanize/_form.py", line 1217, in __setattr__
#    raise TypeError("must assign a string")
#TypeError: must assign a string


    ####error again    turns out double quotes wasn't the problem... expecting a string but we gave list.. ['book thief'] or ["book theif"] is a problem
    # 'book thief'   without the square brackets works..!


####output after correcting errors.. 
#<TextControl(searchdata1=the book theif)>
#<SelectControl(srchfield1=[GENERAL^SUBJECT^GENERAL^^words or phrase, AU^AUTHOR^AUTHORS^Author Processing^author, *TI^TITLE^TITLES^Title Processing^title, SU^SUBJECT^SUBJECTS^^subject, SER^SERIES^TITLES^Title Processing^series, PER^PERTITLE^TITLES^Title Processing^periodical title])>
#<SubmitControl(<None>=Search) (readonly)>
#<SelectControl(library=[ALL, SALL, ANNERLEY, ARC, ASHGROVE, BANYO, BRACKENRDG, BRISBANE S, BULIMBA, CARINA, *CARINDALE, CHERMSIDE, COOPERS PL, CORINDA, EVERTON PA, FAIRFIELD, GARDEN CIT, GRANGE, HAMILTON, HOLLAND PA, INALA, INDOOROOPI, KENMORE, MITCHELTON, MOBILE, MT COOT-TH, MT GRAVATT, MT OMMANEY, NEW FARM, NUNDAH, SANDGATE, STONES COR, SUNNY BANK, TOOWONG, WEST END, WYNNUM, ZILLMERE])>
#<HiddenControl(sort_by=-PBYR) (readonly)>


#* tells us which value is selected (that's what that cheatsheet said and it's true!)
