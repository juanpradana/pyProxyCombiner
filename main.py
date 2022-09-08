import requests

proxys = [
	'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
	'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt',
	'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
	'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
	'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
	'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks5.txt',
	'https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt',
	'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt',
	'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt',
	'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt',
	'https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt',
	'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt',
	'https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt'
	]

f = open("pl.txt", 'w')
f.write("")
f.close()

for proxy in proxys:
	x = requests.get(proxy)
	f = open("pl.txt", 'a')
	f.write(x.text)
	f.close()