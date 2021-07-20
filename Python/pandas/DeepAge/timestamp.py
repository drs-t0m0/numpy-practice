from datetime import datetime

import pandas as pd
import pandas.tseries.offsets as offsets
import pytz

time = datetime.now()
print(time)
print("#" * 30)

t_1 = pd.Timestamp(2018, 12, 18)
print(t_1)

t_2 = pd.Timestamp(year=2018, month=12, day=18, hour=23, minute=12, second=32)
print(t_2)
print("-" * 30)

t_3 = pd.Timestamp(1537499090, unit='s')
print(t_3)
print("-" * 30)

t_4 = pd.Timestamp(1537499090, unit='s', tz='Asia/Tokyo')
print(t_4)
print("#" * 30)

print(pd.to_datetime('2018-9-21'))
print(pd.to_datetime('2018/09/21 12:21+0900'))
print(pd.to_datetime('09/21/2018 03:34'))
print(pd.to_datetime('2018年9月21日 15時34分', format='%Y年%m月%d日 %H時%M分'))
print("#" * 30)

print(pd.date_range('2018-9-21', periods=3, freq='D'))  # 1日ごとに3つ
time_idx = pd.date_range('2018/9/21', periods=3, freq='W')  # 1週間ごとに生成
print(time_idx)
print(type(time_idx[0]))
print("#" * 30)

t_5 = pd.Timestamp(2018, 12, 18, 12, 34, 35, 300000, 123321)
print(t_5)
print("-" * 30)

print(t_5.year)
print(t_5.day)
print(t_5.month)
print(t_5.hour)
print(t_5.minute)
print(t_5.nanosecond)
print(t_5.dayofweek)
print(t_5.dayofyear)
print(t_5.week)
print(t_5.weekofyear)
print(t_5.days_in_month)
print(t_5.is_leap_year)
print(t_5.is_month_end)
print(t_5.is_month_start)
print(t_5.is_quarter_end)
print(t_5.is_quarter_start)
print(t_5.is_year_end)
print(t_5.is_year_start)
print(t_5.quarter)
print(t_5.value)
print("#" * 30)

t_tz = pd.Timestamp('2018-12-13 12:00')
print(t_tz.tzinfo)  # タイムゾーンを指定していないので何も返らない
t_tz = t_tz.tz_localize('utc')  # 協定世界時(UTC)にタイムゾーンを設定
print(t_tz.tzinfo)
print("-" * 30)

print(pytz.all_timezones)
print("-" * 30)

print(t_tz)
t_tz = t_tz.tz_convert('Asia/Tokyo')
print(t_tz)

t_tz = t_tz.tz_convert('America/Chicago')
print(t_tz)
print("-" * 30)

print(t_tz.tz_convert(None))  # UTCのものに戻してタイムゾーンを削除
print(t_tz.tz_localize(None))  # 現在表示している時刻をそのまま残してタイムゾーンを削除
print("#" * 30)

t_tz = t_tz.tz_convert('America/Chicago')
print(t_tz)

t = pd.Timestamp(2018, 12, 10)
print(t)

print(t + offsets.Day(3))  # 3日後
print(t - offsets.Day(3))  # 3日前
print(t + offsets.Hour(3))  # 3時間ご
print(t + offsets.YearEnd())  # 年末
print("#" * 30)

delta = t - pd.Timestamp(2018, 12, 8, 22, 32)
print(delta)
print(t_tz + delta)  # timedeltaで足し合わせることもできる
print(t_tz)
