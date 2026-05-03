# Q4 — Access Private Variable (Error Fix)
# ✅ Using getter (best)
class Test:
    def __init__(self):
        self.__x = 10

    def get_x(self):
        return self.__x

t = Test()
print(t.get_x())

#or other way
# ⚠️ Using name mangling
print(t._Test__x)

