import sqlite3

from django.shortcuts import render
from orders.models import Order,OrderItem
from shop.models import Product
import datetime
from collections import Counter
from django.http import JsonResponse

# Create your views here.

def SalesDashboard(request):
    template = "reportes/sales_dashboard.html"

    sales_models = Order.objects.filter(paid=True).values_list("first_name")
    sales_count_rep = Counter([rep[0] for rep in sales_models])

    sales_amount_rep={}

    for rep in sales_count_rep:
        sales_amount_rep[rep]=0

 ############################################################################
    product_models = Product.objects.filter().values_list("name","quantity","id","sellProduct")

    product_amount_rep={}

    for product in product_models:
        product_amount_rep[product[0]] = product[1];



############################################################################
    orderItem = OrderItem.objects.filter().values_list("product_id","quantity")
    orderItem_productID = Counter([rep[0] for rep in orderItem])

    productOrder_rep = {}

    for rep in orderItem_productID:
        for order in orderItem:
            for product in product_models:
                if rep == product[2]:
                    productOrder_rep[product[0]] = product[3]


    if request.is_ajax():

        color = "rgba(53,135,164,0.7)"
        color2 = "rgba(121,67,117,0.7)"
        color3 = "rgba(18,67,117,0.7)"
        bar_color = []
        bar_color2 = []
        bar_color3 = []
        for s in range(len(sales_count_rep)):
            bar_color.append(color)
            bar_color2.append(color2)
            bar_color3.append(color3)
        sales_count_chart_data={
            "labels":list(sales_count_rep.keys()),
            "datasets":[{
                "label":"Broj narudzbina po korisniku",
                "data":list(sales_count_rep.values()),
                "backgroundColor":bar_color
            }]
        }

        product_amount_chart_data={
            "labels":list(product_amount_rep.keys()),
            "datasets":[{
                "label":"Broj proizvoda na stanju",
                "data":list(product_amount_rep.values()),
                "backgroundColor":bar_color2
            }]
        }

        product_order_chart_data = {
            "labels": list(productOrder_rep.keys()),
            "datasets": [{
                "label": "Broj porudzbina po proizvodu",
                "data": list(productOrder_rep.values()),
                "backgroundColor": bar_color3
            }]
        }

        data_dict = {
            "sales_count_chart_data": sales_count_chart_data,
            "product_amount_chart_data": product_amount_chart_data,
            "product_order_chart_data": product_order_chart_data
        }
        return JsonResponse(data=data_dict,safe=False)
    return render(request, template)

