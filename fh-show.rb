#!/usr/bin/ruby
#
# Formats the (piped) output of fh-fetch.
# Arguments : fh-show 
# 


ARGV.length.times do | i |
  
end

# Simply replace tabs by linefeeds.

t = STDIN.read

t.gsub("\t\t\t", "\n")
t.gsub("\t\t", "\n")
t.gsub("\t", "\n")
