# Scrapy settings for HLScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'HLScraper'

SPIDER_MODULES = ['HLScraper.spiders']
NEWSPIDER_MODULE = 'HLScraper.spiders'
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 543,
# }


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'HLScraper (+http://www.yourdomain.com)'
