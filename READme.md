# 📊 Customer Segmentation using Django & Machine Learning

An end-to-end Machine Learning + Django web application that performs customer segmentation using K-Means clustering.  
This project helps group customers based on their behavior and demographics for better marketing and business decisions.

---

---

## 📌 Project Overview

Customer segmentation is an unsupervised machine learning technique used to divide customers into meaningful groups based on patterns in data.

This project combines:
- 🧠 Machine Learning (K-Means Clustering)
- 🌐 Django Web Framework
- 📊 Data preprocessing & visualization
- 💾 Model serialization using Pickle/Joblib

Users can input customer details through a web form and get predicted customer segments instantly.

---

## 🎯 Objectives

- Segment customers based on behavior patterns
- Identify different customer groups
- Provide a web interface for predictions
- Demonstrate ML model deployment using Django

---

## ⚙️ Tech Stack

- Backend: Django
- Machine Learning: Scikit-learn, Pandas, NumPy
- Model: K-Means Clustering
- Frontend: HTML, CSS, Bootstrap
- Visualization: Matplotlib / Seaborn (if used)

---

## 📊 Dataset

The dataset includes customer-related features such as:
- Age
- Annual Income
- Spending Score

Data is preprocessed before training:
- Handling missing values
- Feature scaling
- Encoding (if required)

---

## 🧠 Machine Learning Workflow

1. Data Collection  
2. Data Preprocessing  
3. Feature Scaling  
4. Finding optimal clusters (Elbow Method)  
5. K-Means Clustering  
6. Model saving (Pickle/Joblib)  
7. Integration with Django

---

## 🖥️ Features

- User input form for customer data
- Instant prediction of customer segment
- ML model integrated with Django backend
- Simple and clean UI
- Scalable architecture for improvements

---

## 📁 Project Structure
customer-segmentation-django-ml/
│
├── app/ # Django app
│ ├── views.py
│ ├── urls.py
│ ├── models.py
│ └── templates/
│
├── ml_model/
│ ├── model.pkl
│ ├── scaler.pkl
│
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md

###  How to Run Locally
1️⃣ Clone the repository
--git clone https://github.com/Sk2059/customer-segmentation-django-ml.git
--cd customer-segmentation-django-ml

2️⃣ Create virtual environment
--python -m venv env
--source env/bin/activate   # Linux/Mac
--env\Scripts\activate      # Windows

3️⃣ Install dependencies
--pip install -r requirements.txt

4️⃣ Run migrations
--python manage.py migrate

5️⃣ Start server
--python manage.py runserver
---

## 🧪 Model Details

- Algorithm: K-Means Clustering
- Optimal clusters found using Elbow Method
- Output: Customer segment labels (Cluster 0, 1, 2...)

---

## 📈 Use Cases

- Retail customer segmentation
- Marketing strategy optimization
- Customer behavior analysis
- Business decision support

---

## 🚀 Future Improvements

- Add interactive dashboard (Plotly/Dash)
- Deploy on cloud (Render / AWS / Railway)
- Use advanced clustering methods (DBSCAN, Hierarchical)
- Add authentication system
- Store predictions in database

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sk Singh  
GitHub: https://github.com/Sk2059