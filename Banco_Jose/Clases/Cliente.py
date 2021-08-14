# librerias
from Clases.Persona import Persona
from Clases.Cuenta import Cuenta


class Cliente(Persona, Cuenta):
    """Esta clase se encarga de crear un objeto del tipo cliente"""

    @staticmethod
    def menu_cliente(clientes):
        opcion = None

        if clientes is None:
            clientes = []

        while opcion != 5:
            print("""
            Opciones:
            1. Crear cliente
            2. Mostrar clientes
            3. Editar clientes
            4. Eliminar clientes
            5. Salir
            """)
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                clientes.append(Cliente(
                    int(input("Ingrese el numero de DNI: ")),
                    input("Ingrese el Nombre: "),
                    input("Ingrese el Apellido: "),
                    input("Ingrese el Sexo <M o F>: "),
                    input("Ingrese la fecha de nacimineto <año-mes-dia>: "),
                    input("Ingrese el Email: "),
                    input("Ingrese el numero de telefono: ")
                ))

            elif opcion == 2:
                if len(clientes) == 0:
                    print(f'Lista de clientes vacia')
                else:
                    for cliente in clientes:
                        print(cliente.__str__())

            elif opcion == 3:
                id_buscar = int(input("Ingrese el DNI del Cliente a Editar: "))

                for cliente in clientes:
                    if cliente.id == id_buscar:
                        cliente.id = int(input("Ingrese el numero de DNI: "))
                        cliente.nombre = input("Ingrese el Nombre: ")
                        cliente.apellido = input("Ingrese el Apellido: ")
                        cliente.sexo = input("Ingrese el Sexo <M o F>: ")
                        cliente.nacimiento = input("Ingrese la fecha de nacimineto <año-mes-dia>: ")
                        cliente.email = input("Ingrese el Email: ")
                        cliente.telefono = input("Ingrese el numero de telefono: ")

            elif opcion == 4:
                id_buscar = int(input("Ingrese el DNI del Cliente a Eliminar: "))

                for cliente in clientes:
                    if cliente.id == id_buscar:
                        clientes.remove(cliente)

            elif opcion == 5:
                return clientes

    def __init__(self, id, nombre, apellido, sexo, nacimineto, email, telefono):
        super().__init__(id, nombre, apellido, sexo, nacimineto)
        self._email = email
        self._telefono = telefono
        self._cuenta = Cuenta()

    def __str__(self):
        return f'''
            {super().__str__()},
            Email: {self._email},
            Telefono: {self._telefono}
        '''

    def operaciones(self):
        Cuenta.menu_cuenta(self._cuenta)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, telefono):
        self._telefono = telefono


# test
if __name__ == '__main__':
    pass