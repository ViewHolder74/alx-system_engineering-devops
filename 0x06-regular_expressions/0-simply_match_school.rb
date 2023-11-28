#!/usr/bin/env ruby

def match_school(str)
  puts str.match(/School$/)
end

if ARGV.length == 1
  match_school(ARGV[0])
else
  puts "Usage: #{$PROGRAM_NAME} <string>"
end
