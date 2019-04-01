var Domain = document.location.origin;
AddControlButtonFunctional();

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
				ProductAmountInput.value = Number(ProductAmountInput.value) + 1;
			} else {
				alert('something went wrong')
			}
		})
}

