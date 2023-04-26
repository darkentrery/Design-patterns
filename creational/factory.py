from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return f"ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return f"ConcreteProduct2"


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Result {product.operation()}"
        return result


class ConcreteCreator1(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    print(f"{creator.some_operation()}")


if __name__ == "__main__":
    client_code(ConcreteCreator1())
    client_code(ConcreteCreator2())
