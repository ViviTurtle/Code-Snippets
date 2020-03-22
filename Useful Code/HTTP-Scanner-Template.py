#!/usr/bin/env python3
import re
import sys
import argparse
#import cases
import requests
import http.client
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

#Imported from https://stackoverflow.com/questions/20658572/python-requests-print-entire-http-request-raw for Debugging
def pretty_print_REQUEST(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------REQUEST-----------',
        req.method + ' HTTP/v1.1 ',
        "Host: "+ req.url + '\r\n' + '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body +  '\r\n-----------END-----------\r\n',
        
    ))

def pretty_print_RESPONSE(req):
    http_versions = {10: "HTTP/1.0", 11: "HTTP/1.1", 20: "HTTP/2.0"} 
    print('{}{}\r\n{}\r\n\r\n{}'.format(
        '-----------RESPONSE-----------',
        '\r\n' + http_versions[req.raw.version] + str(req.status_code) + " " + http.client.responses[req.status_code],
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.text + '\r\n-----------END-----------\r\n',
    ))

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Edit this description for your scanner')
	parser.add_argument('DOMAIN', metavar='DOMAIN', action='store',
	                    help='a single domain name to scan')
	parser.add_argument('--port', '-p' , default=443, type=int,
	                    help='the port the URL is on')
	parser.add_argument('--debug', default=False, action='store_true',
	                    help='Debug Flag')
	parser.add_argument('--verbose', '-v', default=False, action='store_true',
	                    help='To see actual requests/response')
	parser.add_argument('--output', '-o',  default=False, type=argparse.FileType('w'),
	                    help='File to save output as')

	#TODO Save output to a file 
	args = parser.parse_args()

	if args.debug:
		print(args)

	#Sets Up URL and Port
	host=args.DOMAIN
	#The Port to connect to
	port=args.port
	if (port == 443):
		host_url = f"https://{host}"
	if (port == 80):
		host_url = f"http://{host}"

	#Setting up Request
	headers = {'User-Agent': "BugBounty-Vivi", "Transfer-Encoding": "chunked", "Content-Length": "0"}
	post_data = 'Random POST  Data'
	r = requests.Request('POST', host_url, headers=headers, data=post_data)
	prepared = r.prepare()
	if args.verbose or args.debug:
		pretty_print_REQUEST(prepared)

	#Send Request
	s = requests.Session()
	try:
		response = s.send(prepared, timeout=5, verify=False)
		if args.verbose or args.debug:
			pretty_print_RESPONSE(response)

	except requests.exceptions.Timeout:
		print(f"\033[91m{host_url} - Request Timed Out\033[0m")
		return
	print(f"\033[1m{host_url} - Request went through\033[0m")
