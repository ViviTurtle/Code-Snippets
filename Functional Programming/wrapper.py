#!/usr/bin/env python3

def whisper(text):
    return "..."+text.lower()+"..."

def yell(text):
    return text.upper()+"!"


def say_kali_quote_wrapper(say_type):
    print(say_type("The Quieter You Are The More You Are Able To Hear"))
    return say_type("The Quieter You Are The More You Are Able To Hear")


assert say_kali_quote_wrapper(whisper) == "...the quieter you are the more you are able to hear...", "Fix your code"

assert say_kali_quote_wrapper(yell) == "THE QUIETER YOU ARE THE MORE YOU ARE ABLE TO HEAR!", "Fix your code"
