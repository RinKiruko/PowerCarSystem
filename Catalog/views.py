import re
from collections import namedtuple
from django.shortcuts import render
from .models import CategoryGroup, Category, Good
from Filtration.models import Filter
from Filtration.views import toFilter

AllGroups = CategoryGroup.objects.all()
AllGoods = Good.objects.all().order_by('PublishedDate')
context = {
    'CategoryGroups': AllGroups,
    'Goods' : AllGoods
}

def getAllGoods(request):
    return render(request, 'Catalog/catalog.html', context)

def getGoodsSortedByGroups(request, group_title):
    RequestedGroup = CategoryGroup.objects.filter(Title=group_title)
    RelatedWithReqGroupCategories = RequestedGroup.categories.all()
    Goods = Good.objects.filter(Category__in=RelatedWithReqGroupCategories)
    
    context['Goods'] = Goods
    return render(request, 'Catalog/catalog.html', context)

def getGoodsSortedByCategory(request, category_title):
    RequestedCategory = Category.objects.filter(Title=category_title)
    CharacteristicsIDs = RequestedCategory.characteristics.all().value('id')
    Filters = Filter.objects.filter(id__in=CharacteristicsIDs)
    Goods = RequestedCategory.goods.all()
    context['Filters'] = Filters
    context['Goods'] = Goods
    return render(request, 'Catalog/catalog.html', context)

def getFilteredGoods(request, group_title, category_title):
    RequestedGroup = Group.objects.get(Title=group_title)
    RequestedCategory = RequestedGroup.objects.get(Title=category_title)
    GoodsToSorted = RequestedCategory.goods.all()
    if request.GET is not None:
        SerializedFilter = namedtuple('Filter',['CharacteristicName','Modificator','LookupValue'])
        GoodLookups = []
        for field_name in request.GET:
            SplittedFieldName= field_name.split('__')            
            if SplittedFieldName[0] == 'Characteristic':
                GoodLookups.append(SerializedFilter(SplittedFieldName[1], 
                                                    SplittedFieldName[2],
                                                    request.GET[field_name]))
        context['Goods'] = toFilter(GoodsToSorted, GoodLookups)
    return render(request, 'Catalog/catalog.html', context)