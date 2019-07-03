def fizzbuzz(num: int) -> str:
    fizz = "fizz" if num % 3 == 0 else ""
    buzz = "buzz" if num % 5 == 0 else ""
    fizzbuz = fizz + buzz
    return fizzbuz if fizzbuz else str(num)
