import re

def version_number_split(input_string):
   pattern = r'\b([a-zA-Z]+)\s+(\d{1,2}\.\d{1,2}\.\d{1,2})\b'
    # Use re.findall() to find all matches in the input string
   matches = re.findall(pattern, input_string)
    # Return a list of "name version number" pairs
   return [f"{match[0]} {match[1]}" for match in matches]

def manipulate_and_group_versions(banner):
	banner = banner.replace(",","")
	banner = re.sub(r'(?<!\d)(\d+)\.(\d+)\.(\d+)(?!\d)', r'\1.\2.\3', banner)
	banner = re.sub(r'/', ' ', banner)
	versions = version_number_split(banner)
	return versions
