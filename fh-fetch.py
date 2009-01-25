#!/usr/bin/python
# Fetch the specified entries.
# Arguments : fh-fetch 	from 	date [to date]
#                     	feeds	*feed-name-regexp*
#			show	feed-title,entry-title,entry-contents

import os
import glob
import feedparser

dir = glob.iglob(os.environ.get("HOME") + "/.fh/feeds/*")

for file in dir:
        feed = feedparser.parse(file)
        print feed.feed.subtitle

        for e in feed.entries:
            print e.title
