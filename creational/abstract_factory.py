from abc import ABC, abstractmethod


class AbsctractProductA(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class ConcreteProductA1(AbsctractProductA):
    def get_name(self) -> str:
        return f"ProductA1"


class ConcreteProductA2(AbsctractProductA):
    def get_name(self) -> str:
        return f"ProductA2"


class AbsctractProductB(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


class ConcreteProductB1(AbsctractProductB):
    def get_name(self) -> str:
        return f"ProductB1"


class ConcreteProductB2(AbsctractProductB):
    def get_name(self) -> str:
        return f"ProductB2"


class AbsctractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbsctractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbsctractProductB:
        pass


class ConcreteFactory1(AbsctractFactory):
    def create_product_a(self) -> AbsctractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbsctractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbsctractFactory):
    def create_product_a(self) -> AbsctractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbsctractProductB:
        return ConcreteProductB2()


def client_code(factory: AbsctractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_a.get_name()}")
    print(f"{product_b.get_name()}")


if __name__ == "__main__":
    client_code(ConcreteFactory1())
    client_code(ConcreteFactory2())
