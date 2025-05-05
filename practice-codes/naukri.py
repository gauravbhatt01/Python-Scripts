import requests
import pandas


def send(url, headers, params):
  pass

url = "https://www.naukri.com/jobapi/v3/search"
headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0', 'appid':'110', 'systemid':'Naukri'}
params = {
  'noOfResults': '20',
  'urlType': 'search_by_keyword',
  'searchType':'adv',
  'keyword':'python',
  'pageNo':'1',
  'k':'python',
  'nignbevent_src':'jobsearchDeskGNB',
  'seoKey':'python-jobs',
  'src':'jobsearchDesk'
  'latLong':''
}
	
df = DataFrame()

for i in range(1,5):
  page_number = str(i)
  print(f"Current Page Number is - {page_number}")
  params['pageNo'] = page_number
  datax = send(url, headers, params)
  job_set = (datax["jobDetails"])
  df = df.append(jobs_set)

print("Work Done !! Thank You !!", end="")
df.to_excel("analyst-job-24th-March.xlsx", sheet_name="Jobs")
