# 🧾 Python Reporting System for NBP Currency Data

A desktop application built with Python that fetches and visualizes currency exchange rate data from a PostgreSQL database containing information from the **National Bank of Poland (NBP)**.

---

## ✨ Features

- 🔌 Connects to a **remote PostgreSQL database** to retrieve live currency exchange data.
- 📊 Uses **pandas** to efficiently process and structure the data.
- 🖼 Displays the data in a **sortable Tkinter table**.
- 📈 Generates **bar charts** of currency rates using **Matplotlib**.

---

## ⚙️ Setup and Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/python-currency-reporter.git
cd python-currency-reporter
```
> 🔁 Replace `your-username` with your actual GitHub username.

---

### 2. Set Up and Run the Application

```bash
# (1) Create and activate a virtual environment
# macOS/Linux:
python3 -m venv venv
source venv/bin/activate

# Windows:
python -m venv venv
venv\Scripts\activate

# (2) Install required dependencies
pip install -r requirements.txt

# (3) Run the application
python app.py
```

This will launch a Tkinter window. You can:
- 🧮 Generate and display the data table.
- 📊 Display a bar chart with exchange rates.

---

### 🗂️ Project Structure (Example)

```
python-currency-reporter/
│
├── app.py
├── requirements.txt
├── README.md
└── ...
```

---

### 📘 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Contributions

Pull requests and issues are welcome!
