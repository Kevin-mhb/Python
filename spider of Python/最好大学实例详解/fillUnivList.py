
def fillUnivList(ulist,html):
	soup=BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds=tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string])