from django.shortcuts import render, get_object_or_404
from .models import TechType, Product, Review

# Create your views here.
def index(request):
    return render(request, 'TechReviewApp/index.html')

def gettypes(request):
    type_list = TechType.objects.all()
    return render(request, 'TechReviewApp/types.html', {'type_list' : type_list})

def getproducts(request):
    product_list = Product.objects.all()
    return render(request, 'TechReviewApp/products.html', {'product_list' : product_list})

def getreviews(request):
    review_list = Review.objects.all()
    return render(request, 'TechReviewApp/reviews.html', {'review_list' : review_list})

def productdetails(request, id):
    prod = get_object_or_404( Product, pk=id )
    discount = prod.memberDiscount()
    reviews = Review.objects.filter(product = id).count()
    context = {
        'prod' : prod,
        'discount' : discount,
        'reviews' : reviews
    }
    return render( request, 'TechReviewApp/proddetails.html', context = context)