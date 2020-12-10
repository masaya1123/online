import sqlite3
import datatime
import os
from flask import Flask,render_template,request,redirect,session,send_from_directory,url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

#メモ書き
#【todo】dbに登録したLINE IDをLINEボットへ送信




if __name__ =="__main__":
    app.run(debug=True)