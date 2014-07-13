#!/usr/bin/python
import mechanize
from getpass import getpass
from os import makedirs,path
from re import compile
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
try:
	response = br.open("http://moodle.iitb.ac.in/login/index.php")
except:
	print 'Unable to connect to moodle. Check internet connection.'
	exit(1)
br.form = list(br.forms())[0]
br.form['username'] = raw_input('Moodle username: ')
br.form['password'] = getpass('Moodle password: ')
soup = BeautifulSoup(br.submit().read())
for h3 in soup.find_all('h3'):
	string = str(h3.string)
	try:
		new_soup = BeautifulSoup(br.open(h3.a['href']).read())
	except:
		print 'Unable to connect to moodle. Check internet connection.'
	for img in new_soup.find_all('img',alt='File'):
		link_to_file = img.parent['href']
		try:
			new_new_soup = BeautifulSoup(br.open(link_to_file).read())
		except:
			print 'Unable to connect to moodle. Check internet connection.'
		link_to_file = new_new_soup.find('object')['data']
		text = repr(img.next_element.next_element)
		index = 1 + text.index('>')
		text = text[index:]
		index = text.index('<')
		extension = link_to_file[(1 + link_to_file.rindex('.')):]
		text = text[:index]+'.'+extension
		text = str(text.replace('/','|'))
		try:
			makedirs('/home/pradyot/Documents/Moodle/'+string+'/',0755)
		except OSError, e:
			if (e.errno != 17):
				pass
		save_as = '/home/pradyot/Documents/Moodle/'+string+'/'+text
		try:
			if(not(path.exists(save_as))):
				br.retrieve(link_to_file,save_as)[0]
		except:
			print text+' not downloaded'
	
	for folder in new_soup.find_all('a',href=compile('folder')):
		link_to_folder = folder['href']
		try:
			new_new_soup = BeautifulSoup(br.open(link_to_folder).read())
		except:
			print 'Unable to connect to moodle. Check internet connection.'
		for links in new_new_soup.find_all('a',href=compile('forcedownload=')):
			link_to_file = links['href']
			index_last_slash = link_to_file.rindex('/')
			index_last_ques = link_to_file.rindex('?')
			text = link_to_file[(1 + index_last_slash):index_last_ques]
			text = str(text.replace('/','|'))
			text = str(text.replace('%20',' '))
			try:
				makedirs('/home/pradyot/Documents/Moodle/'+string+'/',0755)
			except OSError, e:
				if (e.errno != 17):
					pass
			save_as = '/home/pradyot/Documents/Moodle/'+string+'/'+text
			try:
				if(not(path.exists(save_as))):
					br.retrieve(link_to_file,save_as)[0]
			except:
					print text+' not downloaded'