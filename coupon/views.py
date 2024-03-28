from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CouponCode
from .forms import CouponForms
from django.utils import timezone
from django.shortcuts import redirect


# Create your views here.

@login_required
def coupon_apply(request):
	now = timezone.now()
	form = CouponForms()
	if form.is_valid():
		code = form.cleaned_data.get('code')
		try:
			coupon = CouponCode.objects.get(code__iexact=code, valid_from__lte=now, valid_to__gte=now, active=True)
			request.session['coupon_id'] = coupon.id
		except CouponCode.DoesNotExist:
			request.session['coupon_id'] = None
	return redirect('cart:cart_details')
