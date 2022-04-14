class enc_pass:
    # we want to encrypt our data flow so that the firewall will not know our real data
    def __init__(self, enpass,depass):
        self.enpass = enpass.copy()
        self.depass = depass.copy()
        #print(self.enpass)
        #print(self.depass)

    # encrypt the normal data by map one byte to another in range 0 - 255
    def enc_data(self, bytearr):
        i=0
        while i < len(bytearr):
            bytearr[i] = self.enpass[bytearr[i]]
            i += 1

    # decrypt the encrypt data to original data
    def denc_data(self, bytearr):
        i=0
        while i < len(bytearr):
            bytearr[i] = self.depass[bytearr[i]]
            i += 1

    # create a simple codec
    @classmethod
    def codec(cls, enpass):
        depass = enpass.copy()
        i=0
        while i < len(enpass):
            v=enpass[i]
            depass[v] = i
            i += 1
        return cls(enpass, depass)

