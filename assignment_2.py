import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=options)

# reading URLs from urls.txt file and storing it into urls
text_file = open("urls.txt", "r")
urls = text_file.readlines()
text_file.close()

# list of Universal Analytics and Classic Analytics JavaScripts re: https://support.google.com/analytics/answer/1032399?hl=en
script_tags = ['gtag.js', 'analytics.js', 'ga.js']


# iterating through urls one by one
for url in urls:
	url = url.strip()
	browser.get(url)
	ready = False
	while not ready:
		time.sleep(1)
		ready = browser.execute_script('return document.readyState;')
	gaElement = browser.execute_script("return (typeof ga !== 'undefined');")
	if gaElement:
		print(url + "," + str(gaElement))
		continue
	html = browser.page_source
	# parsing the page source code with the help of Beautiful Soup
	soup = BeautifulSoup(html, features="html.parser")
	# finding all scripts from source code of  the web page
	scripts = soup.findAll("script")
	# initializing found tage to flase to use it as flag
	found_tag = False
	# running loop to go through each script for all scripts of each web page
	for script in scripts:
		if not script.has_attr("src"):
			continue
		script_src = script["src"]
		# checking for Google Analytics Script tags
		for tag in script_tags:
			# if tag is found
			found_tag = (script_src.find(tag) != -1)
			if found_tag:
				break
		if found_tag:
				break
	# printing final results
	if found_tag == True:
		print(url + ", Yes")
	else:
		print(url + ", No")