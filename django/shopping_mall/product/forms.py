from django import forms
from .models import Product



class RegisterForm(forms.Form):

    name = forms.CharField(error_messages={
        'required': "Please Enter the Name of the Product"
    }, max_length=64, label="NAME")
    price = forms.IntegerField(error_messages={
        'required': "Please Enter the Price"
    }, label="PRICE")

    description = forms.CharField(error_messages={
        'required': "Please Enter the Description"
    },  label="DESCRIPTION")

    stock = forms.IntegerField(
      error_messages={
        'required': "Please Enter the Stock"
    },  label="STOCK"
    )

    def clean(self):
        # 기존 기본 유효성 검사를 먼저 호출
        cleaned_data = super().clean()
        name=cleaned_data['name']
        price=cleaned_data['price']
        description=cleaned_data['description']
        stock=cleaned_data['stock']

        if name and price and description and stock:
            product = Product(
              name=name,
              price=price,
              description=description,
              stock=stock
            )
            product.save()
