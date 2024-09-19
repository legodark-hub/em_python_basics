from obj_list import ObjList


class LinkedList:
    def __init__(self) -> None:
        self.head: ObjList = None
        self.tail: ObjList = None

    def add_obj(self, obj: ObjList):
        """Добавление нового объекта ObjList в конец связанного списка

        Args:
            obj (ObjList): объект класса ObjList
        """
        if self.head == None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove_obj(self):
        """Удаление последнего объекта из связного списка"""
        prev_obj = self.tail.get_prev()
        self.tail.set_prev(None)
        self.tail = prev_obj
        self.tail.set_next(None)
        
    def __iter__(self):
        current_obj = self.head
        while current_obj:
            yield current_obj.get_data()
            current_obj = current_obj.get_next()

    def get_data(self):
        return list(self)
