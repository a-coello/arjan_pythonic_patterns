from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def primitive1(self) -> None:
        pass

    @abstractmethod
    def primitive2(self) -> None:
        pass

    @abstractmethod
    def primitive3(self) -> None:
        pass

    def template_method(self) -> None:
        self.primitive1()
        self.primitive2()
        self.primitive3()


class ConcreteClassA(AbstractClass):
    def primitive1(self) -> None:
        print("ConcreteClassA.primitive1")

    def primitive2(self) -> None:
        print("ConcreteClassA.primitive2")

    def primitive3(self) -> None:
        print("ConcreteClassA.primitive3")


class ConcreteClassB(AbstractClass):
    def primitive1(self) -> None:
        print("ConcreteClassB.primitive1")

    def primitive2(self) -> None:
        print("ConcreteClassB.primitive2")

    def primitive3(self) -> None:
        print("ConcreteClassB.primitive3")


def main():
    template = ConcreteClassA()
    template.template_method()


if __name__ == "__main__":
    main()
