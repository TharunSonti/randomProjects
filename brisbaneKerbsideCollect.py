from bs4 import BeautifulSoup
from urllib2 import urlopen
import json
import requests
from selenium.webdriver import Chrome

url = "http://www.brisbane.qld.gov.au/environment-waste/rubbish-tips-bins/rubbish-collections/kerbside-collection"

#helpful link! http://stackoverflow.com/questions/19392466/python-beautifulsoup-get-select-value-not-text

#New info found on 3/11/2016!
# try http://www.aus-emaps.com/postcode_finder.php    #overlays suburb boundaries on google maps! just have to enter in postcode! 
#found the link on this page http://www.aus-emaps.com/postcode_finder.php  after searching google for 'Brisbane suburb boundaries'

html = urlopen(url).read()
soup = BeautifulSoup(html, "lxml")

spans = soup.find_all("option")
#print spans
suburb = [name.text for name in spans]
suburb.pop(0)
#print suburb.pop(0) + '\n'
# print suburb + '\n'  # can't just randomly add a list to a new line silly
#print suburb
#print '\n'

date = [name['value'] for name in spans]
date.pop(0)
# print date.pop(0) +  '/n'   #wrong slash direction.. rookie error
#print date.pop(0) + '\n'
#print date 
#print '\n'

for i in range(len(suburb)):
    print '#' + str(i) + ' Suburb is ' + suburb[i] + ' date is: ' + date[i]
    

#googleURL = "https://www.google.com.au/maps/place/Coorparoo+Brisbane"
mapsURL = "https://www.google.com.au/maps/place/"  

browser = Chrome()

for i in range(len(suburb)):
    googleURL = mapsURL + suburb[i] +'+Brisbane' 
    filename = fileNum + str(i)
    try:
        browser.get(googleURL)
        browser.get_screenshot_as_file(filename)

finally:
    browser.quit()
