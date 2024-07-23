import json
import csv
import requests
file = requests.get("https://clinicaltrials.gov/api/v2/studies?query.cond=heart+attack&postFilter.overallStatus=TERMINATED")
text = json.loads(file.text)
first_column = ['official tile','brief tile','official title','eligibility criteria','','','Why Stopped']
names = []
f=open('terminated.csv','w')
writer = csv.writer(f)
writer.writerow(first_column)
empty_col = ['']
second_column = empty_col*3 + ['Sex','MinimumAge'] 
official_titles = []
eligibility_criteria = []
brief_tile = []
writer.writerow(second_column)
row=[]
index=0
for info in text['studies']:
    columns=[]
    columns.append(info['protocolSection']['identificationModule']['officialTitle'])
    columns.append(info['protocolSection']['identificationModule']['briefTitle'])
    columns.append('')
    columns.append(info['protocolSection']['eligibilityModule']['sex'])
    minimum_age = info['protocolSection']['eligibilityModule'].get('minimumAge', 'None')
    columns.append(minimum_age)
    columns.append('')     
    whyStopped = info['protocolSection']['statusModule'].get('whyStopped', 'None')
    columns.append(whyStopped)
    row.insert(index,columns)
    index+=1

for rows  in range (len(row)):
    writer.writerow(row[rows])