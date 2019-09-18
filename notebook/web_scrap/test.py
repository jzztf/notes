import csv
import requests
from lxml import html

s = requests.Session()
r = s.get("http://learn.onion.net/language=en/35426/w3c-xpath")
tree = html.fromstring(r.text)

text = tree.xpath(
    '//div[@class="innerContent"]/ul/li/a[starts-with(@href, "/language=en/taps")]/text()')
links = tree.xpath(
    '//div[@class="innerContent"]/ul/li/a[starts-with(@href, "/language=en/taps")]/@href')

with open('xx.csv', 'w') as f:
    writer = csv.writer(f)
    for i in zip(text, links):
        writer.writerow(i)
