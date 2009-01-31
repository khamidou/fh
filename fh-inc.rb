#!/usr/bin/ruby
#
# fh-inc - get data from the feeds refered in ~/.fh/feedlist

require 'net/http'
require 'uri'

fd = File.new(ENV["HOME"] + "/.fh/feedlist")

counter = 0

fd.each_line do |line|
  line = line.chomp
  if line != ""
    s = Net::HTTP::get URI::parse(line)
    
    # Each file is named according to the url of the feed.
    fname = line.gsub("http://", "")
    fname.gsub!("/", "-")

    File.open(ENV["HOME"] + "/.fh/feeds/" + fname, "w+") do |ff|
      ff.write(s)
    end

    counter += 1
  end
end

print "Fetched ", counter, " feeds\n"
