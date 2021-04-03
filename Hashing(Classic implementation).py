class hashtable:
    def __init__(self):
        self.size = 11
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def hashval(self,key,size):
        return key%size

    def nexthash(self,oldhash,size):
        return (oldhash+1) % size

    def put(self,key,data):
        hval = self.hashval(key, len(self.slot))
        if self.slot[hval] == None:
            self.slot[hval] = key
            self.data[hval] = data
        else:
            if self.slot[hval] == key:
                self.data[hval] = data
            else:
                nexthval = self.nexthash(hval,len(self.slot))
                while self.slot[nexthval] != None and self.slot[nexthval] != key:
                    nexthval = self.nexthash(nexthval,len(self.slot))
                if self.slot[nexthval] == None:
                    self.slot[nexthval] = key
                    self.data[nexthval] = data
                else:
                    self.data[nexthval] = data

    def get(self,key):
        start = self.hashval(key,len(self.slot))
        data = None
        found = False
        stop = False
        tmp = start
        while self.slot[tmp] != None and not found and not stop:
            if self.slot[tmp] == key:
                found = True
                data = self.data[tmp]
            else:
                tmp = self.nexthash(tmp,len(self.slot))
                if tmp == start:
                    stop = True
        return data
    def __getitem__(self, key):
        self.get(key)
    def __setitem__(self, key, data):
        self.put(key,data)
if __name__ == '__main__':
    H = hashtable()
    H[54]="books"
    H[54]="data"
    H[26]= "algorilhms"
    H[93]="madc"
    H[17]="casy"
    H[77]="CnrccrMOonk"
    H[31]="Jobs"
    H[44]="Hunting"
    H[55]= "King"
    H[20]="Lion"
    print(H.slot)
    print(H.data)
    print(H[54])
    print("OK")