from bs4 import BeautifulSoup
import re

filev = open("file",'r')
new_soup = BeautifulSoup(filev.read())

for links in new_soup.find_all('a',href=re.compile('forcedownload')):
	link_to_file = links['href']
	index_last_slash = link_to_file.rindex('/')
	index_last_ques = link_to_file.rindex('?')
	text = link_to_file[(1 + index_last_slash):index_last_ques]
	text = str(text.replace('/','|'))
	print link_to_file, '||', text