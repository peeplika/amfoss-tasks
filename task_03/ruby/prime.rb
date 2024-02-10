puts "enter a positive number"
n = gets.chomp.to_i
for i in 2..n do
  isprime = true
  for j in 2..(i-1) do
    if i%j == 0 
      then isprime= false
      break
    end
  end  
  if isprime == true
    puts "#{i}"      
    end   
end


