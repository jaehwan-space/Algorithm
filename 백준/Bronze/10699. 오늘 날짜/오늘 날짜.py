from datetime import datetime, timedelta

# UTC 현재 시간
now_utc = datetime.utcnow()

# 서울 시간 (UTC + 9)
now_kst = now_utc + timedelta(hours=9)

print(now_kst.strftime("%Y-%m-%d"))
