import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
response = br.open("http://moodle.iitb.ac.in/login/index.php")
#print response.read(),'\n'
br.form = list(br.forms())[0]
#br.select_form('login')
br.form['username'] = 'pradyot'
br.form['password'] = 'M3+hegammafreak'
response1 = br.submit()
response2 = br.open('http://moodle.iitb.ac.in/mod/folder/view.php?id=22975')
new_soup = BeautifulSoup(response2.read())
print new_soup
# for img in new_soup.find_all('img',alt='File'):
# 	link_to_file = img.parent['href']
# 	text = img.find_next('span').string
# 	print text, link_to_file
