### usage
# $ python uniprot_parse.py EGFR
# returns all relevant uniprot text and some gibberish
# TODO: if deepdive is confounded by the gibberish, we can parse more carefully with beatifulsoup

from bs4 import BeautifulSoup
import urllib
import sys
import mygene

gene=sys.argv[1]

######
# set manually
justDescription

# query mygene for the uniprot id
mg = mygene.MyGeneInfo()
for q in mg.query(gene,species='human',fields='uniprot')['hits']:
	if 'uniprot' in q.keys():
		uniprot_id = q['uniprot']['Swiss-Prot']
		break
print uniprot_id

# query uniprot for the relevant text
target_url='http://www.uniprot.org/uniprot/'+uniprot_id
txt = urllib.urlopen(target_url).read()
soup = BeautifulSoup(txt, 'html.parser') #.get_text()

if justDescription:
	print soup.find_all('meta',{'name':'description'})
else:
	out=''
	for i in soup.find_all('div',{'class':'annotation','property':'schema:hasPart','typeof':'schema:creativeWork'}):
		out+=i.find_all('span',{'property':'schema:text'})
	print out
