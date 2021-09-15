
date = x.split()[0]
time = x.rsplit()[-1]
day = date.split('/')[0]
month = date.split('/')[1]
year = date.split('/')[2]
new_x = str(year + '/' + month + '/' + day + ' ' + time)
print(new_x)