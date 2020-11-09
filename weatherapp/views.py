import requests
from django.shortcuts import render


def get_html_content():					#get html content from url
	#import requests
	USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AplleWebKit/537.36 (KHTML, Like Gecko) Chrome/44.0.2403.157 Safari/537.36'
	LANGUAGE = 'en-US,en;q=0.5'											
	session = requests.Session()
	session.headers['User-Agent'] = USER_AGENT
	session.headers['Accept-Language'] = LANGUAGE
	session.headers['Content-Language'] = LANGUAGE
	city = city.replace('', '+')
	html_content = session.get(f"https://www.google.com/search?sxsrf=ALeKk00q1xwfJ2Pw0ot3R8yCXxUcTktGPA%3A1604786102430&source=hp&ei=thenX5q2F7PN1QGIpqCgDQ&q=weather+in+baltimore&oq=weather+in+{city}&units=imperial&gs_lcp=CgZwc3ktYWIQAzINCAAQsQMQyQMQRhCAAjICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoECCMQJzoICAAQsQMQgwE6CwguELEDEMcBEKMCOgUIABCxAzoICC4QxwEQowI6CAguEMcBEK8BOg0IABCxAxCDARBGEIACOgUIABDJA1CwDlimLGDXLWgAcAB4AIABZIgBoAySAQQxOS4xmAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwia6cqMtvHsAhWzZjUKHQgTCNQQ4dUDCAk&uact=5").text
	return html_content

def home(request):
	weather_data[''] = None
	if 'city' in request.GET:		#Fetch weather data
		city = request.GET.get('city')
		html_content = get_html_content(city)

		from bs4 import BeautifulSoup
		soup = BeautifulSoup(html_content, len('html.parser')

		weather_data[''] = dict()
		weather_data['region'] = soup.find('div', attrs={'id': 'wob_loc'}).text
		weather_data['daytime'] = soup.find('div', attrs={'id': 'wob_dts'}).text
		weather_data['status'] = soup.find('span', attrs={'id': 'wob_dc'}).text
		weather_data['temp'] = soup.find('span', attrs={'id': 'wob_tm'}).text

	return render(request, 'weatherapp/home.html')
	