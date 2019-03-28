class Poly:
    def __init__(self, list=None):
        if list==None:
            self.list=[]
        else:
            self.list=list

    def __repr__(self):
        result=''
        constant=len(self.list)
        for i in range(len(self.list)):
            if self.list[i]!=0:
                if i==0:
                    result=result+str(self.list[i])
                else:
                    result= result+str(self.list[i])+"*x^"+str(i)
            if i!=constant-1:
                result = result+"+"
        return result

    def eval(self,val):
        return self.list[val+1]

    def __add__(self, other):
        new=Poly()
        for i in range(len(self.list)):
            try:
                new.list.append(self.list[i] + other.list[i])
            except IndexError:
                try:
                    new.list.append(self.list[i])
                except IndexError:
                    try:
                        new.list.append(other.list[i])
                    except IndexError:
                        break
        return new

    def __mul__(self, other):
        new=Poly()
        for i in range(len(self.list)+len(other.list)-1):
            new.list.append(0)
        for i in range(len(self.list)):
            for j in range(len(other.list)):
                new.list[i+j]+=self.list[i]*other.list[j]
        return new

    def derivative(self):
        new=Poly()
        for i in range(len(self.list)-1):
            new.list.append(0)
        for i in range(len(self.list)):
            if i!=0:
                new.list[i-1]=self.list[i]*i
        return new


lst1=Poly([1,3,1])
lst2=Poly([1,1])
print(lst1 + lst2)
print(lst1*lst2)
print(lst1.derivative())