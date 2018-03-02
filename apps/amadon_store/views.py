from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	

	return render(request, 'amadon_store/index.html')

def process(request):

	if request.session.get('total_items') == None:
		request.session['total_items'] = 0

	if request.session.get('total_cost') == None:
		request.session['total_cost'] = 0
	
	price = {
		'01': '19.99',
		'02': '29.99',
		'03': '4.99',
		'04': '49.99'
	}

	request.session['produt_id'] = request.POST['product']
	request.session['product_price'] = price[request.POST['product']]
	request.session['product_quantity'] = request.POST['quantity']
	request.session['order_total'] = float(price[request.POST['product']]) * int(request.POST['quantity'])
	
	request.session['total_items'] += int(request.POST['quantity'])
	request.session['total_cost'] += float(price[request.POST['product']]) * int(request.POST['quantity'])

	return redirect('/amadon/checkout')

def checkout(request):
	return render(request, 'amadon_store/checkout.html')

def goback(request):
	request.session.pop('produt_id')
	request.session.pop('product_price')
	request.session.pop('product_quantity')
	request.session.pop('order_total')

	return redirect('/')