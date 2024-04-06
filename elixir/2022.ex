defmodule Day1 do
  def greet do
    d = data()
    IO.puts "Greetings! #{part1(d)} #{part2(d)}"
  end

  def data, do: File.read!("2022/day1.txt")
                |> String.split("\n\n")
                |> Enum.map(fn elf -> String.split(elf)
                                      |> Enum.map(&String.to_integer/1)
                                      |> Enum.sum end)
                |> Enum.sort()
                |> List.to_tuple

  def part1(d) do
    elem(d, tuple_size(d) - 1)
  end

  def part2(d) do
    elem(d, tuple_size(d) - 1) + elem(d, tuple_size(d) - 2) + elem(d, tuple_size(d) - 3)
  end
end

defmodule Day2 do
  def greet do
    d = data()
    IO.puts "Salut! #{} #{}"
  end

  def rps(c) do
    <<a, _, b::utf8>> = c
    elf = case a do
      ?A -> :a
      ?B -> :b
      ?C -> :c
    end
    me = case b do
      ?X -> :x
      ?Y -> :y
      ?Z -> :z
    end
    {elf, me}
  end

  def data do
    File.read!("2022/day2.txt")
    |> String.split("\n")
    |> Enum.map(&rps/1)
  end
end

defmodule Day3 do
  def greet do
    IO.puts "Begrüßungen! #{} #{}"
  end
end

defmodule Day4 do
  def greet do
    IO.puts "Saudações! #{} #{}"
  end
end

defmodule Day5 do
  def greet do
    IO.puts "Pozdrowienia! #{} #{}"
  end
end

defmodule Day6 do
  def greet do
    IO.puts "Salutoj! #{} #{}"
  end
end

defmodule Day7 do
  def greet do
    IO.puts "Tervehdykset! #{} #{}"
  end
end

defmodule Day8 do
  def greet do
    IO.puts "χαιρετισμοί! #{} #{}"
  end
end

defmodule Day9 do
  def greet do
    IO.puts "تحيات! #{} #{}"
  end
end

defmodule Day10 do
  def greet do
    IO.puts "Dagsê! #{} #{}"
  end
end

defmodule Day11 do
  def greet do
    IO.puts "Köszönések! #{} #{}"
  end
end

defmodule Day12 do
  def greet do
    IO.puts "Begroetingen! #{} #{}"
  end
end

defmodule Day13 do
  def greet do
    IO.puts "приветствия! #{} #{}"
  end
end

defmodule Day14 do
  def greet do
    IO.puts "Kveðjur! #{} #{}"
  end
end

defmodule Day15 do
  def greet do
    IO.puts "挨拶! #{} #{}"
  end
end

defmodule Day16 do
  def greet do
    IO.puts "поздрави! #{} #{}"
  end
end

defmodule Day17 do
  def greet do
    IO.puts "인사! #{} #{}"
  end
end

defmodule Day18 do
  def greet do
    IO.puts "Sveicināšanās! #{} #{}"
  end
end

defmodule Day19 do
  def greet do
    IO.puts "Hilsener! #{} #{}"
  end
end

defmodule Day20 do
  def greet do
    IO.puts "Salamu! #{} #{}"
  end
end

defmodule Day21 do
  def greet do
    IO.puts "Hälsningsfraser! #{} #{}"
  end
end

defmodule Day22 do
  def greet do
    IO.puts "ทักทาย! #{} #{}"
  end
end

defmodule Day23 do
  def greet do
    IO.puts "Lời chào! #{} #{}"
  end
end

defmodule Day24 do
  def greet do
    IO.puts "打招呼! #{} #{}"
  end
end

defmodule Day25 do
  def greet do
    IO.puts "Llongyfarchiadau! #{} #{}"
  end
end

Day1.greet(); Day2.greet(); Day3.greet(); Day4.greet(); Day5.greet(); Day6.greet(); Day7.greet(); Day8.greet(); Day9.greet(); Day10.greet(); Day11.greet(); Day12.greet(); Day13.greet(); Day14.greet(); Day15.greet(); Day16.greet(); Day17.greet(); Day18.greet(); Day19.greet(); Day20.greet(); Day21.greet(); Day22.greet(); Day23.greet(); Day24.greet(); Day25.greet()
