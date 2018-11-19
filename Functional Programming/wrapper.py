def whisper(text):
    return "..."+text.lower()+"..."

def yell(text):
    return text.upper()+"!"


def say_kali_quote_wrapper(say_type):
    print(say_type("The Quieter You Are The More You Are Able To Hear"))

say_kali_quote_wrapper(whisper)

say_kali_quote_wrapper(yell)

