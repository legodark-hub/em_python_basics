from linked_list import LinkedList
from obj_list import ObjList


lst = LinkedList()

print(lst.get_data())

obj1 = ObjList("раз")
obj2 = ObjList("два")
obj3 = ObjList("три")

lst.add_obj(obj1)
lst.add_obj(obj2)
lst.add_obj(obj3)

print(lst.get_data())

lst.remove_obj()

print(lst.get_data())
