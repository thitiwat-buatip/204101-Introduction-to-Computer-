# 570610565 Thitiwat buatip Lab 02 ข้อ 5

input_millisec = int(input('Input number of milliseconds: '))

millisec = input_millisec%1000
input_sec = input_millisec//1000

sec = input_sec%60
input_minute = input_sec//60

minute = input_minute%60
input_hr = input_minute//60

hr = input_hr%24
day = input_hr//24


print("Results =", day ,'day(s),', hr ,'hour(s),', minute ,'minute(s),', sec ,'second(s), and', millisec, 'millisec(s)')