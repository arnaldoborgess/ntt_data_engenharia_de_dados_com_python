class ContaBancaria:
    LIMITE_SAQUES = 3

    def __init__(self, saldo=0, limite=500):
        self.saldo = saldo
        self.limite = limite
        self.extrato = []
        self.numero_saques = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return "Depósito realizado com sucesso!"
        return "Operação falhou! O valor informado é inválido."

    def sacar(self, valor):
        if valor > self.saldo:
            return "Operação falhou! Você não tem saldo suficiente."
        elif valor > self.limite:
            return "Operação falhou! O valor do saque excede o limite."
        elif self.numero_saques >= ContaBancaria.LIMITE_SAQUES:
            return "Operação falhou! Número máximo de saques excedido."
        elif valor > 0:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            return "Saque realizado com sucesso!"
        return "Operação falhou! O valor informado é inválido."

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("\n".join(self.extrato))
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

class Menu:
    def __init__(self):
        self.conta = ContaBancaria()

    def exibir_menu(self):
        menu = """
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [q] Sair

        => """
        while True:
            opcao = input(menu).lower()
            if opcao == "d":
                try:
                    valor = float(input("Informe o valor do depósito: "))
                    print(self.conta.depositar(valor))
                except ValueError:
                    print("Operação falhou! O valor informado é inválido.")
            elif opcao == "s":
                try:
                    valor = float(input("Informe o valor do saque: "))
                    print(self.conta.sacar(valor))
                except ValueError:
                    print("Operação falhou! O valor informado é inválido.")
            elif opcao == "e":
                self.conta.exibir_extrato()
            elif opcao == "q":
                break
            else:
                print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    Menu().exibir_menu()