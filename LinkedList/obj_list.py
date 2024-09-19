class ObjList:
    def __init__(self, data) -> None:
        self.__data = data
        self.__next: ObjList = None
        self.__prev: ObjList = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data
