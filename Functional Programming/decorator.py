def whisper_decorator(func):
    def wrapper():
        return "..." + func() + "..."
    return wrapper


def yell_decorator(func):
    def wrapper():
        return func() + "!"
    return wrapper


@whisper_decorator
def whisper_kali_quote():
        return "The Quieter You Are The More You Are Able To Hear"


@yell_decorator
def yell_kali_quote():
        return "The Quieter You Are The More You Are Able To Hear"


print(whisper_kali_quote())
print(yell_kali_quote())
