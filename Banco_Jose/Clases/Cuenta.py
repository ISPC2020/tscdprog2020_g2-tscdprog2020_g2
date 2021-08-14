class Cuenta:

    @staticmethod
    def menu_cuenta(cuenta):
        opcion = None

        while opcion != 5:
            print("""
               Opciones:
               1. Depositar
               2. Extraer
               3. Consultar saldo
               4. Constitucion de plazo fijo
               5. Salir
               """)
            opcion = int(input("Ingrese una opcion: "))

            if opcion == 1:
                cuenta.deposito(float(input("Ingrese el monto a depositar: $")))

            elif opcion == 2:
                cuenta.extraccion(float(input("Ingrese el monto a depositar: $")))

            elif opcion == 3:
                print(cuenta.saldo())

            elif opcion == 4:
                cuenta.plazo_fijo(
                    float(input("Ingrese el monto del capital a invertir: $")),
                    int(input("Ingrese la cantidad de dias: ")),
                    float(input("Ingrese la tasa de interes: "))
                )
            elif opcion == 5:
                break

    def __init__(self):
        self._saldo = 0

    def deposito(self, monto):
        self._saldo += monto

    def extraccion(self, monto):
        self._saldo -= monto

    def saldo(self):
        return self._saldo

    def plazo_fijo(self, capital, tiempo, tasa_interes):
        interes = (capital * tasa_interes) / 100
        print(f'Plazo fijo'.center(25, '-'))
        print(f'Capital invertido ${capital}')
        print(f'Disponible en: {tiempo} dias')
        print(f'Ganancia de ${interes}')


# test
if __name__ == '__main__':
    cuenta = Cuenta()
    cuenta.menu_cuenta(cuenta)
