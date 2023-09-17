from abc import ABC, abstractmethod


class Implementation(ABC):
    @abstractmethod
    def implementation(self) -> None:
        pass


class ConcreteImplementation1(Implementation):
    def implementation(self) -> None:
        print("ConcreteImplementation1.implementation")


class ConcreteImplementation2(Implementation):
    def implementation(self) -> None:
        print("ConcreteImplementation2.implementation")


class Abstraction(ABC):
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation


class RefinedAbstraction1(Abstraction):
    def do_something(self) -> None:
        self.implementation.implementation()


class RefinedAbstraction2(Abstraction):
    def do_something_else(self) -> None:
        self.implementation.implementation()


def main() -> None:
    impl = ConcreteImplementation1()
    abstraction = RefinedAbstraction1(impl)
    abstraction.do_something()


if __name__ == "__main__":
    main()
