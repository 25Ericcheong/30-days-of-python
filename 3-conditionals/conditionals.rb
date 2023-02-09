#!/bin/ruby

require 'json'
require 'stringio'



N = gets.strip.to_i

if N % 2 == 0
    if N >= 2
        if N < 6
            puts "Not Weird"
        else
            if N < 21
                puts "Weird"
            else
                puts "Not Weird"
            end
        end 
        
    end
else
    puts "Weird"
end
