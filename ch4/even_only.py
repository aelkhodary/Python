class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError('Only Integers can be add')
        if integer % 2 :
            raise ValueError('Only even number can be add')
        super().append(integer)



if __name__ == '__main__':
    e = EvenOnly()
    #e.append('a string')
    e.append(3)