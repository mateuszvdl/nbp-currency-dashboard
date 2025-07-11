import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
import psycopg2

root = tk.Tk()
root.title("System raportowy")
root.geometry("800x600")

conn = psycopg2.connect(
    database="...",
    user='...',
    password='...',
    host='...',
    port='...'
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM public.swps_tabela_kursow_t WHERE grupa = 'BM' ORDER BY id ASC")

data = cursor.fetchall()

conn.close()

columns = [desc[0] for desc in cursor.description]
df = pd.DataFrame(data, columns=columns)

def generate_table():
    table_frame = ttk.Frame(root)
    table_frame.place(x=20, y=20)

    table = ttk.Treeview(table_frame)
    table['columns'] = tuple(df.columns)

    for column in df.columns:
        table.heading(column, text=column)

    for index, row in df.iterrows():
        table.insert("", 'end', values=tuple(row))

    table.pack()

def generate_chart():
    plt.bar(df['kurs_dla'], df['kurs'])
    plt.xlabel('Kurs dla')
    plt.ylabel('Kurs')
    plt.title('Wykres')
    plt.show()

table_button = ttk.Button(root, text="Generuj zestawienie tabelaryczne", command=generate_table)
table_button.place(x=20, y=550)

chart_button = ttk.Button(root, text="Generuj wykres", command=generate_chart)
chart_button.place(x=200, y=550)

root.mainloop()
