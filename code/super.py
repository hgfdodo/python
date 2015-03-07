class Filter:
#    def init(self):
#    self.blocked=[]
    blocked=[]
    def init(self):pass
        

    def filte(self,sequence):
        return [x for x in sequence if x not in self.blocked]


class HGFFilter(Filter):
    blocked=['HGF']
    def init(self):pass

        
