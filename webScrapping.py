import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

#step1: Get the HTML
r = requests.get(url)
htmlContent = r.content
#print(htmlContent)

#step 2: parse the html
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#step 3: HTML tree traversal
#commonly used objects : 1.Tag 2. NavigableString 3. BeautifulSoup 4. Comment
title = soup.title
#print(title)
#print(type(title))
#print(type(title.string))
#print(type(soup))

# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
#print(paras)

#Get first element in the HTML page
#print(soup.find('p'))

#Get classes of any elements in the HTML page
print(soup.find('p') ['class'])
#print(soup.find('p') ['id'])

#find all the elements with class lead
#print(soup.find_all('p', class_ = 'lead'))

#comment
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
#print(soup2.p)  #paragraphs

#print(soup2.p.string)
#print(type(soup2.p.string))

# Get the text from the tags/ soup
#print(soup.find('p').get_text())
#print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
#print(anchors)

all_links = set()

# Get all the anchor tags from the page
for link in anchors:
	#print(link.get('href')) 
	if(link.get('href') != '#'):
		linkText = "https://codewithharry.com" +link.get('href')
		all_links.add(link)
		#print(linkText)

navbarSupportedContent = soup.find(id = 'navbarSupportedContent')
#print(navbarSupportedContent)
#print(navbarSupportedContent.children)
#print(navbarSupportedContent.contents)

# .contents - A tag's contents are available as a list, can be stored in memory.
# .children - A tag's children are available as a generator, can't be stored in memory, but you can iterate through the list and get the elements.
#NOTE: if you are working with small web pages and using a for loop, then .content and .children works same.

#for elem in navbarSupportedContent.contents:
#	print(elem)

#for elem in navbarSupportedContent.children:
#	print(elem)

#for item in navbarSupportedContent.strings:
#	print(item)

#for item in navbarSupportedContent.stripped_strings:
#	print(item)

#print(navbarSupportedContent.parent)

#print(navbarSupportedContent.parents)

#for item in navbarSupportedContent.parents:
#	#print(item)
#	print(item.name)

#print(navbarSupportedContent.next_sibling.next_sibling)

#print(navbarSupportedContent.previous_sibling.previous_sibling)

#print(navbarSupportedContent.next_sibling)

#print(navbarSupportedContent.previous_sibling)

# # means selector
#elem =  soup.select('#loginModal')
#print(elem)

# . means class
#elem =  soup.select('.loginModal')
#print(elem)

#elem =  soup.select('.modal-footer')
#print(elem)