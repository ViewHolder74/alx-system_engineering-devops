#!/usr/bin/env ruby
# This script validate the regular expression
# must be only matching: capital letters

puts ARGV[0].scan(/[A-Z]/).join
