import File
from scrapy import cmdline

File.delete_content("artists.json")
cmdline.execute("scrapy runspider JJJUnearthedSpider.py -t json -o artists.json".split())