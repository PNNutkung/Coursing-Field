from django.shortcuts import render, redirect
from django.urls import reverse
import random, string

def index(req):
    return render(req, 'coupon/add_coupon.html')

def add_coupon(req):
    coupon_serial = ''
    value = req.POST['amount']
    coupon_serial = generator()
    try:
        new_coupon = Coupon.objects.get(serial=coupon_serial)
    except(Coupon.DoesNotExist):
        new_coupon = Coupon(serial = coupon_serial,value = value,transaction_id= None)
        new_coupon.save(force_insert=True)
        return #success, do something
    return redirect(reverse('coupon:add_coupon')) #recursive until picking the unique

def generator(size=10, chars=string.ascii_uppercase + string.digits): #set default value at length of 10 with A-Z and 0-9, but can be do like generator(5,'ABC0123456')
    return ''.join(random.choice(chars) for _ in range(size))
