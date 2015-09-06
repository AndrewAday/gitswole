#!/usr/bin/env python
import os
import sys
import subprocess
import dateutil.parser
import datetime

print sys.argv[0]
directory = sys.argv[1]
repository = sys.argv[2]
start_date = sys.argv[3]
end_date = sys.argv[4]


dates = []


parser = argparse.ArgumentParser(description='Strengthen that commit history')

def main():
	checkDate(start_date)
	checkDate(end_date)
	# Initialize new git repo
	subprocess.call("mkdir " + repository)
	os.chdir(os.getcwd() + "/" + repository)
	subprocess.call("touch README.md")
	subprocess.call("echo '#The Swolest repo of them all' >> README.md")
	subprocess.call("git init")

	
	with f as open(directory, 'w+'):






def checkDate(date):
	dates = date.split('-')
	if len(dates) != 3 or len(dates[0]) != 4 or len(dates[1]) != 2 or len(dates[2]) != 2:
		sys.exit('improper date format. use YYYY-MM-DD')

def formatCommitDate(date, time):
	return date + ' ' + time + ' -0800'

def calculateDates(start_date, end_date):
	start_date = dateutil.parser.parse(start_date)
	end_date = dateutil.parser.parse(end_date)
	while start_date != end_date:
		dates.append(start_date.year + '-' start_date.month + '-' + start_date.day)
		start_date += datetime.timedelta(days=1)
	dates.append(end_date.year + '-' end_date.month + '-' + end_date.day)









