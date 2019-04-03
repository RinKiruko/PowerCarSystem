from django.shortcuts import render
from .models import CategoryGroup, Category, Good
from Filtration.models import Filter
from Filtration.views import filter_goods


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
    RequestedCategory = RequestedGroup.categories.filter(Title=category_title)
    RelatedGoodsWithReqCategory = RequestedCategory.goods.all()
    if request.GET is not None:
        Filters= request.GET.copy()
        Goods = filter_goods(**Filters)
        context['Goods'] = Goods
    return render(request, 'Catalog/catalog.html', context)