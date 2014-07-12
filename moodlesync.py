import mechanize, os, re
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("http://moodle.iitb.ac.in/login/index.php")
br.form = list(br.forms())[0]
br.form['username'] = raw_input('Username')
br.form['password'] = raw_input('Password')
soup = BeautifulSoup(br.submit().read())
for h3 in soup.find_all('h3'):
	string = str(h3.string)
	new_soup = BeautifulSoup(br.open(h3.a['href']).read())
	for img in new_soup.find_all('img',alt='File'):
		link_to_file = img.parent['href']
		new_new_soup = BeautifulSoup(br.open(link_to_file).read())
		link_to_file = new_new_soup.find('object')['data']
		text = repr(img.next_element.next_element)
		index = 1 + text.index('>')
		text = text[index:]
		index = text.index('<')
		extension = link_to_file[(1 + link_to_file.rindex('.')):]
		text = text[:index]+'.'+extension
		text = str(text.replace('/','|'))
		try:
			os.makedirs('/home/pradyot/Documents/Moodle/'+string+'/',0755)
		except OSError, e:
			if (e.errno != 17):
				pass
		save_as = '/home/pradyot/Documents/Moodle/'+string+'/'+text
		br.retrieve(link_to_file,save_as)[0]
	
	for folder in new_soup.find_all('a',href=re.compile('folder')):
		link_to_folder = folder['href']
		new_new_soup = BeautifulSoup(br.open(link_to_folder).read())
		for links in new_new_soup.find_all('a',href=re.compile('forcedownload')):
			link_to_file = links['href']
			index_last_slash = link_to_file.rindex('/')
			index_last_ques = link_to_file.rindex('?')
			text = link_to_file[(1 + index_last_slash):index_last_ques]
			text = str(text.replace('/','|'))
			try:
				os.makedirs('/home/pradyot/Documents/Moodle/'+string+'/',0755)
			except OSError, e:
				if (e.errno != 17):
					pass
			save_as = '/home/pradyot/Documents/Moodle/'+string+'/'+text
			br.retrieve(link_to_file,save_as)[0]