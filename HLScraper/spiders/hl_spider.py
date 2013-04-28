from scrapy.contrib.spiders.crawl import Rule, CrawlSpider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from HLScraper.items import HlscraperItem
from scrapy.selector.lxmlsel import HtmlXPathSelector

#     def parse(self, response):
#         filename = response.url.split("/")[-2]
#         open(filename, 'wb').write(response.body)
class HLSpider(CrawlSpider):
    name = "hl"
    allowed_domains = ["hl.co.uk"]
    start_urls = [
        "http://www.hl.co.uk/funds/fund-discounts,-prices--and--factsheets/search-results?is150=true"
#         "http://www.hl.co.uk/funds/fund-discounts,-prices--and--factsheets/search-results"
    ]
    
    rules = [Rule(SgmlLinkExtractor(allow=['/funds/fund-discounts,-prices--and--factsheets/search-results/'], deny=['charts$', 'invest$', 'tab=']), 'parse_fund')]
    

    def parse_fund(self, response):
        x = HtmlXPathSelector(response)
        
        fund = HlscraperItem()
        fund['Url'] = response.url
        fund['Name'] = x.select("normalize-space(/html/body/div[@id='container']/div[@id='content']/div[@class='spacer-left-dbl']/div[@id='fund-section-content']/div[@class='spacer-bottom']/div[@id='security-title']/h1[@class='underline']/text())").extract()
        fund['ExdividendDate'] = x.select("normalize-space(//tr/th[text()[contains(., 'Ex-dividend date')]]/../td/text())").extract()
        fund['PaymentDate'] = x.select("normalize-space(//tr/th[text()[contains(., 'Payment date')]]/../td/text())").extract()
        fund['RunningYield'] = x.select("normalize-space(//tr/th[text()[contains(., 'Running yield')]]/../td/text())").extract()
        fund['HistoricYield'] = x.select("normalize-space(//tr/th[text()[contains(., 'Historic yield')]]/../td/text())").extract()
        fund['IncomePaid'] = x.select("normalize-space(//tr/th[text()[contains(., 'Income paid')]]/../td/text())").extract()
        fund['TypeOfPayment'] = x.select("normalize-space(//tr/th[text()[contains(., 'Type of payment')]]/../td/text())").extract()
        fund['LaunchDate'] = x.select("normalize-space(//tr/th[text()[contains(., 'Launch date')]]/../td/text())").extract()
        fund['Sector'] = x.select("normalize-space(//tr/th[text()[contains(., 'Sector')]]/../td/text())").extract()
        fund['FundSize'] = x.select("normalize-space(//tr/th[text()[contains(., 'Fund size')]]/../td/text())").extract()
        fund['NumberOfHoldings'] = x.select("normalize-space(//tr/th[text()[contains(., 'Number of holdings')]]/../td/text())").extract()
        fund['TypeOfUnits'] = x.select("normalize-space(//tr/th[text()[contains(., 'Type of units')]]/../td/text())").extract()
        fund['FundType'] = x.select("normalize-space(//tr/th[text()[contains(., 'Fund type')]]/../td/text())").extract()
        fund['NetInitialCharge'] = x.select("normalize-space(//tr/th[text()[contains(., 'Net initial charge')]]/../td/text())").extract()
        fund['NetAnnualCharge'] = x.select("normalize-space(//tr/th[text()[contains(., 'Net Annual charge')]]/../td/text())").extract()
        fund['OtherExpenses'] = x.select("normalize-space(//tr/th[text()[contains(., \"Fund manager's other expenses\")]]/../td/text())").extract()
        fund['PerformanceFee'] = x.select("normalize-space(//tr/th[text()[contains(., 'Performance fee')]]/../td/text())").extract()
        fund['PlatformFee'] = x.select("normalize-space(//tr/th[text()[contains(., 'HL Platform charge')]]/../td/text())").extract()
        
        fund['Wealth150'] = x.select("/html/body/div[@id='container']/div[@id='content']/div[@class='spacer-left-dbl']/div[@id='fund-section-content']/div[@class='spacer-bottom']/div[@id='security-title']/h1[@class='underline']/a/img/@src").extract()

        return fund