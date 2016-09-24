from bs4 import BeautifulSoup
import mechanize

#started 9:35 pm 24/9/2016
#http://stackoverflow.com/questions/4888463/how-to-install-mechanize-for-python-2-7
#sudo apt-get install python-mechanize

bookslist = []

url = 'https://elibcat.library.brisbane.qld.gov.au/uhtbin/webcat'

#print url

br = mechanize.Browser()
br.set_handle_robots(False)   # ignore robots
br.set_handle_refresh(False)  # can sometimes hang without this

response = br.open(url)
#print response.read() 

for form in br.forms():
    print "Form name:", form.name

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

#works and follows the url to where it goes  e.g.    https://elibcat.library.brisbane.qld.gov.au/uhtbin/webcat
# redirected to 
# https://elibcat.library.brisbane.qld.gov.au/uhtbin/cgisirsi/?ps=ohIqbErG80/ZZELIBCAT/1640104/60/1308/X

###########OUTPUT that was printed: ####################
#Form name: new_session
#Form name: loginform
#Form name: searchform
#Form name: reset_query_form
#Form name: url_form
#<TextControl(searchdata1=48 laws of power)>
#<SelectControl(srchfield1=[GENERAL^SUBJECT^GENERAL^^words or phrase, AU^AUTHOR^AUTHORS^Author Processing^author, *TI^TITLE^TITLES^Title Processing^title, SU^SUBJECT^SUBJECTS^^subject, SER^SERIES^TITLES^Title Processing^series, PER^PERTITLE^TITLES^Title Processing^periodical title])>
#<SubmitControl(<None>=Search) (readonly)>
#<SelectControl(library=[*ALL, SALL, ANNERLEY, ARC, ASHGROVE, BANYO, BRACKENRDG, BRISBANE S, BULIMBA, CARINA, CARINDALE, CHERMSIDE, COOPERS PL, CORINDA, EVERTON PA, FAIRFIELD, GARDEN CIT, GRANGE, HAMILTON, HOLLAND PA, INALA, INDOOROOPI, KENMORE, MITCHELTON, MOBILE, MT COOT-TH, MT GRAVATT, MT OMMANEY, NEW FARM, NUNDAH, SANDGATE, STONES COR, SUNNY BANK, TOOWONG, WEST END, WYNNUM, ZILLMERE])>
#<HiddenControl(sort_by=-PBYR) (readonly)>

## So redirect worked, form was accessed and modified! 

#print response.read()
