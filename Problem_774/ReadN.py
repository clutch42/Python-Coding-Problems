from Read7 import Read7


def read_n(n):
    read_file = Read7("data.txt")
    seven_chars = read_file.read7()
    char = ""
    while seven_chars != "" and read_file.position < n:
        char += seven_chars
        seven_chars = read_file.read7()
    return char[:n]
    read_file.close()