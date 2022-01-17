teste = list()
teste.append('Gustavo')
teste.append('22')
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 33
galera.append(teste)
print(galera)
# OUTPUT: [['Maria', 33], ['Maria', 33]]
# Estão referenciando ainda para o mesmo espaço na memória

# Jeito CORRETO
teste = list()
teste.append('Gustavo')
teste.append('22')
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 33
galera.append(teste[:])
print(galera)
# OUTPUT: [['Gustavo', '22'], ['Maria', 33]]
# Cria uma cópia, cortando a referência para o objeto antigo
