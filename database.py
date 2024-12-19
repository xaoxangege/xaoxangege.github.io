import sqlite3
import os

# 数据库路径
db_path = os.path.join(os.path.dirname(__file__), 'templates', 'database', 'accounting.db')

# 创建数据库和表格
def create_table():
    if not os.path.exists(db_path):
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount INTEGER,
                time TEXT,
                user_name TEXT
            )
        ''')
        conn.commit()
        conn.close()

# 创建数据库表格
create_table()
