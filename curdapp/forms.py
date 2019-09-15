from django import forms

class InsertDataForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )
    procuct_name=forms.CharField(
        label="Enter Product Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_color=forms.CharField(
        label="Enter Product Color",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Color'
            }
        )
    )
    product_class=forms.CharField(
        label="Enter Product Class",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Class'
            }
        )
    )
    product_cost=forms.CharField(
        label="Enter Product Cost",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    number_of_items=forms.IntegerField(
        label="Enter Number Of Items",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Number Of Items'
            }
        )
    )
    customer_name=forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    customer_mobile=forms.IntegerField(
        label="Enter Customer Mobile Number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Mobile'
            }
        )
    )
    custumer_email=forms.EmailField(
        label="Enter Custumer Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Email'
            }
        )
    )

class UpdateDataForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Product Id",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Id'
            }
        )
    )
    product_cost=forms.IntegerField(
        label="Enter Product Cost",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
class DeleteDataForm(forms.Form):
    product_id=forms.IntegerField(
        label="Enter Product Id ",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Id'
            }
        )
    )