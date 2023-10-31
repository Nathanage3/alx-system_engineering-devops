#!/usr/bin/env ruby
log_entry = ARGV[0]
from = log_entry.scan(/\[from:(.*?)\]/).flatten[0]
to = log_entry.scan(/\[to:(.*?)\]/).flatten[0]
flags = log_entry.scan(/\[flags:(.*?)\]/).flatten[0]

puts "#{from},#{to},#{flags}"
