#Find internship by scraping this info from the Khosla ventures careers page 
#(http://jobs.khoslaventures.com/) and automatically searching for the keyword 'internship' on
#all the pages

from bs4 import BeautifulSoup
import urllib2

homepagelink = "http://jobs.khoslaventures.com/"
pageLinks = []
contactLinks = []

link = homepagelink

i = 1
while i < 72: 
    print i, link
    try:
        resp = urllib2.urlopen(link) #open page
            
    except urllib2.HTTPError, e:  #check for error and catch it
        print string + '   failed with error code - %s.' % e.code
        break 
    
    else:
        soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
        for a in soup.findAll('a'): #for each a tag on each link
            if a.string:            #if it has a string                
                if 'Internship' in a.string or 'Intern ' in a.string or 'Remote' in a.string:  #Noticed words start with capital.. 
                    cLink = a['href']  #get the link
                    contactLinks.append([homepagelink + cLink, a.string])
                    #print a.string
                    print contactLinks
                if 'Next' in a.string:
                    link = homepagelink + a['href']
                    pageLinks.append(link)
                    
                #if 'Next' not in a.string:   #wrong condition? since it would trigger for any link on the page??
                #    print 'No more pages left'
                #    break
        i = i + 1
        
print contactLinks, '\n'
#print pageLinks
