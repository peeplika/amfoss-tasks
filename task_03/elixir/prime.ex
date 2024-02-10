defmodule PrimeChecker do
  def is_prime?(n) when n <= 1, do: false
  def is_prime?(n) when n == 2, do: true
  def is_prime?(n) do
    Enum.reduce(2..(n-1), true, fn divisor, acc ->
      acc && rem(n, divisor) != 0
    end)
  end
end

IO.puts "Enter a positive number: "
n = IO.gets("") |> String.trim() |> String.to_integer()

if n <= 0 do
  IO.puts "Not valid"
else
  Enum.each(2..n, fn element ->
    if PrimeChecker.is_prime?(element) do
      IO.puts element
    end
  end)
end


