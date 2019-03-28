class Vector :
    def __init__(self,d) :
        if isinstance(d,int):
            self.coords = [0]*d
        else:
            self.coords = d

    def __add__(self, other):
        answer = Vector(len(self.coords))
        for i in range(len(self.coords)):
            answer.coords[i] = (self.coords[i] + other.coords[i])
        return answer

    def __sub__(self,other):
        answer = Vector(len(self.coords))
        for i in range(len(self.coords)):
            answer.coords[i] = (self.coords[i] - other.coords[i])
        return answer

    def __str__(self):
        return "<" + ",".join(str(x) for x in self.coords) + ">"

    def __repr__(self):
        return str(self)

    def __neg__(self):
        answer = Vector(len(self.coords))
        for i in range(len(self.coords)):
            num = self.coords[i]
            if num > 0:
                answer.coords[i] = -num
            elif num < 0:
                answer.coords[i] = abs(num)
        return answer

    def __mul__(self,other):
        if isinstance(other,int):
            answer = Vector(len(self.coords))
            for i in range(len(self.coords)):
                answer.coords[i] = self.coords[i] * other
        else:
            answer = 0
            for i in range(len(self.coords)):
                answer += self.coords[i] * other.coords[i]
        return answer

    def __rmul__(self,other):
        if isinstance(other,int):
            answer = Vector(len(self.coords))
            for i in range(len(self.coords)):
                answer.coords[i] = self.coords[i] * other
        else:
            answer = 0
            for i in range(len(self.coords)):
                answer += self.coords[i] * other.coords[i]
        return answer

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __eq__(self,other):
        return self.coords == other.coords

    def __ne__(self,other):
        return not (self == other)

    def __len__(self):
        return len(self.coords)
