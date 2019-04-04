from Catalog.models import Good, Attribute
from Filtration.models import Filter
from collections import namedtuple


def createFilterFromGETQueryDict(GETQueryDict):
	ResultFiltersCollection = []
	SerializedFilter = namedtuple('Filter',['CharacteristicName',
											'Modificator',
											'LookupValue'])
	for field_name in GETQueryDict:
		SplittedFieldName= field_name.split('__')            
		if SplittedFieldName[0] == 'Characteristic':
		ResultFiltersCollection.append(SerializedFilter(SplittedFieldName[1],
												SplittedFieldName[2],
												request.GET[field_name]))

def toFilter(goods, conditions):
    ResultQuery = goods
    Lookups = 
    for condition in conditions: #condition is namedtuple('Filter',[CharacteristicName,Modificator,LookupValue])
        ResultQuery.filter()
    