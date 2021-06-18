import random
import matplotlib.pyplot as plt

import fire

low = 0
high = 7

def chunks(lst, n):
  """Yield successive n-sized chunks from lst.

  Args:
    lst (list): The list to generate chunks from.
    n (int): Size of the chunks.

  Yields:
    [list]: The next chunk.
  """
  for i in range(0, len(lst), n):
    yield lst[i:i + n]


def weighted_random(low=low, high=high):
  """Generates a weighted random number.

  Args:
    low (float): The lowest possible value.
    high (float): The highest possible value.

  Returns:
    int: Weighted random number.
  """
  return int(random.triangular(low, high + 1, low))


def plot(iterations, low=low, high=high):
  """Plots the weighted_random function.

  Args:
    iterations (int): The number of values to generate.
    low (float): The lowest possible value.
    high (float): The highest possible value.
  """
  s = [weighted_random(low, high) for _ in range(iterations)]
  _ = plt.hist(s, bins='auto')
  plt.show()


def calculate_scores(*teams):
  """Calculates and prints the scores for the given teams.

  Args:
    teams (list): The teams grouped by brackets.
  """
  brackets = chunks(teams, 2)


  for bracket in brackets:
    scores = [weighted_random(low, high) for _ in bracket]

    for team, score in zip(bracket, scores):
      print(f"{team}: {score}")
      
    print()


if __name__ == "__main__":
  fire.Fire()
