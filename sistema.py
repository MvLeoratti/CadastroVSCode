#1- Pessoa Fisica
#2- Pessoa Juridica
#3 - Sair

#1- Pessoa Fisica / 2 Pessoa Juridica/ 3 - Sair
#1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Sair
#1 - Cadastrar Pessoa Juridica / 2- Listar Pessoa Juridica / 3- Sair

from datetime import date, datetime
from Pessoa import ENDERECO, PessoaFisica


def main():

    lista_pf = []
    while True:
        opcao = int(input("Escolha uma Opcao: 1 - Pessoa Fisica - 2 - Pessoa Juridica - 0 Sair: "))
        #Opcao -1 - Cadastrar Pessoa
        if opcao ==1:
            while True:
                opcao_PF = int(input("Escolha uma opcao: 1- Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3- voltar ao menu anterior: "))

                if opcao==1:
                    novaPF = PessoaFisica()
                    novo_end_PF = ENDERECO()

                    novaPF.nome = input("Digite o nome da Pessoa Fisica: ")
                    novaPF.cpf = input("Digite o CPF")
                    novaPF.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros): "))

                    data_nascimento = input("Digite a data de Nascimento (dd/mm/aaaa): ") #Solicita a data de Nascimento
                    novaPF.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today()- novaPF.dataNascimento).days #// 365

                    if idade>=18:
                        print("A Pessoa tem mais de 18 anos!")
                    else:
                        print("A Pessoa tem menos de 18 anos. Retornando ao menu anteriror!")
                        continue # Retorna ao inicio do loop
                    novo_end_PF.logradouro = input("Digite o Logradouro: ")
                    novo_end_PF.numero = input("Digite um Numero: ")
                    end_comercial = input("Este endereco e comercial: S/N: ") # Solicitar se o endereco e comercial ou Nao
                    novo_end_PF.endereco_comercial = end_comercial.strip().upper() == 'S'
                    novaPF.endereco = novo_end_PF

                    lista_pf.append(novaPF)

                    print("Cadastro realizado com Sucesso!!")
                elif opcao==2:
                    #Listar Pessoa Fisica
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome} ")
                            print(f"CPF: {cada_pf.cpf}")
                            print(f"Data Nascimento:  {cada_pf.dataNascimento.strftime('%d/%m/%Y')}")
                            print(f"Imposto a Pagar: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para Sair: ")
                            input()
                    else: 
                        print("Lista Vazia")
                elif opcao ==0:
                    print("Voltamos ao menu anterior! ")
                else:
                    print("Opcao Invalida, por favor digite uma das opcoes indicadas! ")
                   
                
        elif opcao==2:
            print("Funcionalidade para essa pessoa juridica Nao  foram Implementadas! ")
            pass
        elif opcao ==0:
            print("Obrigado por utilizar o nosso sistema! Valeu! ")
            break
        else:
            print("Opcao invlaida! ")

if __name__== "__main__":
    main() #Chama a funcao principal
                    
                
