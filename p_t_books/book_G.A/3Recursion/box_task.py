'''#00
def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while pile is not empty:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key")





#01
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            print("found the key")'''
#мой код.
class Box:
    def __init__(self, items):
        self.items = items

    def grab_a_box(self):
        return next((item for item in self.items if isinstance(item, Box)), None)

    def is_a_key(self):
        return "key" in self.items

def look_for_key(box):
    for item in box.items:
        if isinstance(item, Box):
            look_for_key(item)
        elif item == "key":
            print("Found the key!")
            return

box1 = Box(["book", "pen", "box"])
box2 = Box(["notebook", "box"])
box3 = Box(["pencil", "ruler", "key"])

box1.items.append(box2)
box1.items.append(box3)
look_for_key(box1)