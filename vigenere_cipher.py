class Vigenere:
    dic = ''
    key = ''
    pas = ''
    pls = ''

    def _pindex(self, l, i):
        return self.dic.find(l[i % len(l)])

    def set_dic(self, dic):
        self.dic = dic

    def set_key(self, key):
        self.key = key

    def set_pas(self, pas):
        self.pas = pas        
    
    def get_dic(self):
        return self.dic

    def get_key(self):
        return self.key

    def get_pas(self):
        return self.pas

    def tst_dic(self, s):
        err = 0
        self.pls = ''
        for i in s:
            if self.dic.find(i) == -1:
                err += 1
                self.pls += i
        return err

    def get_pls(self):
        return self.pls

    def get_crypt(self):
        res = ''
        for i in range(len(self.pas)):
            res +=  self.dic[(self._pindex(self.pas, i) + self._pindex(self.key, i)) % len(self.dic)]
        return res

    def get_encrp(self):
        res = ''
        for i in range(len(self.pas)):
            res +=  self.dic[(self._pindex(self.pas, i) - self._pindex(self.key, i)) % len(self.dic)]
        return res




if __name__ == "__main__":
    A = Vigenere()

    A.set_dic(str(input("Enter dic: ")))

    while True:
        A.set_key(str(input("Enter key: ")))
        if(A.tst_dic(A.get_key())):
            print(A.get_pls(), "- does not belong to the dictionary")
        else:
            break
    
    while True:
        A.set_pas(str(input("Enter pas: ")))
        if(A.tst_dic(A.get_pas())):
            print(A.get_pls(), "- does not belong to the dictionary")
        else:
            break
        
    print("Crypt pas:", A.get_crypt())
    print("Encrp pas:", A.get_encrp())