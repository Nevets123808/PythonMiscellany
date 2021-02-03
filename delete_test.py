class thing:
    def __init__(self):
            pass

    def delete(self):
        self = None
        return self

me = thing()
print(type(me))
me.delete()
print(me)
