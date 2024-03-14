#!/usr/bin/python3
""" Determine who the winner of each game is. """


def isWinner(x, nums):
    # Function to check if a number is prime
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    # Function to simulate a round of the game and determine the winner
    def game(n):
        # Generate a list of prime numbers from 2 to n
        primes = [i for i in range(2, n+1) if is_prime(i)]
        # If the number of primes is odd, Maria wins (since she goes first)
        # If the number of primes is even, Ben wins
        return len(primes) % 2 == 1

    # Count the number of rounds Maria wins
    Maria_wins = sum(game(n) for n in nums)
    # The number of rounds Ben wins is the total number of rounds minus,
    # the number of rounds Maria wins
    Ben_wins = x - Maria_wins

    # Determine the overall winner
    if Maria_wins > Ben_wins:
        return 'Maria'
    elif Ben_wins > Maria_wins:
        return 'Ben'
    else:
        return None
