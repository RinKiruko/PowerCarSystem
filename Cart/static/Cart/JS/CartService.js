var Domain = document.location.origin;

var CartButton = document.getElementById('cart-showCartButton');
CartButton.addEventListener('click', ShowCart);

function ShowCart() {
	if ( document.getElementsByClassName('ProductCartList')[0] != null ) {
		let CartContainer = document.getElementsByClassName('CartContainer')[0];
		SwitchVisibility(CartContainer);
	} else {
		let formdata = new FormData();
		let CSRFTokenInput = document.getElementsByName('csrfmiddlewaretoken')[0];
		formdata.append('csrfmiddlewaretoken', CSRFTokenInput.value);
	
		fetch(Domain + '/cart/getcart/', {
		method : 'POST',
		credentials : 'same-origin',
		body : formdata
		}).then(
			function(response) {
				return response.text();
		}).then(
			function(ResponseText) {
				let CartContainer = document.getElementsByClassName('CartContainer')[0];
				CartContainer.innerHTML = ResponseText;
				AddControlButtonFunctional();

				SwitchVisibility(CartContainer);
		})	
	}	
}

function SwitchVisibility(_element) {
	if (jQuery(_element).hasClass('hidden')) {
		
		jQuery(_element).removeClass('hidden');
		jQuery(_element).addClass('visible');

	} else {

		jQuery(_element).removeClass('visible');
		jQuery(_element).addClass('hidden')
	}
}

function AddControlButtonFunctional() {
	var DeleteButton, DecreaseButton, IncreaseButton;
	DeleteButtons = document.getElementsByClassName('DeleteButton');
	DecreaseButtons = document.getElementsByClassName('DecreaseButton');
	IncreaseButtons = document.getElementsByClassName('IncreaseButton');

	for (let button of DeleteButtons) {
		button.addEventListener('click', DeleteProduct);
	};

	for (let button of DecreaseButtons) {
		button.addEventListener('click', DecreaseProductQuantity);
	};

	for (let button of IncreaseButtons) {
		button.addEventListener('click', IncreaseProductQuantity);
	};
}



function DeleteProduct() {
	let formdata = new FormData();
	let CSRFTokenInput = document.getElementsByName('csrfmiddlewaretoken')[0];
	formdata.append('csrfmiddlewaretoken', CSRFTokenInput.value);

	formdata.append('ProductToDelete', this.value);

	fetch(Domain + '/cart/delete/', {
		method : 'POST',
		credentials : 'same-origin',
		body : formdata
	}).then(
		function(response) {
			if (response.status == 200) {
				alert('Product was deleted')
				return response.text()				
			} else {
				// other magic()
			}
		}).then(
		function (ResponseText) {
			let ProductsQuantityContainer = document.getElementById('cart-productQuantity');
			ProductsQuantityContainer.innerText = ResponseText;
		})
}

function DecreaseProductQuantity() {
	let ProductAmountInput = this.parentElement.children[1];

	let formdata = new FormData();
	let CSRFTokenInput = document.getElementsByName('csrfmiddlewaretoken')[0];
	formdata.append('csrfmiddlewaretoken', CSRFTokenInput.value);

	formdata.append('ProductToDecrease', this.value);

	fetch(Domain + '/cart/decrease/', {
		method : 'POST',
		credentials : 'same-origin',
		body : formdata
	}).then(
		function(response) {
			if (response.status == 200) {				
				let ProductsQuantityContainer = document.getElementById('cart-productQuantity');
				ProductsQuantityContainer.innerText = Number(ProductsQuantityContainer.innerText) - 1
				ProductAmountInput.value = Number(ProductAmountInput.value) - 1;
			} else {
				// other magic()
			}
		})
}

function IncreaseProductQuantity() {
	let ProductAmountInput = this.parentElement.children[1];

	let formdata = new FormData();
	let CSRFTokenInput = document.getElementsByName('csrfmiddlewaretoken')[0];
	formdata.append('csrfmiddlewaretoken', CSRFTokenInput.value);

	formdata.append('ProductToAdd', this.value);

	fetch(Domain + '/cart/add/', {
		method : 'POST',
		credentials : 'same-origin',
		body : formdata
	}).then(
		function(response) {
			if (response.status == 200) {				
				let ProductsQuantityContainer = document.getElementById('cart-productQuantity');
				ProductsQuantityContainer.innerText = Number(ProductsQuantityContainer.innerText) + 1;
				ProductAmountInput.value = Number(ProductAmountInput.value) + 1;
			} else {
				alert('something went wrong')
			}
		})
}

