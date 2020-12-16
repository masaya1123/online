import sqlite3

conn = sqlite3.connect('notbose.db')
c = conn.cursor()
c.execute('SELECT day13 FROM calendar where taskid = 1')#列名の頭に数字は使えない
print(c.fetchone()[0])
conn.commit()
conn.close()

print(1)


conn = sqlite3.connect('notbose.db')
c = conn.cursor()
c.execute('update calendar set day13 = 1 where taskid = 1')
conn.commit()
conn.close()



conn = sqlite3.connect('notbose.db')
c = conn.cursor()
c.execute('update calendar set @day text ; = 0 where taskid = 1')
conn.commit()
conn.close()