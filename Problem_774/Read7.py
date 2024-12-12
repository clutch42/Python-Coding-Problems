class Read7:
    def __init__(self, filename):
        self.file = open(filename, 'r')  # Open the file for reading
        self.position = 0  # Pointer to track the current position in the file

    def read7(self):
        # Read up to 7 characters from the current position
        chunk = self.file.read(7)  # Read the next 7 characters
        if not chunk:
            return ""  # No more characters to read

        return chunk

    def close(self):
        # Always remember to close the file after you're done
        self.file.close()
