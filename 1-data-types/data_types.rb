i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
ii = gets.to_i
dd = gets.to_f
ss = gets.rstrip

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.
puts "#{i + ii}"

# Print the sum of the double variables on a new line.
puts sprintf('%.1f', (d + dd).round(1))

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
puts s + ss
