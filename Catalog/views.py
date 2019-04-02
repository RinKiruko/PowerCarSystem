from django.shortcuts import render
from .models import CategoryGroup, Category, Good

AllGroups = CategoryGroup.objects.all()
AllGoods = Good.objects.all().order_by(pub_date)
context = {
    'CategoryGroups': AllGroups,
    'Goods' : AllGoods
}

def getAllGoods(request):
    return render(request, 'Catalog/catalog.html', context=context)

def getGoodsSortedByGroups(request, group_title):
    RequestedGroup = CategoryGroup.objects.filter(Title=group_title)
    RelatedWithReqGroupCategories = RequestedGroup.categories.all()
    Goods = Good.objects.filter(Category__in=RelatedWithReqGroupCategories
    
    context['Goods'] = Goods
    return render(request, 'Catalog/catalog.html', context=context)

def getGoodsSortedByCategory(request, category_title):
    RequestedCategory = Category.objects.filter(Title=category_title)
    Goods = RequestedCategory.goods.all()

    context['Goods'] = Goods