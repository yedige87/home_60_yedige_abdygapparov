from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from shop_app.forms import ProductForm, BasketForm
from shop_app.models import Basket, Customer, Order
from shop_app.models.products import Product, CategoryChoice




class Product_Detail(DetailView):
    template_name = 'product_view.html'
    model = Product


class ProductCreateView(CreateView):
    template_name = 'product_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'product_edit.html'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse('product_view', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'product_confirm_delete.html'
    model = Product
    success_url = reverse_lazy('index')


def check_product(request, pk):
    client_id = 1
    product = Product.objects.get(pk=pk)
    customer = Customer.objects.get(pk=client_id)

    try:
        basket = get_object_or_404(Basket, product_id=pk)
    except BaseException:
        basket = Basket.objects.create()
        basket.product_id = pk
        basket.customer_id = client_id
        basket.type = 2
        basket.price = product.price
        basket.title = product.title
    basket.qty_prod = product.qty
    basket.qty_old = basket.qty
    basket.save()
    clients = Basket.objects.filter(type=3)
    if not clients:
        client = Basket.objects.create()
        client.type = 3
        client.title = customer.name
        client.qty_old = 1
        client.customer_id = client_id
        client.save()

        client = Basket.objects.create()
        client.type = 3
        client.title = customer.phone
        client.qty_old = 2
        client.customer_id = client_id
        client.save()

        client = Basket.objects.create()
        client.type = 3
        client.title = customer.address
        client.qty_old = 3
        client.customer_id = client_id
        client.save()

    return redirect(f'/basket_add/{basket.pk}')


class BasketAddView(UpdateView):
    template_name = 'basket_add.html'
    form_class = BasketForm
    model = Basket

    def get_success_url(self):
        return reverse('change_product', kwargs={'pk': self.object.pk})


def change_product(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.amount = basket.price * basket.qty
    basket.save()
    diff_qty = basket.qty - basket.qty_old
    total_amount = 0
    baskets = Basket.objects.all()
    for bas in baskets:
        if bas.type == 2:
            total_amount += bas.amount

    total_rec = Basket.objects.get(title='Итоговая сумма:')
    total_rec.amount = total_amount
    total_rec.save()

    if basket.qty == 0:
        basket.delete()

    product = get_object_or_404(Product, pk=basket.product_id)
    product.qty = product.qty - diff_qty
    product.save()
    return redirect('basket_view')


class BasketView(ListView):
    template_name = 'basket_view.html'
    model = Basket
    context_object_name = 'baskets'


def basket_delete(request, pk):
    basket = get_object_or_404(Basket, pk=pk)
    basket.qty_old = basket.qty
    basket.qty = 0
    basket.save()
    return redirect(f'/change_product/{basket.pk}')


def create_order(request):
    curr_order_num = 1
    baskets = Basket.objects.all().order_by('type')
    Order.objects.all().delete()
    for basket in baskets:
        ord = Order.objects.create()
        ord.order_num = curr_order_num
        ord.type = basket.type
        ord.title = basket.title
        ord.qty = basket.qty
        ord.qty_old = basket.qty_old
        ord.price = basket.price
        ord.amount = basket.amount
        ord.product_id = basket.product_id
        ord.customer_id = basket.customer_id
        ord.save()
    Basket.objects.all().delete()
    basket = Basket.objects.create()
    basket.title = 'Итоговая сумма:'
    basket.type = 1
    basket.customer_id = 1
    basket.qty = 99
    basket.save()
    return redirect('order_view')


class OrderView(ListView):
    template_name = 'order_view.html'
    model = Order
    context_object_name = 'orders'


def category_view(request: WSGIRequest, cat_id):
    print("cat_id ='" + cat_id + "'")
    products = Product.objects.filter(category=cat_id)
    context = {
        'products': products, 'choices': CategoryChoice.choices, 'category_name': cat_id
    }
    return render(request, 'category_view.html', context=context)


def search_product_view(request: WSGIRequest, find_str):
    print('find_str', find_str)
    search_string = {'search_string': find_str}
    return render(request, 'partial/search.html', context=search_string)
