import time

import pandas as pd

str_1 = '2019/04/07'

print(pd.to_datetime(str_1))
print("-" * 30)

t_str = '20190407'
print(pd.to_datetime(t_str))
print("-" * 30)

time_sr = pd.Series([20181024, 20200915, 20210111])
convert_time = pd.to_datetime(time_sr, format='%Y%m%d')
print(convert_time)

time_sr_2 = pd.Series(['181024 13:24', '200915 07:59', '210111 23:45'])
print(pd.to_datetime(time_sr_2, format='%y%m%d %H:%M'))
print("-" * 30)

time_j = "2018年12月12日 05時25分"
print(pd.to_datetime(time_j, format='%Y年%m月%d日 %H時%M分'))
print("#" * 30)

print(pd.to_datetime(1537417500, unit='s'))
print("-" * 30)

print(pd.to_datetime(1537417500, unit='s').tz_localize('utc').tz_convert('Asia/Tokyo'))

utc_time = pd.to_datetime(1537417500, utc=True, unit='s')

print(utc_time)
print(utc_time.tz_convert('Asia/Tokyo'))
print("-" * 30)

print(pd.to_datetime(1537417500293410982, unit='ns'))
print("-" * 30)

print(pd.to_datetime(1537417500293, unit='ms'))
print("#" * 30)

long_t = pd.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 2000)

start_time = time.time()
pd.to_datetime(long_t, infer_datetime_format=False)  # デフォルト
print(time.time() - start_time)

start_time = time.time()
pd.to_datetime(long_t, infer_datetime_format=True)
print(time.time() - start_time)

# start_time = time.time()
# pd.to_datetime(long_t, format='%d/%m/%Y')  # フォーマット指定
# print(time.time() - start_time)
print("#" * 30)

df = pd.DataFrame(
    {
        'year': [1998, 2012, 1990, 2018],
        'month': [10, 1, 10, 12],
        'day': [10, 11, 21, 1],
        'hour': [12, 23, 14, 1],
        'minute': [29, 3, 30, 59]
    }
)

print(pd.to_datetime(df))