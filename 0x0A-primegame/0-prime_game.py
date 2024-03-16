#!/usr/bin/python3
""" Determine who the winner of each game is. """


def isWinner(x, nums):
    """ Determine who the winner of each game is. """
    if x <= 0 or not nums:
        return None

    # Create a sieve of Eratosthenes to find all the,
    # prime numbers in the range [1, n]
    sieve = [True] * (max(nums) + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max(nums) ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max(nums) + 1, i):
                sieve[j] = False

    # Keep track of the number of wins for each player
    Maria_wins = 0
    Ben_wins = 0

    for n in nums:
        # # Generate a list of prime numbers from 2 to n
        primes = [i for i in range(2, n+1) if sieve[i]]
        # If the number of primes is odd, Maria wins this round
        # If the number of primes is even, Ben wins
        if len(primes) % 2 == 1:
            Maria_wins += 1
        else:
            Ben_wins += 1

    # Determine the overall winner
    if Maria_wins > Ben_wins:
        return 'Maria'
    elif Ben_wins > Maria_wins:
        return 'Ben'
    else:
        return None
