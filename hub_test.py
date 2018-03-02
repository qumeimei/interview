'''
'''

import requests
import json,sys,datetime
from pprint import pprint
import collections
from collections import OrderedDict

'''
The main function will Get a json file, find the dates for each country that 
the most people could attend in two consecutive days,return the dates as strings 
and POST the countries with the dates as JSON properties to the given API.
'''

# group the partner by country
def group_by_country(partners):
	countries=OrderedDict()
	for li in partners:
		key=li['country']
		if key in countries:
			countries[key].append(li)
		else:
			countries[key]=[li]
	
	#print "@@@",sort_countries	
	print '@@@countries'
	return countries

# dertermine if given two days are consecutive days
def is_consecutive_days(day1,day2):
	day1=convert_time_format(day1)
	day2=convert_time_format(day2)
	delta=day2-day1
	return delta.days==1

# convert string to datetime
def convert_time_format(day):
	return datetime.datetime.strptime(day, "%Y-%m-%d").date()

# calculate the best start date for all contries
def start_date(countries):
	start_date_contries=OrderedDict()
	for country in countries:

		num,start_date,attendees_email=find_start_date(countries[country])
		start_date_contries[country.encode('ascii', 'ignore')]=(start_date,num,attendees_email)


	return start_date_contries
	
	# return sroted(start_date_contries.items())

# find the best start date for each country
def find_start_date(partners_one_country):
	#print partners_one_country

	available_dates=OrderedDict()
	for partner in partners_one_country:
		dates=partner["availableDates"]
		dates.sort()

		for idx, val in enumerate(dates):
			if(idx<len(dates)-1):
				if (is_consecutive_days(val,dates[idx+1])):
					if val in available_dates:
						available_dates[val.encode('ascii', 'ignore')].append(partner["email"].encode('ascii', 'ignore'))
					else:
						available_dates[val.encode('ascii', 'ignore')]=[partner["email"].encode('ascii', 'ignore')]

	
	# print len(available_dates)
	if(len(available_dates)==0):
		return (0,None,[])

	# print available_dates

	max_attend=0
	key=""
	for k,v in available_dates.items():
		if(len(v)>max_attend):
			key=k
			max_attend=len(v)


	arr=available_dates[key]
	arr.sort()

	#return null
	# print  '@@@',max((len(v), k,v) for k,v in available_dates.iteritems()),'/n'
	# print '@@',max_attend,key,available_dates[key]
	return max_attend,key,arr

def format(start_date_contries):
	country_array=[]
	# sort_di=collections.OrderedDict(sorted(start_date_contries.items()))
	for country,val in start_date_contries.items():
		item_dic=OrderedDict()
		item_dic["attendeeCount"]=val[1]
		item_dic["attendees"]=val[2]
		item_dic["name"]=country
		item_dic["startDate"]=val[0]
		country_array.append(item_dic)
		
	return {'countries':country_array}
	

# program starts here
if __name__ == '__main__':

	

	URL =
	# sending get request and saving the response as response object
	r = requests.get(url=URL)
	data = r.json()
	partners=data['partners']
	#group the partner by country
	countries=group_by_country(partners)
	#get the best start date with maximal partner for each country
	start_date_contries=start_date(countries)
	#format the data according to the requirement
	res=format(start_date_contries)
	#print '@',country_array[0]
	
	result=json.dumps(res)
	print '@@@@@@@',result
	


	r = requests.post
	print r.status_code
	print r.json()

	#print json.dumps(country_array, indent=4, sort_keys=True)








    
	
