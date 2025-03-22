def reverse_string(text):
    return text[::-1]

def reverse_list(data):
    return data[::-1]

def reverse_number(number):
    return int(str(number)[::-1])

def reverse_sentence(sentence):
    return " ".join(sentence.split()[::-1])

def reverse_everything(thing):
    try:
        if isinstance(thing, str):
            return reverse_string(thing)
        elif isinstance(thing, list):
            return reverse_list(thing)
        elif isinstance(thing, int) or isinstance(thing, float):
            return reverse_number(thing)
        elif isinstance(thing, dict):
            reversed_dict = {value: key for key, value in thing.items()}
            return reversed_dict
        elif isinstance(thing, tuple):
            return tuple(reversed(thing))
        else:
            return "Could not reverse this type of thing!"
    except:
        return "An error occured while attempting to reverse."
