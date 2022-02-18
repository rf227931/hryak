# requires: pyrogram, tgcrypto, apscheduler

from pyrogram import Client, idle
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timezone, timedelta
from time import sleep

API_ID = 16623
API_HASH = "8c9dbfe58437d1739540f5d53c72ae4b"

app = Client('olokill', API_ID, API_HASH)
app.start()

CHAT = -1001494427468

def job():
    app.send_message(-1001494427468, '/grow')
    app.send_message(-1001598192842, '/grow')

send_sch = BackgroundScheduler()
send_sch.add_job(job, 'interval', hours=24)

now = datetime.now(timezone(timedelta(hours=3))).time()
h, m = 23 - now.hour, 60 - now.minute + 1
sleep((h * 60 + m) * 60)

job()
send_sch.start()

try:
    idle()
finally:
    send_sch.shutdown()
    app.stop()
