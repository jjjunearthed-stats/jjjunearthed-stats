from scrapy import cmdline
import File

File.delete_content("artists.json")
cmdline.execute("scrapy runspider JJJUnearthed/spiders/JJJUnearthedSpider.py -a from_index=4269 -a to_index=4270 -t json -o artists.json".split())
