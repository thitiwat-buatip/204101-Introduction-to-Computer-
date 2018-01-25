#570610565 Thitiwat Buatip

input_millisec = int(input('Input number ofmilliseconds: '))

millisec = input_millisec%1000

input_sec = input_millisec//1000

sec = input_sec%60

input_minute = input_sec//60
minute = input_minute%60


input_hr = input_minute//60
hr = input_hr%24

input_day = input_hr//24


print(input_day ,'day(s)', hr ,'hour(s)', minute ,'minute(s),', sec ,'second(s), and', millisec, 'millisec(s)')