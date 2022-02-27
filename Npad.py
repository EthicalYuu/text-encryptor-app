class Npad:
    def create_write_notepad(self, file_name, content):
        f = open(str(file_name) + '.txt', "w+")
        f.write(content)
        f.close

