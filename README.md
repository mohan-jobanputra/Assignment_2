# Assignment 2

Python code to which reads an input file, containing a list of web pages. The Python code should crawl the source code of these web pages and print <URL>,“No” if the page does not contain a Google Analytics code, and print <URL>, “Yes” if the website contains a Google Analytics code.

## Getting Started

Download and clone the repository on to your desktop and UnZip it.

### Prerequisites

Before running the script you need to install a few libraries/packages -

- install bs4 (BeautifulSoup v4)
- install Selenium Webdriver
- install ChromeDriver - WebDriver for Chrome (http://chromedriver.chromium.org/downloads)


### Installing

After successfully installing all the prerequisites for this project open a new terminal window on your desktop and go the directory where you unzipped downloaded repository

To run the script type the following command into your terminal window

```
python assignment_2.py
```

Running this script might take some time and after completion your can see the output in the terminal window itself. the output will be in the format 

```
<URL>,“Yes/No”
```

Example:

```
(base) mJ:~ mJ$ cd Desktop/Convonix_assignments/Assignment_2
(base) mJ:Assignment_2 mJ$ ls
assignment_2.py	urls.txt
(base) mJ:Assignment_2 mJ$ cat urls.txt 
https://kjsieit.somaiya.edu/kjsieit/#
http://www.convonix.com/
http://alumnite.kjsieit.in/
https://www.lohanaboarding.org/
(base) mJ:Assignment_2 mJ$ python assignment_2.py 
https://kjsieit.somaiya.edu/kjsieit/#, Yes
http://www.convonix.com/, Yes
http://alumnite.kjsieit.in/, No
https://www.lohanaboarding.org/, No
```
## Running the tests

You can update the url.txt file with your own set of URLs to check for Google Analytics code.



