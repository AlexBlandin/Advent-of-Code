from collections import Counter
from enum import IntEnum
from operator import itemgetter, mul
from pathlib import Path


class Card(IntEnum):
  Ace = 0
  King = 1
  Queen = 2
  Jack = 3
  Ten = 4
  Nine = 5
  Eight = 6
  Seven = 7
  Six = 8
  Five = 9
  Four = 10
  Three = 11
  Two = 12
  Joker = 13


class Kind(IntEnum):
  FiveOfAKind = 0
  FourOfAKind = 1
  FullHouse = 2
  ThreeOfAKind = 3
  TwoPairs = 4
  OnePair = 5
  HighCard = 6


def which(hand: tuple[Card, ...]) -> Kind:
  """Which kind of hand is this?"""
  match Counter(sorted(hand)).most_common():
    case (
      [(_, 4), (Card.Joker, 1)]
      | [(Card.Joker, 4), (_, 1)]
      | [(_, 3), (Card.Joker, 2)]
      | [(Card.Joker, 3), (_, 2)]
      | [(_, 5)]
    ):
      return Kind.FiveOfAKind
    case (
      [(_, 3), (_, 1), (Card.Joker, 1)]
      | [(Card.Joker, 3), (_, 1), (_, 1)]
      | [(_, 2), (Card.Joker, 2), (_, 1)]
      | [(_, 4), (_, 1)]
    ):
      return Kind.FourOfAKind
    case [(_, 2), (_, 2), (Card.Joker, 1)] | [(_, 3), (_, 2)]:
      return Kind.FullHouse
    case (
      [(_, 2), (_, 1), (_, 1), (Card.Joker, 1)]
      | [(Card.Joker, 2), (_, 1), (_, 1), (_, 1)]
      | [(_, 3), (_, 1), (_, 1)]
    ):
      return Kind.ThreeOfAKind
    case [(_, 2), (_, 2), (_, 1)]:
      return Kind.TwoPairs
    case [(_, 1), (_, 1), (_, 1), (_, 1), (Card.Joker, 1)] | [(_, 2), (_, 1), (_, 1), (_, 1)]:
      return Kind.OnePair
    case [(_, 1), (_, 1), (_, 1), (_, 1), (_, 1)]:
      return Kind.HighCard


def hand_with_jacks(hand: str) -> tuple[Card, ...]:
  return tuple(map({k: Card(i) for i, k in enumerate("AKQJT98765432")}.__getitem__, hand))


def hand_with_jokers(hand: str) -> tuple[Card, ...]:
  return tuple(map({k: Card(i) for i, k in enumerate("AKQ_T98765432J")}.__getitem__, hand))


def rank(hands: list[tuple[Card, ...]], bets: list[int]):
  return sorted(zip(map(which, hands), hands, bets, strict=True), key=itemgetter(0, 1))


def score(ranks: list[tuple[Kind, tuple[Card, ...], int]]):
  return sum(map(mul, map(itemgetter(2), reversed(ranks)), range(1, len(ranks) + 1)))


lines = list(map(str.split, Path("day7.txt").read_text().splitlines()))
hands, bets = list(map(itemgetter(0), lines)), list(map(int, map(itemgetter(1), lines)))
print(
  score(rank(list(map(hand_with_jacks, hands)), bets)),
  score(rank(list(map(hand_with_jokers, hands)), bets)),
)
