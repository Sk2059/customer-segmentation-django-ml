from django.shortcuts import render

from .forms import CustomerRFMForm
from .ml_utils import predict_segment


def predict_segment_view(request):
    result = None

    if request.method == "POST":
        form = CustomerRFMForm(request.POST)
        if form.is_valid():
            result = predict_segment(
                recency=form.cleaned_data["recency"],
                frequency=form.cleaned_data["frequency"],
                monetary=form.cleaned_data["monetary"],
            )
    else:
        form = CustomerRFMForm()

    return render(
        request,
        "segmentation/predict.html",
        {"form": form, "result": result},
    )
