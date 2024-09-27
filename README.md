# Desafio 1

# Explicação do Código

## Classe `ContaBancaria`

### Atributos de Classe

- `LIMITE_SAQUES`: Limite de saques permitidos por dia (3).

### Método Construtor

- `__init__(self, saldo=0, limite=500)`: Inicializa uma conta bancária com saldo inicial e limite de saque. Também inicializa o extrato e o número de saques.

### Métodos

- `depositar(self, valor)`: Adiciona o valor ao saldo se for positivo e registra no extrato.
- `sacar(self, valor)`: Realiza um saque se o valor for válido, não exceder o saldo, o limite de saque e o número máximo de saques.
- `exibir_extrato(self)`: Exibe o extrato das transações e o saldo atual.

## Classe `Menu`

### Método Construtor

- `__init__(self)`: Inicializa uma conta bancária.

### Método

- `exibir_menu(self)`: Exibe um menu para o usuário realizar operações de depósito, saque, exibir extrato ou sair.

### Estrutura do Menu

- `[d] Depositar`: Solicita o valor do depósito e realiza a operação.
- `[s] Sacar`: Solicita o valor do saque e realiza a operação.
- `[e] Extrato`: Exibe o extrato da conta.
- `[q] Sair`: Encerra o programa.

### Execução

- O programa inicia a exibição do menu se executado diretamente.

### Observações

Uso de lista para extrato: Em vez de concatenar strings, usei uma lista para armazenar as transações, o que é mais eficiente.
Simplificação das condições de saque para melhorar a legibilidade.
Uso de join para exibir o extrato: Isso torna a exibição das transações mais limpa.
