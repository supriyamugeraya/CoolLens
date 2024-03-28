# Wrappers-India-Online
E Commerce Project
Video Link https://youtu.be/gTKKXUt2z0s



<div class="user_links pt-1">
				<a href="{% url 'main_cart' %}" style="font-size: 22px; color: #fff; margin-right: 20px;"><i
						class="fa fa-shopping-cart" aria-hidden="true"></i><sup><span class="badge"
							id="cart_no">{{cart_element_no}}</span></sup></a>
				{% if request.user.is_authenticated %}
				<a href="##" data-container="body" data-toggle="popover" data-placement="bottom" data-trigger="focus"
					data-html="true"
					data-content="<a href='{% url 'myorders' %}'>My Order</a><br><a href='{% url 'account_settings' %}'>Account Settings</a>"><img
						src="{{request.user.userdetail.photo.url}}"
						style="height: 20px; width: 20px; border-radius: 10px; margin-right: 3px;">{{request.user.first_name}}</a>&nbsp;|
				<a href="{% url 'logout' %}">Logout</a>
				{% else %}
				<a href="{% url 'login' %}">Login</a>&nbsp;|
				<a href="{% url 'signup' %}">Register</a>&nbsp;|
				<a href="{% url 'seller_signup' %}">Seller</a>
				{% endif %}