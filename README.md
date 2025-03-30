
# GSG-InfoSystem

A Django-web based Project

---
### Setup Instructions

### 1. clone the repo 
```bash 
git clone https://github.com/07himanshu20/GSG-InfoSystem-Portfolio.git
cd GSG-InfoSystem-Portfolio 
```

### 2. Create virtual Environment for python
```bash
python3 -m venv env
source /env/bin/activate
```

### 3.Run the project on localserver
```bash
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py migrations
python3 manage.py runserver
