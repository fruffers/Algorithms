
class queue():
    __capacity = 1000
    __size = 0
    __front = 0
    __back = 0
    __list = [i for i in __capacity]

    def add(self,val):
        if self.__back != self.__capacity:
            self.__list[self.__back] = val
            self.__back += 1
            self.__size += 1

    def remove(self):
        if self.__size != 0:
            res = self.__list[self.__front]
            self.__size -= 1
            self.__front += 1
            return res
    
    def peek(self):
        if self.__size != 0:
            return self.__list[self.__front]

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False
