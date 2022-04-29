#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------

class Target:
    """
    El objetivo define la interfaz específica del dominio utilizada por el código del cliente.
    """

    def request(self) -> str:
        return "Objetivo: el comportamiento del objetivo predeterminado."


class Adaptee:
    """
    The Adaptee contains some useful behavior, but its interface is incompatible
    with the existing client code. The Adaptee needs some adaptation before the
    client code can use it.
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the Adaptee's interface compatible with the Target's
    interface via multiple inheritance.
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    The client code supports all classes that follow the Target interface.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Cliente: Puedo trabajar bien con los objetos de Target:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: La clase Adaptee tiene una interfaz rara. "
          "mira, no lo entiendo:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Cliente: Pero puedo trabajar con él a través del Adaptador:")
    adapter = Adapter()
    client_code(adapter)
