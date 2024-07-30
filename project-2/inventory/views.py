from django.shortcuts import render
from .forms import *
from .models import *

# Create your views here.
def homepage(request):
    data = {
        'name':'kishor',
        'role':'hello',
        'numbers':{1,2,3,4,5,6,},
        'marks':{
            'kannada':100,
            'english':100,
        }
    }

    return render(request,'home.html',data)

# router for about page:
def aboutpage(request):

    return  render(request,'about.html')

# router for services page:
def servicespage(request):

    return render(request,'services.html')
# router for contact page:
def contactpage(request):

    return render(request,'contact.html')

def productsadd(request):
    if request.method == "POST":
        product_form = Product_Form(request.POST)
        if product_form.is_valid():
            product_form.save()
            return redirect('product_list')  # Redirect to the product list or another page
        else:
            print("Form errors: ", product_form.errors)  # Print form errors to debug issues
    else:
        product_form = Product_Form()

    context = {
        'product_form': product_form
    }
    return render(request, 'products_add.html', context)


