#!/usr/bin/env python3

def whisper_decorator(func):
    def wrapper():
        return "..." + func().lower() + "..."
    return wrapper


def yell_decorator(func):
    def wrapper():
        return func().upper() + "!"
    return wrapper


@whisper_decorator
def whisper_kali_quote():
        return "The Quieter You Are The More You Are Able To Hear"

@yell_decorator
def yell_kali_quote():
        return "The Quieter You Are The More You Are Able To Hear"


print(whisper_kali_quote())
assert whisper_kali_quote() == "...the quieter you are the more you are able to hear...", "Fix your code"

print(yell_kali_quote())
assert yell_kali_quote() == "THE QUIETER YOU ARE THE MORE YOU ARE ABLE TO HEAR!", "Fix your code"
