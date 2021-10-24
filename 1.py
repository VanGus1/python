duration = int(input("Введите кол-во секунд для конвертации: "))

seconds = 0
minutes = 0
hours = 0
days = 0

if duration < 60:
	print(str(duration) + "seconds")
elif duration >= 60 and duration < 3600:
	minutes = duration // 60
	seconds = duration - minutes*60
	print(str(minutes) + " minutes " + str(seconds) + " seconds")
elif duration >= 3600 and duration < 86400:
	hours = duration // 3600
	seconds = duration - hours*3600
	minutes = seconds // 60
	seconds = seconds - minutes*60
	print(str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds")
elif duration >= 86400:
	days = duration // 86400
	seconds = duration - days*86400
	hours = seconds // 3600
	seconds = duration - hours*3600 - days*86400
	minutes = seconds // 60
	seconds = seconds - minutes*60
	print(str(days) + " days " + str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds")

input()