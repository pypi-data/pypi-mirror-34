def suffix(s,suf="[+]"):
    "Suffix a string with another string and return the new value"

    return f"{suf} {s}"

def suffix_print(s,suf="[+]"):
    "Suffix and print a string"

    print(suffix(s,suf))

def clean_suffix_print(s,suf="[+]", end=""):
    """Suffix and print a string without the newline character. The ```end```
    argument is used to indicate the final character of each line, which is
    a newline character by default."""

    print(suffix(s,suf), end=end)

# shortcuts are short
sprint = suffix_print
csprint = clean_suffix_print
