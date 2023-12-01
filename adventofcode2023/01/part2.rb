# iterate over all sequential permutations of the string
def strcheck(str)
  (0...str.length).each do |i|
    (i..str.length).each do |j|
      puts "#{str[i]}#{str[j]}"
    end
  end
end

strcheck('siemka')

sum = 0
digits = {
  'one' => '1',
  'two' => '2',
  'three' => '3',
  'four' => '4',
  'five' => '5',
  'six' => '6',
  'seven' => '7',
  'eight' => '8',
  'nine' => '9'
}
File.readlines('sample2.txt').each do |line|
  first_num = nil
  last_num = nil

  str = ''
  line.each_char do |char|
    str += char
    if digits.key?(str) and first_num.nil?
      first_num = digits[str]
      str = char
    end

    if char =~ /[0-9]/ and first_num.nil?
      first_num = char
      str = ''
    end

    if char =~ /[0-9]/
      last_num = char
      str = ''
    end

    if digits.key?(str)
      last_num = digits[str]
      str = ''
    end
  end

  puts "nums for line #{line.strip}: #{first_num} and #{last_num}, str: #{str}"
  line_sum = (first_num + last_num).to_i
  sum += line_sum
end
