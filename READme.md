# 📊 Customer Segmentation — Django + Machine Learning

An end-to-end customer segmentation tool: an RFM (Recency, Frequency, Monetary)
pipeline trained with K-Means clustering, served through a Django web form
that returns a labeled segment for any customer.

Enter a customer's Recency, Frequency, and Monetary values and get back a
plain-language segment — **Champions**, **Loyal Customers**, **At Risk /
Churned**, or **New / Occasional** — instead of a raw cluster number.

---

## 📌 Project Overview

Customer segmentation groups customers into meaningful clusters based on
purchasing behavior, so a business can target marketing and retention
differently for a big spender who buys weekly versus someone who bought once
a year ago and never came back.

This project combines:

- 🧠 **Machine Learning** — RFM feature engineering + K-Means clustering (scikit-learn)
- 🌐 **Django** — a form-driven web interface that loads the trained model and returns predictions
- 📊 **EDA & visualization** — outlier handling, the elbow method, PCA cluster plots (see `notebooks/segmentation.ipynb`)
- 💾 **Model serialization** — the fitted scaler, PCA, and K-Means model are persisted with `joblib`

---

## 🖥️ Features

- Web form to enter a customer's Recency / Frequency / Monetary values
- Instant, labeled segment prediction (not just a cluster number)
- Server-side validation (no negative values, etc.)
- Cluster labels derived from the model's actual trained centroids, not guessed
- Test suite covering both the ML prediction logic and the Django view
- CI workflow that runs the test suite on every push

---

## ⚙️ Tech Stack

- **Backend:** Django 5.2
- **Machine Learning:** scikit-learn (K-Means, PCA, StandardScaler), joblib
- **Frontend:** Plain HTML/CSS (no framework dependency)
- **Testing:** pytest, pytest-django
- **CI:** GitHub Actions

---

## 📊 Dataset & ML Workflow

Trained on the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online+retail)
(`data/raw/OnlineRetail.csv`), transaction-level data from a UK-based online store.

1. Data cleaning — drop nulls/duplicates, remove cancelled orders
2. Feature engineering — build RFM (Recency, Frequency, Monetary) per customer
3. Outlier treatment — IQR-based filtering on Monetary
4. Feature scaling — `StandardScaler`
5. Finding optimal clusters — elbow method (k=4 chosen)
6. K-Means clustering + PCA (2D) for visualization
7. Model evaluation — silhouette score
8. Persist `model.pkl`, `scaler.pkl`, `pca.pkl` with `joblib`
9. Cluster centers are inverse-transformed back into real R/F/M units and
   mapped to human-readable labels in `segmentation/ml_utils.py`

The full walkthrough, including plots, lives in `notebooks/segmentation.ipynb`.

**Resulting segments** (from this project's trained model):

| Cluster | Label | Recency | Frequency | Monetary |
|---|---|---|---|---|
| 2 | Champions | ~29 days | ~8.5 orders | ~2,610 |
| 0 | Loyal Customers | ~46 days | ~4.2 orders | ~1,475 |
| 3 | New / Occasional | ~56 days | ~1.8 orders | ~446 |
| 1 | At Risk / Churned | ~258 days | ~1.4 orders | ~383 |

If you retrain on different data, re-run the centroid inspection and update
`CLUSTER_LABELS` in `segmentation/ml_utils.py` — cluster index ordering isn't
guaranteed to stay the same across retrains.

---

## 📁 Project Structure

```
customer-segmentation-django-ml/
│
├── config/                  # Django project settings, root urls
├── segmentation/
│   ├── ml_utils.py          # Loads model/scaler/pca, predict_segment()
│   ├── forms.py             # CustomerRFMForm
│   ├── views.py             # predict_segment_view
│   ├── urls.py
│   └── tests.py             # pytest tests (ml_utils + view)
├── templates/segmentation/
│   └── predict.html
├── notebooks/
│   └── segmentation.ipynb   # Full EDA + training pipeline
├── ml/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── pca.pkl
├── data/raw/
│   └── OnlineRetail.csv
├── .github/workflows/ci.yml
├── requirements.txt         # Runtime deps only
├── requirements-dev.txt     # + notebook/test deps
├── .env.example
├── pytest.ini
└── manage.py
```

---

## ▶️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sk2059/customer-segmentation-django-ml.git
cd customer-segmentation-django-ml
```

### 2. Create a virtual environment

```bash
python -m venv env
```

**Activate it:**

```bash
# Windows
env\Scripts\activate

# Linux / Mac
source env/bin/activate
```

### 3. Install dependencies

```bash
# Just to run the app:
pip install -r requirements.txt

# To also run the notebook and tests:
pip install -r requirements-dev.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` and set a real `DJANGO_SECRET_KEY` if you're deploying anywhere
beyond your own machine. The defaults work fine for local development.

### 5. Run migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

### 🌐 Open in browser

```
http://127.0.0.1:8000/
```

---

## 🧪 Running Tests

```bash
pip install -r requirements-dev.txt
pytest -v
```

Tests cover:
- `ml_utils.predict_segment()` — correctness of predictions for clearly high- and low-value customers
- The Django view — GET renders the form, POST with valid/invalid data behaves correctly

CI (`.github/workflows/ci.yml`) runs this suite automatically on every push and pull request to `main`.

---

## 🧠 Model Details

- **Algorithm:** K-Means clustering, k=4 (chosen via elbow method)
- **Features:** Recency, Frequency, Monetary (RFM), standardized
- **Output:** one of four labeled segments — Champions, Loyal Customers, New/Occasional, At Risk/Churned

---

## 📈 Use Cases

- Retail customer segmentation
- Marketing strategy optimization (who to target with what)
- Identifying at-risk customers for retention campaigns
- Business decision support / dashboards

---

## 🚀 Future Improvements

- [ ] Persist predictions to the database (currently stateless per request)
- [ ] Compute RFM automatically from an uploaded order history instead of manual entry
- [ ] Add a dashboard view (Plotly/Dash) showing overall segment distribution
- [ ] Deploy to Render/Railway with Postgres instead of SQLite
- [ ] Add authentication for multi-user / multi-business use
- [ ] Docker + docker-compose for one-command setup

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sk Singh
GitHub: [Sk2059](https://github.com/Sk2059)
