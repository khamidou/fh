#!/usr/bin/python
# Fetch the specified entries.
# Arguments : fh-fetch 	from 	date [to date]
#                     	feeds	*feed-name-regexp*
#			show	feed-title,entry-title,entry-contents

import os
import sys
import glob
import feedparser

fetch_params = { "feed-title": 1, "feed-summary": 1, "feed-link": 1, "entry-title": 1, "entry-subtitle": 1, "entry-link": 1, "entry-content": 1, }

sep = "" # the separator used to ...separate each entry of the feed
i = 0

# Parses a string of the form arg1,arg2,arg3
# If an element is present, put its value to one in fetch_params.
def parse_arg_list(str):
	fetch_params = {}
	for item in sys.argv[i].strip(","):
		fetch_params[item] = 1

def print_field(field):
	print field.encode("utf8").rstrip("\n")
	print sep

def main():
	for i in range(len(sys.argv[1:])):
		if (sys.argv[i] == "from"):
			pass

		if (sys.argv[i] == "show"):
			i += 1
			parse_arg_list(sys.argv[i])
				

	dir = glob.iglob(os.environ.get("HOME") + "/.fh/feeds/*")

	for file in dir:
		feed = feedparser.parse(file)
		
		if fetch_params["feed-title"]:
			if feed.feed.has_key("title"):
				print_field(feed.feed.subtitle)

 		if fetch_params["feed-summary"]:
 			if feed.feed.has_key("sumary"):
 				print_field(feed.summary)


		for e in feed.entries:

			if fetch_params["entry-subtitle"]:
				print_field(e.title)

			if fetch_params["entry-link"]:
				if feed.feed.has_key("links"):
					print_field(e.links[0]["href"])
			
			if fetch_params["entry-subtitle"]:
				if feed.feed.has_key("description"):
					print_field(e.description)

			if fetch_params["entry-content"]:
				if feed.feed.has_key("content"):
					print_field(e.content[0].value)
					
			print "\n"
if __name__ == "__main__":
	main()
