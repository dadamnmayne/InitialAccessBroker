import re
import requests

def extract_proper_nouns(url):
	# Fetch the webpage content
	response = requests.get(url)
	if response.status_code == 200:
		# Extract text from HTML content
		text = response.text
		# Regular expression pattern to match phrases with words that begin with a capital letter
		pattern = r'\b[A-Z][a-zA-Z]*\b(?:\s+[A-Z][a-zA-Z]*\b)*(?!\s+[a-z])'
		# Find all matches in the text
		matches = re.findall(pattern, text)
		print("Proper Nouns Found (Dirty List):")
		for phrase in matches:
			print(phrase)
		return None
	else:
		print("Failed to fetch the webpage.")
		return None
