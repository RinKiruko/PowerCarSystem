from Catalog.models import Good, Attribute
from Filtration.models import Filter

def createFilterFromQueryDict(GETQueryDict)
def toFilter(goods, conditions):
    ResultQuery = goods
    Lookups = 
    for condition in conditions: #condition is namedtuple('Filter',[CharacteristicName,Modificator,LookupValue])
        ResultQuery.filter()
    