class Superclass
  def method(self):
    pass

class Subclass(Superclass):
  def method(self):
    print('subClass1에서 method()를 오버라이딩gka')

class SubClass2 (SuperClass) :
  pass
sub1 = subClass1()
sub2 = subClass2()

sub1.method()
sub2.method()

def mrthod(self):
  raise NotImplementedError()

