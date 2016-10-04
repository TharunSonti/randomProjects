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
                #print 'a.string is' 
                #print a.string 
                x = a.string.lower()  #to remove effect of capitals e.g. "INTERN" not being found since we search for "Intern"
                if ('internship' in x) or ('intern ' in x) or ('remote' in x):  #Noticed words start with capital.. 
                    cLink = a['href']  #get the link
                    #if cLink[0] == '/':  #need to append home address to start of this link e.g. /hello is the link we found.. 
                    #    contactString = homepagelink + cLink
                    #    contactLinks.append([contactString, a.string])  #store contact page link + job title
                    #elif homepagelink in cLink:  #website link can be opened as is without editing.. 
                    #    contactLinks[i].append(cLink, a.string)   #store contact page link
                    #elif 'http://www.' not in cLink and 'jobdetail.php?' in cLink: 
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

contactLinks = [['http://jobs.khoslaventures.com/jobdetail.php?jobid=582045', u'Systems Reliability Engineering Internship'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=559705', u'Sales Development Internship UK'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=581760', u'Beyond the Box Score blog manager - Remote'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=581328', u'Principal Consultant, Penetration Testing / Network Security (Remote)'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=466159', u'Security Research Intern (SPEAR)'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=580645', u'Biochemistry Technician- Internship'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=578349', u'Engineering Internship'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=576268', u'Legal Intern - Fall 2016'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=551582', u'Software Engineer - Internship Summer 2017'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=574246', u'Customer Experience - Part Time (SF + NY Remote)'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=574223', u'Internship Opportunities \u2013 Software Development'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=545324', u'Therapist Part Time Remote'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=573634', u'Full Stack Software Engineer (Internship)'], ['http://jobs.khoslaventures.com/jobdetail.php?jobid=573630', u'Data Scientist (Internship)']]
for i in contactLinks:
    print i, '\n'
