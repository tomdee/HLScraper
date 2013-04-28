# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class HlscraperItem(Item):
    # define the fields for your item here like:
    Url = Field()
    Name = Field()
    ExdividendDate = Field()
    NetAnnualCharge = Field()
    NetInitialCharge = Field()
    PaymentDate = Field()
    RunningYield = Field()
    HistoricYield = Field()
    IncomePaid = Field()
    TypeOfPayment = Field()
    LaunchDate = Field()
    Sector = Field()
    FundSize = Field()
    NumberOfHoldings = Field()
    TypeOfUnits = Field()
    FundType = Field()
    Wealth150 = Field()
    OtherExpenses = Field()
    PerformanceFee = Field()
    PlatformFee = Field()
    pass
