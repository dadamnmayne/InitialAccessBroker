from model.bannergrabber import grab_banner
from model.versionprocessing import manipulate_and_group_versions
from model.checksearchsploit import check_searchsploit
from model.getpropernouns import extract_proper_nouns
import re
import requests
#delete
import subprocess



url = input("URL: ")
banner = grab_banner(url)
versions = manipulate_and_group_versions(banner)
print("\n" + "Reconnaissance Report for " + url)
print("---------------------------------")
print("---------------------------------")
print("---------------------------------")

print("*****TIER 1 RESULTS (SEARCHSPLOIT)*****" + "\n")
print(check_searchsploit(versions))

print("*****TIER 2 RESULTS (SITUATIONAL AWARENESS USING PROPER NOUNS)*****" + "\n")
extract_proper_nouns(url)    	  

print("*****TIER 3 RESULTS (ENUMERATE ENDPOINTS/WEB APP DIRECTORIES)*****" + "\n")

def enumerate_directories(url):
	command = "model/gobuster dir -u http://perfection.htb -w model/directory-list-2.3-big.txt -x txt,php,html -t 16 -r"
	result = subprocess.run(command, shell=True, capture_output=True, text=True, errors='ignore')
	return result
	
enumerate_directories(url)
