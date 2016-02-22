from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
import requests
import time

oldurl = "https://www.livebelowtheline.com.au/leaderboards/all_participants?page=1"
url = "https://www.livebelowtheline.com.au/leaderboards/all_participants?page="


t0 = time.time() 

html = urlopen(oldurl).read()
soup = BeautifulSoup(html, "lxml")

spans = soup.find_all("span", class_="leader-name")
names = [name.text for name in spans]

#for name in names:
#    print name

names1 = []
names = []
for i in range (1, 62):
    pageURL = url + str(i)
    #print pageURL
    html = urlopen(pageURL).read()
    soup = BeautifulSoup(html, "lxml")
    spans = soup.find_all("span", class_="leader-name")
    names.append([name.text for name in spans])
    #print names[1][1]
    names1 = names1 + [name.text for name in spans]

#for i in names1:
 #   print i
    
#print names[3][0].encode('ascii', 'ignore').decode('ascii')
# print names1.sort() prints none.. screws up due to unicode characters? e.g. accents and stuff??

f = open('output.txt', 'w')
json.dump(names1, f)
f.close()

# for each page 
# open the page
# store names

#print names1
#print 'https://api.genderize.io/?name=' + names1[0]

femaleNames = []
maleNames = []
unknownNames = []

maleTally = 0
femaleTally = 0
unknownTally = 0
total = 0

for name in names1:   #for each name check gender and add to tally
    
    r = requests.get('https://api.genderize.io/?name=' + name)
    #pageText = r.text
    #gender = pageText['gender']    #this fails I guess because this is a string not a dictionary which is what it looks like though..?
    # print pageText # prints this which looks like a dictionary?? {"name":"Georgina","gender":"female","probability":"1.00","count":437}

    #print gender

    # print json.dumps(r.json())  #throws an error?
    # print json.loads(r.json())  #throws an error?
    nameRequest = json.loads(r.text)

    # print nameRequest['gender']   printed female
    gender = nameRequest['gender']

    if gender == 'female':
        femaleTally += 1
        femaleNames.append(name)
    elif gender == 'male':
        maleTally += 1
        maleNames.append(name)
    else: 
        unknownTally += 1
        unknownNames.append(name)

    total += 1
    
#    if total > 9:
#       break

#parsed_json = simplejson.loads(r.json())   didn't work?
# print parsed_json['gender']   

#print 'femaleTally is ' + femaleTally   # this fails.. can't add string and int
print 'femaleTally is', femaleTally 
print 'Their names are:', femaleNames
print '\n'
print 'maleTally is',  maleTally
print 'Their names are:', maleNames
print '\n'
print 'unknownTally is', unknownTally
print 'Their names are:', unknownNames


with open('results.txt', 'w') as f:
    f.write('The Female Tally is ' + str(femaleTally) + '. ')
    f.write('Their names are: ' + str(femaleNames))
    f.write('\n')
    f.write('The Male Tally is ' + str(maleTally) + '. ' )
    f.write('Their names are: ' + str(maleNames))
    f.write('\n')
    f.write('The Unknown Tally is ' + str(unknownTally) + '. ')
    f.write('Their names are: ' + str(unknownNames) + '\n')
    f.write('The total is: ' + str(total))


t1 = time.time()
totalTime = t1-t0
print totalTime
