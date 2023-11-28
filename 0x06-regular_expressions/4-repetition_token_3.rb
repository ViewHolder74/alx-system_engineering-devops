#!/usr/bin/env ruby
# This script Find the regular expression that will match the above cases:
# hbn
# hbon
# hbtn
# hbttn
# hbtttn
# hbttttn

puts ARGV[0].scan(/hbt*n/).join
