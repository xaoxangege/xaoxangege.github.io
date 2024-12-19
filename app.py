from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# 路由: 显示首页
@app.route('/')
def index():
    return render_template('index.html')

# 路由: 显示账单记录
@app.route('/records')
def records():
    conn = sqlite3.connect('templates/database/accounting.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records")
    rows = cursor.fetchall()
    conn.close()
    return render_template('records.html', records=rows)

if __name__ == '__main__':
    # 此部分删除
    pass
