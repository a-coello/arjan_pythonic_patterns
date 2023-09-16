from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class ConcreteStrategy1(Strategy):
    def execute(self) -> None:
        print("ConcreteStrategy1.execute")


class ConcreteStrategy2(Strategy):
    def execute(self) -> None:
        print("ConcreteStrategy2.execute")


class Context:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy

    def do_something(self) -> None:
        self.strategy.execute()


def main() -> None:
    context = Context(strategy=ConcreteStrategy1())
    context.do_something()


if __name__ == "__main__":
    main()
