# 🏢 Employee Management System

![Django](https://img.shields.io/badge/Django-Employee%20Management%20System-green?style=for-the-badge)

This is a **Django-based Employee Management System** developed for a **Database Course Project**. The system allows users to manage employee records, including adding, updating, and deleting employee details.

## 📁 Project Structure

```
Employee-Management-System/
│── employees/        # Django app handling employee data
│── templates/        # HTML templates for frontend
│── static/           # CSS, JS, and images
│── db.sqlite3        # SQLite database
│── manage.py         # Django management script
│── README.md         # Project documentation
```

## ✨ Features
✅ Add new employees 👨‍💼👩‍💼  
✅ Update employee details ✏️  
✅ Delete employees ❌  
✅ View a list of employees 📋  
✅ Search employees 🔍  
✅ User authentication (Admin login) 🔑  

## 🛠️ Technologies Used
- **Backend:** Django (Python)
- **Database:** SQLite
- **Frontend:** HTML, CSS, Bootstrap

## 🚀 Installation & Setup

1️⃣ Clone this repository:
```bash
git clone https://github.com/yourusername/employee-management.git
cd employee-management
```

2️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

3️⃣ Apply migrations:
```bash
python manage.py migrate
```

4️⃣ Run the Django server:
```bash
python manage.py runserver
```

5️⃣ Open in browser: **http://127.0.0.1:8000/**

## 🔐 Admin Access
To access the admin panel:
```bash
python manage.py createsuperuser
```
Then, go to **http://127.0.0.1:8000/admin/** and log in with your credentials.

## 🎯 Future Improvements
- [ ] Implement Role-Based Access Control (RBAC)
- [ ] Add employee attendance tracking
- [ ] Improve UI/UX with better styling

## 🤝 Contributing
Contributions are welcome! Feel free to **fork**, **open an issue**, or **submit a pull request**. 🚀

## ⭐ Show Your Support
If you found this project useful, don't forget to **star** this repository! ⭐

---
📌 **Author:** Raul 👨‍💻 | 💡 Django & Databases Project
