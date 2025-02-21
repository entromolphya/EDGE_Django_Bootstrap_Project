# 🌳 Tree Store - Django Project

Welcome to **Tree Store**, an online tree-selling blog built with **Django**, **Bootstrap**, and **SQLite**. Users can browse various tree-related blog posts and purchase their favorite trees through external links.

## 🚀 Features

✔ **Home Page** - Introduction to Tree Store and featured trees.  
✔ **Blog Page** - Lists all tree-related blog posts with images, descriptions, and purchase links.  
✔ **Buy Now Button** - Redirects users to external websites to buy trees.  
✔ **Admin Panel** - Add, update, or delete blog posts using Django Admin.  
✔ **Database Integration** - Stores all blog data in SQLite.  
✔ **Bootstrap UI** - Responsive and modern design.  

## 🛠️ Installation Guide

Follow these steps to set up the project on your local machine:

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/tree-store.git
cd tree-store


2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv env
Activate the environment:

Windows: env\Scripts\activate
Mac/Linux: source env/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Apply Migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
5️⃣ Create a Superuser (Admin Panel)
bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to set up a username and password.

6️⃣ Run the Server
bash
Copy
Edit
python manage.py runserver
Then open the browser and visit:

Home Page: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/
📂 Project Structure
bash
Copy
Edit
tree-store/
│── treestore/        # Django Project Configuration
│── blog/             # Blog App (Models, Views, URLs)
│── templates/        # HTML Templates
│── static/           # CSS, JS, and Images
│── db.sqlite3        # Database File
│── manage.py         # Django Management Script
│── env/              # Virtual Environment (Ignore this in Git)
🛠️ Technologies Used
Django (Python Web Framework)
Bootstrap (CSS Framework)
SQLite (Database)
HTML, CSS (Frontend)
🤝 Contributing
Feel free to fork this repository and contribute improvements!

Fork the repository
Create a new branch (git checkout -b feature-branch)
Commit your changes (git commit -m "Added a new feature")
Push to your branch (git push origin feature-branch)
Create a Pull Request
📄 License
This project is open-source and available under the MIT License.