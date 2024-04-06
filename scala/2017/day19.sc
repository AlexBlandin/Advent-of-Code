import scala.io.Source
import collection.mutable
val file = Source.fromFile("day19.txt")
val lines = file.getLines.toArray

@main
def solve() = {
  s"Hello! ${42}"
}

@main
def test() = {
  s"Tests! ${24}"
}

file.close
