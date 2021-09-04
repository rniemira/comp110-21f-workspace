"""Repeating a beat in a loop."""

__author__ = "730329962"


beat: str = input("What beat do you want to repeat? ") + " "
times: int = int(input("How many times do you want to repeat it? "))
if times > 0:
    count: int = int(times - 1)
    repeat_beat: str = ""
    i: int = 0
    while i < 1:
        while count > 0:
            repeat_beat += beat
            count = count - 1
        i = i + 1
    print(repeat_beat + beat)
else:
    print("No beat...")