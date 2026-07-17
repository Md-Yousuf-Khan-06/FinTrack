# 💰 FinTrack

A command-line Personal Finance Management System built using Python.

FinTrack helps users manage their personal finances by allowing them to record income and expenses, search transactions, view monthly summaries, and securely store data using JSON.

---

## 📷 Preview

### Main Menu

![Main Menu](docs/menu.png)

### Transactions

![Transactions](docs/transactions.png)

---

## ✨ Features

- ➕ Add income transactions
- ➖ Add expense transactions
- 📋 View all income and expense records
- 🔍 Search expense transactions by:
  - Category
  - Description
  - Payment Method
- 📊 View monthly financial summary
- 🗑️ Delete expense transactions
- 💾 Automatic JSON data storage
- 📅 Automatic date and time recording
- ✅ Input validation for a better user experience

---

## 🛠️ Technologies Used

- Python 3
- JSON
- Python Standard Library (`json`, `datetime`)
- Git
- GitHub

---

## 📁 Project Structure

```text
FinTrack/
│
├── src/
│   └── main.py
├── docs/
├── data.json
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Md-Yousuf-Khan-06/FinTrack.git
```

### 2. Navigate to the project folder

```bash
cd FinTrack
```

### 3. (Optional) Create and activate a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Run the application

```bash
python src/main.py
```

---

## 📋 Sample Menu

```text
FINTRACK
Personal Finance Management System

1. Add Income
2. Add Expense
3. View Transactions
4. Search Transactions
5. Monthly Summary
6. Delete Transaction
7. Exit
```

---

## 🚀 Future Improvements

- Refactor the project into multiple Python modules
- Search income transactions
- Edit existing transactions
- Category-wise expense reports
- Monthly and yearly financial reports
- SQLite database integration
- GUI using Tkinter or PyQt
- Web version using Django or Flask

---

## 👨‍💻 Author

**Mohammed Yousuf Khan**

- Python Developer
- AI & Machine Learning Enthusiast

### 🔗 Connect

- **GitHub:** https://github.com/Md-Yousuf-Khan-06
- **LinkedIn:** https://www.linkedin.com/in/mohammed-yousuf-khan-ai

---

## 📌 Project Status

**Version:** 1.0

✅ The core features of FinTrack are complete and fully functional.

### Planned Enhancements

- Modular project architecture
- Database integration (SQLite)
- Enhanced financial reports
- Graphical User Interface (GUI)
- Additional analytics and visualizations