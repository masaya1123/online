import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask , render_template , request , redirect , send_from_directory, session , url_for
import datetime
import os
from werkzeug.utils import secure_filename
from flask import send_from_directory

app = Flask(__name__)

#成功コード（途中経過）
# @app.route('/')
# def index():
#     return render_template('main.html')

# @app.route('/calendar')
# def calendar():
#     conn = sqlite3.connect('notbose.db')
#     c = conn.cursor()
#     c.execute('SELECT day13 FROM calendar where taskid = 1')#列名の頭に数字は使えない
#     succeess_failed=c.fetchone()[0]
#     conn.commit()
#     conn.close()
#     return render_template('main.html',succeess_failed = succeess_failed)



#これをコピペで1～31日まで作る
#dbからカレンダーに成果を反映するコード
@app.route('/main')
def mian():
    conn = sqlite3.connect('notbose.db')
    c = conn.cursor()
    c.execute('SELECT day13 FROM calendar where taskid = 1')#taskidを拾ってくる必要あり#列名の頭に数字は使えない
    succeess_failed=c.fetchone()[0]
    conn.commit()
    conn.close()
    return render_template('main.html',succeess_failed = succeess_failed)
#dbからカレンダーに成果を反映するコード


#サイトからdbに成功をinputするコード(途中)
@app.route('/succeess', methods=["POST"])
def succeess():
    conn = sqlite3.connect('notbose.db')
    c = conn.cursor()
    c.execute('update calendar set day13 = 1 where taskid = 1')#'day13'とtaskidを拾ってくる必要あり
    conn.commit()
    conn.close()
    return redirect('/')

#成功コードが書けたらコピペで失敗コードを書く




if __name__ == "__main__":
    app.run(debug=True)