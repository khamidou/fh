#!/usr/bin/ruby
#
# Fetch the specified entries.
# Arguments : fh-fetch 	from 	date [to date]
#                     	feeds	*feed-name-regexp*
#			show	feed-title,entry-title,entry-contents

require "feedparser"

fh_to = Time.new()
fh_from = fh_to - 2592000 # It's yesterday

feeds = "*"

# This hash holds what elements we display.
# By default, only show the titles of the feeds
show = { "feedtitle" => 1, "entry-title" => 1, "entry-contents" => 0 }
 
cwd = Dir.getwd

# if ARGV.length == 0
#   puts "fh-fetch from date [to date]"
#   puts "	 feeds *feed-name-regexp*"
# end

ARGV.length.times do | i |
  if (ARGV[i] == "from")
    fh_from = Time.parse(ARGV[i+1])
    
  end
  
  if (ARGV[i] == "to")
    fh_to = Time.parse(ARGV[i+1])
  end

  if (ARGV[i] == "feeds")
    feeds = ARGV[i+1]
  end
  
  if (ARGV[i] == "show")
    show = {}
    ARGV[i+1].split(",").each { | elem |
      if (elem == "ftitle" || elem == "feed-title")
        show["feedtitle"] = 1
      end
    }
  end
end


Dir.chdir(ENV["HOME"] + "/.fh/feeds/")

Dir[feeds].each { | file | 
  if file != "." && file != ".."
    s = File.read(file)
    f = FeedParser::Feed::new(s)

    if (show["feed-title"])
      print f.title, "\t"
    end

    f.items.each { |e|
    
      if (show["entry-title"])
        print e.title, "\t\t"
      end
      if (show["entry-contents"])
        print e.to_s, "\t\t\t"
      end
    }
  end
}

Dir.chdir(cwd)
