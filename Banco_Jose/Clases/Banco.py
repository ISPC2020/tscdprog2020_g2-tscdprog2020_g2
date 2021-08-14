# librerias
from Clases.Cliente import Cliente
from Clases.Empleado_dao import EmpleadoDAO


class Banco:
    _opcion = None
    _clientes = None

    @classmethod
    def menu_principal(cls, opcion=_opcion, clientes=_clientes):
        opcion = opcion
        clientes = clientes

        while opcion != 5:
            print("""
            1. Clientes
            2. Cuentas
            3. Empleandos
            4. Salir
            """)
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                clientes = Cliente.menu_cliente(clientes)
            elif opcion == 2:
                cliente_busqueda = int(input("Ingrese el DNI del Cliente a Buscar: "))
                for cliente in clientes:
                    if cliente.id == cliente_busqueda:
                        print(cliente.__str__())
                        cliente.operaciones()
            elif opcion == 3:
                EmpleadoDAO.menu_empleadoDAO()
            elif opcion == 4:
                break


if __name__ == '__main__':
    Banco.menu_principal()
