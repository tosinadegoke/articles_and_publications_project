from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm, RawProductForm
# Create your views here.

# def product_create_view(request):
    # my_form = RawProductForm()
    # print(request.GET)
    # print(request.POST)
    # if request.method == 'POST':
    #     print('the title is: ', request.POST.get('title'))
        # my_form  = RawProductForm(request.POST)
        # if my_form.is_valid():
        #     #now the submitted data is good
        #     print(my_form.cleaned_data) 
    # context = {
    #     # 'form' : my_form
    # }
    # return render (request, "products/product_create.html", context)

def product_create_view(request):
    my_form = RawProductForm()
    if request.method == 'POST':
        my_form  = RawProductForm(request.POST)
        if my_form.is_valid():
            #now the submitted data is good
            print(my_form.cleaned_data) 
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            print(my_form.errors)
    context = {
        'form' : my_form
    }
    return render (request, "products/product_create.html", context)


def product_update_view(request, prod_id):
    obj = get_object_or_404(Product, id = prod_id)
    my_form = ProductForm(request.POST or None, instance= obj)
    if my_form.is_valid():
        my_form.save()
        my_form = ProductForm()
    context = {
        'form' : my_form
    }
    return render(request, 'products/product_create.html', context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form' : form
#     }
#     return render (request, "products/product_create.html", context)

def product_detail_view(request, my_id):
    # obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id = my_id)
    
    context = {
        'object' : obj,
    }
    return render(request, "products/details.html", context)
    

def product_delete_view(request, prod_id):
    obj = get_object_or_404(Product, id = prod_id)
    if request.method == 'POST':
        #   confirming delete
        obj.delete()
        # return redirect('../')
        return redirect('product_list') #   the webpage to product list page

    context = {
        'object': obj,
    }
    return render(request, 'products/product_delete.html', context)


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render (request, 'products/product_list.html', context)



# def product_detail_view(request):
#     obj = Product.objects.get(id=1)
#     context = {
#         'object' : obj,
#     }
#     return render(request, "products/details.html", context)