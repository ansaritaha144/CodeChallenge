import requests

response = requests.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')

json_response = response.json()
print(json_response)

source = json_response['source'][0]['annotations']['source_name']
dataset_size = len(json_response['data'])
start_year = json_response['data'][dataset_size-1]['Year']
end_year = json_response['data'][0]['Year']

maxGrowth = 0
minGrowth = 0
peak_growth_year = ''
lowest_growth_year = ''
peak_percent = 0
lowest_percent = 0

for i in range(0, dataset_size - 1):

    difference = json_response['data'][i]['Population'] - json_response['data'][i + 1]['Population']

    if maxGrowth < difference:
        maxGrowth = difference
        peak_growth_year = json_response['data'][i]['Year']
        peak_percent = (difference/json_response['data'][i]['Population'])*100
        peak_percent = round(peak_percent, 2)

    if minGrowth > difference or minGrowth == 0:
        minGrowth = difference
        lowest_growth_year = json_response['data'][i]['Year']
        lowest_percent = (difference / json_response['data'][i]['Population'])*100
        lowest_percent = round(lowest_percent, 2)


print('According to ' + source + ', in ' + str(dataset_size) + ' years from ' + start_year + ' to ' + end_year + ', peak population growth was ' + str(peak_percent) + '% in ' + peak_growth_year + ' and the lowest population increase was ' + str(lowest_percent) + '% in ' + lowest_growth_year + '.')
