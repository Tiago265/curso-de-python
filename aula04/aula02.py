# 10/05/2025

class contaBancaria:
    def __init__(self,titular , numero_conta):
        self.titular = titular
        self._numero_conta = numero_conta # Atributo protegito: Uso indicado dentro da classe e Sub-classes
        self.__saldo = 0 # Atributo privado: Modificação restrita dentro da classe
    
    def depositar(self,valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} efetuado com sucesso.")
        else:
            print("Insira um valor positivo para depósito.")

    def sacar(self,valor):
        if valor > 0 and self.__saldo >= valor:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")