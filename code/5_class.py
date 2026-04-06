# 5.class.py

class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass #자식 클래스에서 구현
    
    def setName(self,name: str):
        """
        Set the Animal class's name
        Animal 클래스의 이름을 반환하는 함수
        :return: Animal의 이름
        """
        self.name = name
        
    def getName(self) -> str:
        """
        Return the Animal class's name
        Animal 클래스의 이름을 반환하는 함수
        :return: Animal의 이름
        """
        return self.name
    
class dog(Animal): #  is-a 관계 (자식)
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        
    def speak(self):
        print(f"{self.name} say woof!")
        
class Cat(Animal):
    def speak(self):
        print(f"{self.name} say meaw!"})
        
        