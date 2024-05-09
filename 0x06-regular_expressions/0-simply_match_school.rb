#!/usr/bin/env ruby

require 'oniguruma'

def check_for_school(text)
  # Oniguruma regex for "School" (case-insensitive)
  school_regex = Oniguruma::ORegex.new("School", options: Oniguruma::OPTION_IGNORECASE)

  # Check if the argument matches the regex
  match = school_regex.match(text)

  if match
    puts "The string '#{text}' contains 'School'."
  else
    puts "The string '#{text}' does not contain 'School'."
  end
end

# Get the argument from the command line (if any)
argument = ARGV.first

# Check if an argument was provided
if argument
  check_for_school(argument)
else
  puts "Please provide a string as an argument."
end
