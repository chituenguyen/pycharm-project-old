from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item, Order, OrderItem, BillingAddress, Coupon, refund
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages
from .forms import CheckoutForm, CouponForm, RefundForm
import random, string
from django.conf import settings


# Create your views here.


class HomeView(ListView):
    model = Item
    paginate_by = 12
    template_name = 'home-page.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CouponForm()
            context = {
                'object': order,
                'form': form
            }
        except ObjectDoesNotExist:
            messages.error(self.request, 'error')
            return render(self.request, 'order-summary.html')
        return render(self.request, 'order-summary.html', context)


class CheckoutView(View):
    def get(self, *args, **kwargs):
        form = CheckoutForm()
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'form': form,
                'order': order
            }
            return render(self.request, 'checkout-page.html', context)
        except:
            context = {'form': form}
            return render(self.request, 'checkout-page.html', context)

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        order = Order.objects.get(user=self.request.user, ordered=False)
        if form.is_valid():
            address = form.cleaned_data.get('address')
            apartment = form.cleaned_data.get('apartment')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            billing_address = BillingAddress(
                user=self.request.user,
                address=address,
                apartment=apartment,
                country=country,
                zip=zip,
            )
            order_items = order.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.save()

            order.ordered = True
            order.code_refund = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
            billing_address.save()
            order.billing_address = billing_address
            order.save()

            return redirect('core:home')
        return redirect('core:checkout')


class ProductDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)

    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated")
        else:
            messages.info(request, "This item was add to your cart ")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was add to your cart")
    return redirect('core:product', slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]

            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            # return redirect("core:order-summary")
            return redirect("core:product", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


@login_required
def add_element_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    order = order_qs[0]
    # check if the order item is in the order
    if order.items.filter(item__slug=item.slug).exists():
        order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        )[0]

        order_item.quantity += 1
        order_item.save()

    return redirect("core:order-summary")


@login_required
def remove_element_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    order = order_qs[0]
    # check if the order item is in the order
    if order.items.filter(item__slug=item.slug).exists():
        order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        )[0]
        if order_item.quantity > 1:
            order_item.quantity -= 1
            order_item.save()
        else:
            order.items.remove(order_item)
            order_item.delete()

    return redirect("core:order-summary")


@login_required
def trash(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    order = order_qs[0]
    # check if the order item is in the order
    if order.items.filter(item__slug=item.slug).exists():
        order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
        )[0]

        order.items.remove(order_item)
        order_item.delete()

    return redirect("core:order-summary")


def add_coupon(request):
    if request.method == 'POST':
        form = CouponForm(request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=request.user,
                    ordered=False
                )
                order.coupon = Coupon.objects.get(code=code)
                order.save()
                messages.success(request, 'success add coupon')
                return redirect('core:order-summary')
            except ObjectDoesNotExist:
                messages.info(request, 'code wrong')
                return redirect('core:order-summary')


class RefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form
        }
        return render(self.request, 'refund.html', context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST or None)
        if form.is_valid():
            code = form.cleaned_data.get('code')
            messages = form.cleaned_data.get('messages')
            email = form.cleaned_data.get('email')
            try:
                order = Order.objects.get(code_refund=code)
                order.refund = True

                store_refund = refund(
                    user=self.request.user,
                    messages=messages
                )
                store_refund.save()
                order.save()

                return redirect('core:refund')
            except ObjectDoesNotExist:
                return redirect('core:refund')
