# add
# push
# pop
# peek
# isEmpty

class stack():
    __capacity = 1000
    __size = 0
    __list = [i for i in __capacity]

    def push(self,val) -> str:
        if self.__size != self.__capacity:
            self.__list[self.__size] = val
            self.__size += 1

    def pop(self):
        if self.__size != 0:
            self.__size -= 1
            return self.__list[self.__size]
    
    def peek(self) -> str:
        if self.__size != 0:
            return self.__list[self.__size]

    def isEmpty(self):
        if self.__size == 0:
            return True
        return False

