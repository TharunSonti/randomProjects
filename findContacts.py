from bs4 import BeautifulSoup
import urllib2

links = ["","",""]  #list of websites to search  #emptied/removed for privacy.. 
# we load the websites and test if they load
#then look for their contact pages
#then look for emails starting with info@, admin@, office@, enquiries@

x = []
y = []
z = [] #stores indices of those links which we couldn't find an email for? 
contactLinks = []

# print links.len fails as does links.len() and links.length()
for n in range(len(links)):  #for each link add an empty list into x and y
    x.append([])
    y.append([])
    contactLinks.append([])
# print x, y
# print '\n'

newLinks = []
i = 0
count = 0 # python doesn't like: count = 0, total = 0 
total = 0

for string in links:  #for each link

    total = total + 1
    # print total
    
    try:
        resp = urllib2.urlopen("http://"+ string) #open homepage
            
    except urllib2.HTTPError, e:  #check for error and catch it
        print string + '   failed with error code - %s.' % e.code
        z.append(i) #store the index in a list of failed links..
        i += 1  

    else: 
        #store the valid links in a new list.. 
        count = count + 1   
        print str(count) +"/" + str(total)
        # print str(count) +"/" + str(total) + "  homepage loads for:" + string

        newLinks.append(string)

# #print "working home page links are: " + newLinks  #silly error - cant add string and list? 
print "working home page links are: "
print newLinks

# every link worked.. # shortcut now
# newLinks = links

#newlinks contains all working/tested homepages..

######Scrape contact page info from home page!  ######

i = -1
failedToFind = []

# when we fail to find a contact link then we end up with an empty list e.g. [["random1"], [], ["random2"]]
#which is a problem later
for string in newLinks:            # for each valid homepage link
    i = i + 1                   # try this at the start of the loop for once/fun
    
    #open homepage
    resp = urllib2.urlopen("http://" + string)

    #used to have a try except else statement here but except without anything afterwards caused error?
    
    soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
    for a in soup.findAll('a'): #for each <a> tag on each link
        if a.string:            #if it has a string
            if 'Contact' in a.string:    #look for the string 'Contact'
                cLink = a['href']
                if cLink[0] == '/' and not contactLinks[i]:  #need to append home address to start of this link e.g. /contact-us is the link we found.. 
                    contactString = string + cLink
                    contactLinks[i].append(contactString)   #store contact page link
                    print contactString 
                elif string in cLink  and not contactLinks[i]:  #website link can be opened as is without editing.. 
                    contactString = string  
                    contactLinks[i].append(contactString)   #store contact page link
                    
                # if contactString not in contactLinks[i]:  # if we haven't already
                # if contactLinks[i] == []:  #if empty then add a link otherwise don't bother? So we essentially only take the first link we find? 
                    # contactLinks[i].append(contactString)   #store contact page link
                    # print "found contact page:" + contactString
                    
            # else:   #prints errors for other links on page too.. not correct check we want
            #     print "failed to find contact page for:" + string
            #     failedToFind.append(string)    #store homepage link for pages we couldn't find contacts page for

    if not contactLinks[i]: #empty list is false #if empty still then print message
        print "failed to find contact page for:" + string
        failedToFind.append(string)    #store homepage link for pages we couldn't find contacts page for

print contactLinks

i = -1 
for string in contactLinks:    #since contactLinks is a list of lists we get each list
    i = i + 1
    #open contactpage
    if string:  #empty list would fail this test..? so only take valid emails..? 
        try:
            resp = urllib2.urlopen("http://" + string[0]) #just take the first link? 
        
        except urllib2.HTTPError, e:
            print string[0] + '   failed with error code - %s.' % e.code
            z.append(i) #add to list of failed links..
            
        else:
            soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
    
            for a in soup.findAll('a'): #for each a tag on each link
                if a.string:
                    if 'info@' in a.string and not x[i]: #only add if we haven't got an email addressy
                        x[i].append(a.string.strip())
                        print a.string
                        # print 'found a url with info in the link'
                        
                    elif 'enquiries@' in a.string and not x[i]:
                        x[i].append(a.string.strip())
                        print a.string
                        # print 'found a url with enquiries in the link'
                        
                    elif 'admin@' in a.string  and not x[i]:
                        x[i].append(a.string.strip())
                        print a.string
                        # print 'found a url with admin the link'
                    
                    elif 'office@' in a.string and not x[i]:
                        x[i].append(a.string.strip())
                        print a.string
                    
                    # else: 
                        # y[i].append(a.string)    
                        # print "didn't find a url"
                        # print "couldn't find "
                        # z.append(i) #don't want this here otherwise for every incorrect link on a page we'd p
            
            if x[i] == []:
                z.append(i)
                print "couldn't find email for: " + string[0]
                
            # print x
            # print y
            # print '\n'    
            
print x
