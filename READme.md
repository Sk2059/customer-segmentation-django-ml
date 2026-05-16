📊 Customer Segmentation using Django & Machine Learning

An end-to-end Machine Learning + Django web application that performs customer segmentation using clustering techniques (K-Means).
The system groups customers based on behavioral and demographic data to help businesses improve targeted marketing, personalization, and decision-making.


📌 Project Overview

Customer segmentation is an unsupervised machine learning technique used to divide customers into meaningful groups based on patterns in data.

This project integrates:

🧠 Machine Learning (K-Means Clustering)
🌐 Django Web Framework
📊 Data Preprocessing & Visualization
💾 Model Serialization (Pickle/Joblib)

Users can input customer data through a web interface and instantly get predicted customer segments.

🎯 Objectives
Segment customers based on behavior patterns
Identify high-value and low-value customer groups
Provide a simple web interface for predictions
Demonstrate ML deployment using Django
⚙️ Tech Stack
Backend: Django
Machine Learning: Scikit-learn, Pandas, NumPy
Model: K-Means Clustering
Frontend: HTML, CSS, Bootstrap
Visualization: Matplotlib / Seaborn (if used)
Deployment: (Add if applicable)
📊 Dataset

The model is trained on customer-related features such as:

Age
Annual Income
Spending Score
(Other behavioral features depending on dataset)

Dataset is preprocessed before training (handling missing values, scaling, encoding if required).

🧠 Machine Learning Workflow
Data Collection
Data Cleaning & Preprocessing
Feature Scaling (Standardization)
Finding Optimal Clusters (Elbow Method)
K-Means Clustering
Model Saving using Pickle/Joblib
Integration with Django Backend
🖥️ Features
🔢 Input customer details via web form
🤖 Predict customer segment instantly
📈 Visual insights into clustering (optional charts)
💾 Pre-trained ML model integrated with Django
📊 Easy-to-use dashboard interface
📁 Project Structure
customer-segmentation-django-ml/
│
├── app/                    # Django app
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── templates/
│
├── ml_model/
│   ├── model.pkl          # Trained clustering model
│   ├── scaler.pkl         # Feature scaler (if used)
│
├── static/
├── media/
├── manage.py
├── requirements.txt
└── README.md
▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/Sk2059/customer-segmentation-django-ml.git
cd customer-segmentation-django-ml
2️⃣ Create virtual environment
python -m venv env
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run migrations
python manage.py migrate
5️⃣ Start server
python manage.py runserver
🧪 Model Details
Algorithm: K-Means Clustering
Optimal clusters selected using: Elbow Method
Output: Customer segment labels (Cluster 0, 1, 2, …)
📈 Example Use Case

A retail company can:

Identify VIP customers
Detect low-engagement users
Run targeted marketing campaigns
Improve customer retention
📌 Future Improvements
Add real-time dashboard (Plotly / Dash)
Deploy on cloud (AWS / Render)
Add DB integration (PostgreSQL)
Use advanced clustering (DBSCAN, Hierarchical)
Add login system & analytics dashboard
🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Sk Singh
GitHub: @Sk2059