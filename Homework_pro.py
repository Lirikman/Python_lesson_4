#1 В файле с логами найти дату самого позднего лога (по метке времени)
import re
with open('log', encoding='utf-8') as file:
    text = file.read()

time = re.findall(r'\d\d:\d\d:\d\d', text)
time.sort()

date = text.find(time[-1])

print('Дата самого позднего лога по метке времни:', text[(date-11):date])