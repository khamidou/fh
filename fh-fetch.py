#!/usr/bin/python
# Fetch the specified entries.
# Arguments : fh-fetch 	from 	date [to date]
#                     	feeds	*feed-name-regexp*
#			show	feed-title,entry-title,entry-contents

import os
import sys
import glob
import feedparser

fetch_params = { "show-subtitle": 1, "show-titles": 1, "show-subtitles": 1, "show-content": 1, }

# Parses a string of the form arg1,arg2,arg3
# If an element is present, put its value to one in fetch_params.
def parse_arg_list(str):
	for item in sys.argv[i].strip(","):
		fetch_params[item] = 1

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
		if fetch_params["show-subtitle"]:
			print feed.feed.subtitle

		for e in feed.entries:
			if fetch_params["show-subtitles"]:
				print e.title
				print "\t"

			if fetch_params["show-content"]:
				if feed.feed.has_key("description"):
					print e.description
				elif feed.feed.has_key("content"):
					print e.content
				print "\t"
					
			print "\n"
if __name__ == "__main__":
	main()
