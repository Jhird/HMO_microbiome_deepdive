from bs4 import BeautifulSoup
import urllib
import sys

gene=sys.argv[1]
target_url='www.genecards.org/cgi-bin/carddisp.pl?gene='+gene
txt = urllib.urlopen(target_url).read()
soup = BeautifulSoup(html_doc, 'html.parser').get_text()


