from django.shortcuts import redirect, render
from app.models import Product


def dashboard(request):
    products = Product.objects.all()

    context = {
        "products":products
    }
    return render(request, 'dashboard.html',context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        desciption = request.POST.get('desciption')

        print(name,category,price,desciption)
        product = Product(
            name = name,
            category = category,
            price = price,
            desciption = desciption,
            )
        product.save()

        return redirect('dashboard')


    return render(request, 'dashboard.html')

def edit(request,id):
    product = Product.objects.get(id=id)
    # print(product.name)
    context = {
        'product':product
    }
    return render(request, 'edit.html',context)

def update(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        desciption = request.POST.get('desciption')

        product = Product(
            id = id,
            name = name,
            category = category,
            price = price,
            desciption = desciption,
            )
        product.save()


        # print(name,category,price,desciption)

        
    return redirect('dashboard')

def delete(request,id):
    product = Product.objects.filter(id=id)
    product.delete()
    return redirect('dashboard')

    
    