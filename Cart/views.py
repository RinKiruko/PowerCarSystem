from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
import json
from Catalog.models import Good
from Order.forms import IndividualOrderForm
from Order.forms import OrganizationOrderForm

def add_product(request):
	if 'CART' in request.session:
		Cart = request.session['CART']
		


		# Cart Structure: {
		# 	'ProductsQuantity': quantity-int,
		# 	'Products': {
		# 		'ProductID 1': quantity-int,
		# 		'ProductID 2': quantity-int,
		# 		'ProductID 3': quantity-int,
		# 		'ProductID 4': quantity-int,
		# 		...
		# 		'ProductID n': quantity-int,
		# 	}
		# }
		

		ProductToAddId = request.POST['ProductToAdd']

		if ProductToAddId in Cart['Products']:
			Cart['Products'][ProductToAddId] += 1			
			Cart['ProductsQuantity'] += 1

			request.session['CART'] = Cart
			
			return HttpResponseRedirect(settings.GENERIC_URL + 'catalog')
		else:
			Cart['Products'][ProductToAddId] = 1
			Cart['ProductsQuantity'] += 1

			request.session['CART'] = Cart
			
			return HttpResponseRedirect(settings.GENERIC_URL + 'catalog')
	else:
		Cart = {}
		ProductToAddId = request.POST['ProductToAdd']	
		
		Cart['ProductsQuantity'] = 1
		Cart['Products'] = { ProductToAddId : 1 }

		request.session['CART'] = Cart
		
		return HttpResponseRedirect(settings.GENERIC_URL + 'catalog')
	
def set_quantity(request):
	if 'CART' in request.session:
		Cart = request.sesion['CART']

		ProductForChangingQuantity = request.POST['TargetProduct']
		NewTargetProductQuantity = request.POST['NewQuantity']
		OldTargetProductQuantity = Cart['Products'][ProductForChangingQuantity]		
		
		TotalProductsQuantity = Cart['ProductsQuantity']

		NewTotalProductQuantity = TotalProductsQuantity - OldTargetProductQuantity + NewTargetProductQuantity
		Cart['Products'][ProductForChangingQuantity] = NewTargetProductQuantity
		request.session[CART] = Cart
	return render(request, status=200)

def decrease_quantity(request):
	Cart = request.session['CART']
	
	ProductForDecreaseQuantity = request.POST['ProductToDecrease']
	Cart['Products'][ProductForDecreaseQuantity] -= 1
	Cart['ProductsQuantity'] -= 1
	request.session['CART'] = Cart
	return HttpResponse(request, status=200)


def delete_product(request):
	Cart = request.session['CART']
	ProductToDelete = request.POST['ProductToDelete']
	
	Cart['ProductsQuantity'] -= Cart['Products'][ProductToDelete]
	del Cart['Products'][ProductToDelete]
	
	request.session['CART'] = Cart

	return HttpResponse(content=str(Cart['ProductsQuantity']))


def get_cart(request):
	if 'CART' in request.session:
		Cart = request.session['CART']

		ShoppingList = [( Good.objects.get(pk=int(product_id)), product_quantity) 
							for product_id, product_quantity in Cart['Products'].items()]

		context = {
			'ShoppingList': ShoppingList,
			'ProductsQuantity': Cart['ProductsQuantity']
		}
	else:
		context = {}		
	return render(request, 'Cart/CartAsUl.html', context)


def GetFullCartPage(request):
	if 'CART' in request.session:
		context={}
		Cart = request.session['CART']
		
		if 'USER' in request.session:
			UserInformation = Account.objects.get(pk = request.session['User']).values(
																		'FirstName',
																		'MiddleName',
																		'LastName',
																		'OrganizationName',
																		'Email',
																		'PhoneNumber',
																		'DeliveryAddress',
																		'AccountType')
			if UserInformation.AccountType == 'Individual':
				CustomerInformation = {
					'FirstName': UserInformation['FirstName'],
					'MiddleName': UserInformation['MiddleName'],
					'LastName':UserInformation['LastName'],
					'Email':UserInformation['Email'],
					'PhoneNumber':UserInformation['PhoneNumber'],
					'DeliveryAddress':UserInformation['DeliveryAddress'],
				}
				OrderForm = IndividualOrderForm(CustomerInformation)
			else:
				CustomerInformation = {
					'FirstName':UserInformation['FirstName'],
					'MiddleName':UserInformation['MiddleName'],
					'LastName':UserInformation['LastName'],
					'OrganizationName':UserInformation['OrganizationName'],
					'Email': UserInformation['Email'],
					'PhoneNumber': UserInformation['PhoneNumber'],
					'DeliveryAddress': UserInformation['DeliveryAddress']
				}
				OrderForm = OrganizationOrderForm(CustomerInformation)
			context['OrderForm'] = OrderForm.as_ul()
			context['AccountType'] = UserInformation['AccountType']
		else:
			context['IndividualOrderForm'] = IndividualOrderForm().as_ul()
			context['OrganizationOrderForm'] = OrganizationOrderForm().as_ul()

		ShoppingList = []
		for product_id in Cart['Products']:
			product = Good.objects.get(pk=int(product_id))
			quantity = Cart['Products'][product_id]
			position_price = product.price * quantity
			ShoppingList.append((product, quantity, position_price))
		if 'USER' in request.session:
			User = User.objects.get(pk == request.session['USER'])
		print(ShoppingList)
		context['ShoppingList'] = ShoppingList

		return render(request, 'Cart/FullCartPage.html', context)
	else:
		return render(request, 'Cart/FullCartPage.html')