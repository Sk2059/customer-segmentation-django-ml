"""
Loads the trained K-Means pipeline (scaler -> PCA -> KMeans) produced by
notebooks/segmentation.ipynb and exposes a single predict_segment() function
that the Django view calls.

The artifacts are loaded once at import time (module-level singletons) rather
than on every request, since joblib.load() from disk is comparatively slow.

Cluster labels below were derived by inverse-transforming the fitted
KMeans cluster centers back into original Recency/Frequency/Monetary units
(see the "Cluster interpretation" cell added to the notebook) and are specific
to the OnlineRetail.csv training run. If you retrain the model on different
data, re-run that inspection and update CLUSTER_LABELS accordingly - the
cluster index KMeans assigns to "high value" customers isn't guaranteed to
stay at the same integer across retrains.
"""

import warnings
from dataclasses import dataclass

import joblib
from django.conf import settings



_model = None
_scaler = None
_pca = None

# Cluster index -> (label, short description). Derived from this project's
# trained model; see docstring above.
CLUSTER_LABELS = {
    0: ("Loyal Customers", "Buys regularly and spends well; recent activity."),
    1: ("At Risk / Churned", "Long time since last purchase, buys rarely."),
    2: ("Champions", "Most recent, most frequent, and highest spending customers."),
    3: ("New / Occasional", "Infrequent buyers with modest spend."),
}


def _load_artifacts():
    """Load the three pickled objects the first time they're needed."""
    global _model, _scaler, _pca
    if _model is None:
        artifacts_dir = settings.ML_ARTIFACTS_DIR
        _model = joblib.load(artifacts_dir / "model.pkl")
        _scaler = joblib.load(artifacts_dir / "scaler.pkl")
        _pca = joblib.load(artifacts_dir / "pca.pkl")
    return _model, _scaler, _pca


@dataclass
class SegmentPrediction:
    cluster_id: int
    label: str
    description: str
    pca_x: float
    pca_y: float


def predict_segment(recency: float, frequency: float, monetary: float) -> SegmentPrediction:
    """
    Given raw RFM values for a customer, return which cluster they fall into.

    Feature order MUST match training: [Recency, Frequency, Monetary].
    """
    model, scaler, pca = _load_artifacts()

    features = [[recency, frequency, monetary]]

    # The scaler/PCA/KMeans were originally fit on a pandas DataFrame with
    # named columns (Recency/Frequency/Monetary). We predict from a plain
    # list here to avoid adding pandas as a production dependency, which
    # triggers a harmless "X does not have valid feature names" warning -
    # silence just that.
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore", message="X does not have valid feature names", category=UserWarning
        )
        scaled = scaler.transform(features)
        cluster_id = int(model.predict(scaled)[0])
        pca_coords = pca.transform(scaled)[0]

    label, description = CLUSTER_LABELS.get(
        cluster_id, (f"Cluster {cluster_id}", "No description available.")
    )

    return SegmentPrediction(
        cluster_id=cluster_id,
        label=label,
        description=description,
        pca_x=float(pca_coords[0]),
        pca_y=float(pca_coords[1]),
    )
