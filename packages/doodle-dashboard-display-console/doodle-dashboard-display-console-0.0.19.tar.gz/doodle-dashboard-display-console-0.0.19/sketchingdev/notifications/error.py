def contains_all_in_error_message(error, words):
    msg = str(error).lower()

    for word in words:
        if word.lower() not in msg:
            return False

    return True
