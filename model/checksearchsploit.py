import subprocess

def check_searchsploit(versions):
	output = ""
	for version in versions:
		 command = "searchsploit " + version
		 result = subprocess.run(command, shell=True, capture_output=True, text=True, errors='ignore')
		 if result.returncode == 0:
		     output += version + ": \n"
		     output += result.stdout + "\n"
		 else:
		     error = result.stderr
		     output += error + "\n"
	return output
