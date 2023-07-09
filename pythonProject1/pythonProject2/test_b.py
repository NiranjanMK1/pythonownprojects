import pytest

class Test:
   @pytest.fixture()
   def myfixture(self):
      print("my fixture is called")
      yield
      print("This is once after every mehtod")

   def test_method1(self,myfixture):
      print("method1 is called")

   def test_method2(self, myfixture):
      print("method2 is called")