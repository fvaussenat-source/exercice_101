import os
class Path(str):

    def __init__(self, folder_file):
        self.folder_file = folder_file

    def dirname(self):
        return Path(os.path.dirname(self))

    @property
    def ext(self):
        filename = os.path.splitext(self)
        return filename[-1]

    @property
    def name(self):
        name = os.path.basename(self)
        filename= os.path.splitext(name)
        return filename[0]



s = Path("/Users/thibh/Documents/test.txt")
print(s.dirname().dirname())
print(s.name)
print(s.ext)
