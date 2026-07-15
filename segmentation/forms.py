from django import forms


class CustomerRFMForm(forms.Form):
    """
    Collects the three RFM inputs the trained model expects.

    In a real deployment these would usually be computed automatically from
    a customer's order history rather than typed in by hand - this form is
    the manual-entry path described in the README ("Users can input customer
    details through a web form").
    """

    recency = forms.IntegerField(
        min_value=0,
        label="Recency (days since last purchase)",
        help_text="How many days ago did this customer last buy something?",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 30"}),
    )
    frequency = forms.IntegerField(
        min_value=0,
        label="Frequency (number of orders)",
        help_text="How many separate orders has this customer placed?",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 5"}),
    )
    monetary = forms.FloatField(
        min_value=0,
        label="Monetary (total amount spent)",
        help_text="Total lifetime spend for this customer.",
        widget=forms.NumberInput(attrs={"class": "form-control", "placeholder": "e.g. 1200.00"}),
    )
