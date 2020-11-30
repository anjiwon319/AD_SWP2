import pickle

class MemoDB:
    def __init__(self, filename):
        try:
            fH = open(filename, 'rb')
        except FileNotFoundError as e:
            self.memodb = []
            return
        try:
            self.memodb = pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()

    def writeMemoDB(self):
        fH = open(self.filename, 'wb')
        pickle.dump(self.memodb, fH)
        fH.close()
