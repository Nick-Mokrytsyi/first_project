
# class ClassName:
#     pass

# class ChildClassName(ClassName):
#     pass


class Point:
    x = 0

    def __add__(self, other):
        return self.x + other.x


pt = Point()    # __new__(), __init__()
# pt            # __call__()
# del pt          # __del__()

pt1 = Point()
pt1.x = 5
pt2 = Point()
pt2.x = 7

a = pt1 + pt2
print(a)