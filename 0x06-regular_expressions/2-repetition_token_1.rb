#!/usr/bin/env ruby
# This script finds the regular expression that will match the blow cases
# htn
# hbtn
# hbbtn
# hbbbtn

puts ARGV[0].scan(/hb{2,3}tn/).join
