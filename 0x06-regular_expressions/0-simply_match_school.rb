#!/usr/bin/env ruby

require 'oniguruma'

# Returns true if the text contains "School", false otherwise
# Checks for null pointer references, unhandled exceptions, and more
def check_for_school?(text)
  # If text is nil or empty, return false
  return false if text.nil? || text.empty?

  # If text is not a string, raise a TypeError to alert the user
  raise TypeError, "text is not a string" unless text.is_a?(String)

  # If text contains "School" (case insensitive), return true
  text.downcase.include?("school")
end
# Get the argument from the command line (if any)
argument = ARGV.first

# Check if an argument was provided
if argument
  check_for_school(argument)
else
  # If no argument was provided, print a helpful message
  puts "Please provide a string as an argument."
end
