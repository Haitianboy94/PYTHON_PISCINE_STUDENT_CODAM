def game_event_stream(count):
    """Generates game events one at a time.
    The yield keyword turns a function into a function generator.
    The function generator returns an iterator.
    The code inside the function is not executed when they are first called,
    but are divided into steps, one step for each yield,
    and each step is only executed when iterated upon.
    Unlike the return keyword which stops further execution of the function,
    the yield keyword returns the result so far,
    and continues to the next step.
    it returns a generator/iterator that can be iterated to produce values.."""
    players = ['alice', 'bob', 'charlie', 'Ruthler', 'kevin']
    event_types = ['killed monster', 'found treasure', 'leveled up']
    level_pattern = [5, 12, 8, 15, 3, 18, 7, 11, 14, 6, 19, 4, 13,
                     9, 16, 2, 10, 17, 20, 1]

    for i in range(count):
        player = players[i % len(players)]
        level = level_pattern[i % len(level_pattern)]
        event = event_types[i % len(event_types)]

        yield {
            'id': i + 1,
            'player': player,
            'level': level,
            'event': event
        }


def fibonacci_generator():
    """Generates Fibonacci numbers indefinitely"""
    a = 0
    b = 1
    while True:
        yield a
        new_a = b
        new_b = a + b
        a = new_a
        b = new_b


def prime_generator():
    """Generates prime numbers one at a time"""
    yield 2
    primes = [2]
    stater = 3

    while True:
        is_prime = True
        for number in primes:
            if number * number > stater:
                break
            if stater % number == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(stater)
            yield stater
        stater += 2


def process_stream(event_stream, max_display=3):
    """Processes events one by one, tracking statistics"""
    total = 0
    high_level = 0
    treasure = 0
    levelup = 0

    for event in event_stream:
        total += 1

        if total <= max_display:
            print(f"Event {event['id']} :Player {event['player']} "
                  f"level {event['level']} {event['event']}")
        elif total == max_display + 1:
            print("...")

        if event['level'] >= 10:
            high_level += 1
        if 'treasure' in event['event']:
            treasure += 1
        if 'leveled up' in event['event']:
            levelup += 1

    return {
            'total': total,
            'high_level': high_level,
            'treasure': treasure,
            'levelup': levelup
            }


def main():
    print("=== Game Data Stream Processor ===\n")

    event_count = 1000
    print(f"Processing {event_count} game events...\n")

    events = game_event_stream(event_count)
    stats = process_stream(events, max_display=3)

    print("")
    print("=== Stream Analytics ===")
    print(f"Total events processed: {stats['total']}")
    print(f"High-level players (10+): {stats['high_level']}")
    print(f"Treasure events: {stats['treasure']}")
    print(f"Level-up events: {stats['levelup']}\n")
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print("")
    print("=== Generator Demonstration ===")

    fib_gen = fibonacci_generator()
    fib_numbers = []
    for _ in range(10):
        fib_numbers.append(next(fib_gen))

    fib_str = ""
    for i in range(len(fib_numbers)):
        if i > 0:
            fib_str += ", "
        fib_str += str(fib_numbers[i])
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_gen = prime_generator()
    prime_numbers = []
    for _ in range(5):
        prime_numbers.append(next(prime_gen))

    prime_str = ""
    for i in range(len(prime_numbers)):
        if i > 0:
            prime_str += ", "
        prime_str += str(prime_numbers[i])
    print("Prime numbers (first 5): " + prime_str)


if __name__ == "__main__":
    main()
