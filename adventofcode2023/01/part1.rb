sum = 0
File.readlines('input.txt').each do |line|
  first_num = nil
  last_num = nil
  line.each_char do |char|
    first_num = char if char =~ /[0-9]/ and first_num.nil?
    last_num = char if char =~ /[0-9]/
  end

  line_sum = (first_num + last_num).to_i
  sum += line_sum
end

puts sum
