"""
Tests for the segmentation app.

Run with: pytest
(requires pytest + pytest-django - see requirements-dev.txt)
"""

import pytest
from django.urls import reverse

from segmentation.ml_utils import predict_segment, SegmentPrediction


# ---- ml_utils: pure logic, no Django client needed ------------------------

def test_predict_segment_returns_a_valid_prediction():
    result = predict_segment(recency=10, frequency=10, monetary=3000)

    assert isinstance(result, SegmentPrediction)
    assert result.cluster_id in {0, 1, 2, 3}
    assert result.label  # not empty
    assert isinstance(result.pca_x, float)
    assert isinstance(result.pca_y, float)


def test_low_engagement_customer_is_not_labeled_champion():
    # Long time since last order, almost never buys, spends little ->
    # should land in a low-value cluster, not "Champions".
    result = predict_segment(recency=400, frequency=1, monetary=20)
    assert result.label != "Champions"


def test_high_engagement_customer_is_not_labeled_at_risk():
    # Very recent, frequent, big spender -> should not be flagged "At Risk".
    result = predict_segment(recency=2, frequency=15, monetary=5000)
    assert result.label != "At Risk / Churned"


# ---- view: needs Django's test client + DB, so mark it -------------------

@pytest.mark.django_db
def test_predict_view_get_renders_empty_form(client):
    response = client.get(reverse("segmentation:predict"))
    assert response.status_code == 200
    assert b"Predict segment" in response.content


@pytest.mark.django_db
def test_predict_view_post_valid_data_shows_result(client):
    response = client.post(
        reverse("segmentation:predict"),
        data={"recency": 30, "frequency": 5, "monetary": 1200},
    )
    assert response.status_code == 200
    assert response.context["result"] is not None


@pytest.mark.django_db
def test_predict_view_post_invalid_data_shows_errors(client):
    response = client.post(
        reverse("segmentation:predict"),
        data={"recency": -5, "frequency": 5, "monetary": 1200},
    )
    assert response.status_code == 200
    assert response.context["result"] is None
    assert not response.context["form"].is_valid()
