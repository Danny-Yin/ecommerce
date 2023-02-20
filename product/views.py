from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from product.models import User, Product, ShoppingCart


def login_view(request):
    if request.method == "POST":
        current_user = User.objects.filter(name=request.POST["username"], password=request.POST["password"]).first()
        if current_user:
            request.session['user'] = {
                'id': current_user.id,
                'username': current_user.name,
            }
            return redirect("Homepage")
        else:
            return render(request, 'Login.html', {'error': 'Invalid login credentials'})
    else:
        return render(request, 'Login.html')


def homepage_view(request):
    all_product = Product.objects.all()
    return render(request, 'Homepage.html', {'item': all_product})


def add_product(request, product_id):
    if 'user' not in request.session:
        messages.warning(request, f'Sorry, Please login')
        return redirect('Homepage')
    else:
        shopping_cart_row, created = ShoppingCart.objects.get_or_create(user_id=request.session['user']['id'],
                                                                        product_id=product_id)
        if shopping_cart_row.quantity is None:
            shopping_cart_row.quantity = 1
        else:
            shopping_cart_row.quantity += 1
        shopping_cart_row.save()
    return redirect("Homepage")


def peronalshopping_cart(request):
    if 'user' not in request.session:
        messages.warning(request, f'Sorry, Please login')
        return redirect('Homepage')
    else:
        user_id = request.session['user']['id']
        cart_items = ShoppingCart.objects.filter(user_id=user_id)
        items_in_cart = []
        total_price = 0
        for cart in cart_items:
            tmp = []
            product_rows = Product.objects.filter(id=cart.product_id)
            product_row = product_rows[0]
            tmp.append(product_row.name)
            tmp.append(cart.quantity)
            tmp.append(product_row.price)
            sub_price = tmp[-1] * tmp[-2]
            tmp.append(sub_price)
            total_price += sub_price
            tmp.append(product_row.img_url)
            tmp.append(cart.id)
            items_in_cart.append(tmp)
        context = {
            "items_in_cart": items_in_cart,
            "total_price": total_price,
            "user_name": request.session["user"]["username"]
        }
        return render(request, "myShoppingCart.html", context)



def add_number(request, item_id):
    cart_item = ShoppingCart.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('myShoppingCart')


def reduce_number(request, item_id):
    cart_item = ShoppingCart.objects.get(id=item_id)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
    return redirect('myShoppingCart')


def no_number(request, item_id):
    cart_item = ShoppingCart.objects.get(id=item_id)
    cart_item.delete()
    return redirect('myShoppingCart')
