# ====================================================================
# TÓPICO 01 - Variáveis, tipos de dados e entrada/saída
# ====================================================================

print("QUESTÃO 01 - TÓPICO 01")
minha_idade = 18
altura = 7.5
linguagem = "Python"
ativo = True
print(minha_idade, type(minha_idade))
print(altura, type(altura))
print(linguagem, type(linguagem))
print(ativo, type(ativo))

print("QUESTÃO 09 - TÓPICO 01")
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")
area = input("Área de interesse:")
proxima_idade = idade + 1
print("Nome:", nome)
print("Idade atual:", idade)
print("Idade no próximo ano:", proxima_idade)
print("Cidade:", cidade)
print("Área de interesse:", area)


# ====================================================================
# TÓPICO 02 - Operadores e expressões
# ====================================================================

print("QUESTÃO 10 - TÓPICO 02")
print("17 / 5 =", 17 / 5)
print("17 // 5 =", 17 // 5)
print("17 % 5 =", 17 % 5)
print("2 ** 4 =", 2 ** 4)
print("O resto 17 % 5 = 2 informa quantos itens sobram ao dividir 17 em grupos de 5.")

print("QUESTÃO 18 - TÓPICO 02")
import math
comprimento = float(input("Comprimento da sala (m): "))
largura = float(input("Largura da sala (m): "))
lado_placa = float(input("Lado de uma placa (m): "))
area_sala = comprimento * largura
area_placa = lado_placa * lado_placa
quantidade_minima = math.ceil(area_sala / area_placa)
quantidade_com_reserva = math.ceil(quantidade_minima * 1.1)
print("Área da sala:", area_sala)
print("Quantidade mínima:", quantidade_minima)
print("Quantidade com reserva:", quantidade_com_reserva)


# ====================================================================
# TÓPICO 03 - Estruturas condicionais
# ====================================================================

print("QUESTÃO 19 - TÓPICO 03")
n = int(input("Digite um inteiro: "))
if n > 0:
    print("positivo")
elif n < 0:
    print("negativo")
else:
    print("zero")

print("QUESTÃO 27 - TÓPICO 03")
consumo = int(input("Consumo em m3: "))
if consumo < 0:
    print("Consumo inválido")
else:
    if consumo <= 10:
        valor1 = consumo * 2
        valor2 = 0
        valor3 = 0
    elif consumo <= 20:
        valor1 = 10 * 2
        valor2 = (consumo - 10) * 3
        valor3 = 0
    else:
        valor1 = 10 * 2
        valor2 = 10 * 3
        valor3 = (consumo - 20) * 5
    total = valor1 + valor2 + valor3
    print(f"Faixa 1: R$ {valor1:.2f}")
    print(f"Faixa 2: R$ {valor2:.2f}")
    print(f"Faixa 3: R$ {valor3:.2f}")
    print(f"Total: R$ {total:.2f}")

# ====================================================================
# TÓPICO 04 - Repetição com while e validação
# ====================================================================

print("QUESTÃO 28 - TÓPICO 04")
i = 1
while i <= 10:
    print(i)
    i = i + 1

print("QUESTÃO 36 - TÓPICO 04")
saldo = 0
while True:
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("0 - Sair")
    opcao = int(input("Opção: "))
    if opcao == 0:
        break
    elif opcao == 1:
        valor = float(input("Valor do depósito: "))
        if valor > 0:
            saldo = saldo + valor
            print("Depósito realizado")
        else:
            print("Depósito recusado")
    elif opcao == 2:
        valor = float(input("Valor do saque: "))
        if valor > 0 and valor <= saldo:
            saldo = saldo - valor
            print("Saque realizado")
        else:
            print("Saque recusado")
    elif opcao == 3:
        print("Saldo:", saldo)
    else:
        print("Opção inválida")
# ====================================================================
# TÓPICO 05 - Repetição com for e laços aninhados
# ====================================================================

print("QUESTÃO 37 - TÓPICO 05")
print("range(5):")
for i in range(5):
    print(i, end=" ")
print("\nrange(2, 8):")
for i in range(2, 8):
    print(i, end=" ")
print("\nrange(10, 0, -2):")
for i in range(10, 0, -2):
    print(i, end=" ")
print()

print("QUESTÃO 45 - TÓPICO 05")
altura = int(input("Digite a altura (1-20): "))
if 1 <= altura <= 20:
    ultima_linha = ""
    for i in range(1, altura + 1):
        ultima_linha += str(i) + " "
    largura = len(ultima_linha.strip())

    for i in range(1, altura + 1):
        linha = ""
        for j in range(1, i + 1):
            linha += str(j) + " "
        print(linha.strip().rjust(largura))
else:
    print("Altura inválida")

# ====================================================================
# TÓPICO 06 - Strings e processamento de texto
# ====================================================================

print("QUESTÃO 46 - TÓPICO 06")
texto = "Programar"
print("Primeiro caractere:", texto[0])
print("Último caractere:", texto[-1])
print("Quatro primeiros:", texto[:4])
print("Tamanho:", len(texto))

print("QUESTÃO 54 - TÓPICO 06")
texto = input("Digite uma mensagem: ")
print("Caracteres:", len(texto))
limpo = texto.replace(".", " ").replace(",", " ").replace("!", " ").replace("?", " ").replace(":", " ").replace(";", " ")
palavras = limpo.split()
if not palavras:
    print("Quantidade de palavras: 0")
    print("Média e palavra mais longa não disponíveis")
else:
    print("Quantidade de palavras:", len(palavras))
    soma_tamanhos = sum(len(p) for p in palavras)
    print(f"Tamanho médio: {soma_tamanhos / len(palavras):.2f}")
    maior = palavras[0]
    for p in palavras:
        if len(p) > len(maior):
            maior = p
    print("Palavra mais longa:", maior)

# ====================================================================
# TÓPICO 07 - Listas e matrizes
# ====================================================================

print("QUESTÃO 55 - TÓPICO 07")
lista = [10, 20, 30, 40, 50]
print("Lista inicial:", lista)
lista.append(60)
print("Após append(60):", lista)
lista.insert(0, 5)
print("Após insert(0, 5):", lista)
retirado = lista.pop()
print("Valor retirado:", retirado)
print("Lista final:", lista)
print("Tamanho final:", len(lista))

print("QUESTÃO 63 - TÓPICO 07")
sala = [["Livre" for _ in range(6)] for _ in range(5)]
while True:
    print("1 - Mostrar sala")
    print("2 - Reservar")
    print("3 - Cancelar reserva")
    print("0 - Sair")
    op = int(input("Opção: "))
    if op == 0:
        break
    elif op == 1:
        ocupados = 0
        for i in range(5):
            for j in range(6):
                print(f"[{sala[i][j][0]}]", end=" ")
                if sala[i][j] == "Ocupado":
                    ocupados += 1
            print()
        print("Total de lugares ocupados:", ocupados)
    elif op == 2:
        l = int(input("Linha (1-5): ")) - 1
        c = int(input("Coluna (1-6): ")) - 1
        if 0 <= l < 5 and 0 <= c < 6:
            if sala[l][c] == "Livre":
                sala[l][c] = "Ocupado"
                print("Reserva realizada")
            else:
                print("Lugar já ocupado")
        else:
            print("Coordenadas inválidas")
    elif op == 3:
        l = int(input("Linha (1-5): ")) - 1
        c = int(input("Coluna (1-6): ")) - 1
        if 0 <= l < 5 and 0 <= c < 6:
            if sala[l][c] == "Ocupado":
                sala[l][c] = "Livre"
                print("Reserva cancelada")
            else:
                print("Lugar já está livre")
        else:
            print("Coordenadas inválidas")
# ====================================================================
# TÓPICO 08 - Tuplas, dicionários e conjuntos
# ====================================================================

print("QUESTÃO 64 - TÓPICO 08")
produto = ("Caderno", 15.50, 3)
nome, preco, qtd = produto
total = preco * qtd
print("Produto:", nome)
print("Preço:", preco)
print("Quantidade:", qtd)
print("Total:", total)
print("Tuplas são imutáveis, logo tentar produto[1] = 20 geraria TypeError.")

print("QUESTÃO 72 - TÓPICO 08")
qtd_part = int(input("Quantidade de participantes: "))
participantes = []
for i in range(qtd_part):
    while True:
        ident = input(f"Identificador do participante {i+1}: ")
        if not ident or any(p["ident"] == ident for p in participantes):
            print("Identificador vazio ou já existente. Tente novamente.")
        else:
            break
    nome = input("Nome: ")
    pontos = int(input("Pontuação: "))
    participantes.append({"ident": ident, "nome": nome, "pontos": pontos})


participantes.sort(key=lambda x: (-x["pontos"], x["nome"], x["ident"]))

print("Top 3 Participantes:")
for idx, p in enumerate(participantes[:3], 1):
    print(f"{idx}º - ID: {p['ident']}, Nome: {p['nome']}, Pontos: {p['pontos']}")
if not participantes:
    print("Nenhum participante cadastrado")

# ====================================================================
# TÓPICO 09 - Funções, decomposição e recursão
# ====================================================================

print("QUESTÃO 73 - TÓPICO 09")
def dobro(numero):
    return numero * 2

print("Dobro de 5:", dobro(5))
print("Dobro de 10:", dobro(10))
print("Dobro de -3:", dobro(-3))

print("QUESTÃO 81 - TÓPICO 09")
def validar_nota(nota):
    return 0 <= nota <= 10

def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar_media(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

def avaliar_registros(registros):
    resultados = []
    for reg in registros:
        nome = reg["nome"]
        notas = reg["notas"]
        if not notas:
            resultados.append({"nome": nome, "status": "Rejeitado: sem notas"})
            continue
        validas = []
        invalida = False
        for n in notas:
            if validar_nota(n):
                validas.append(n)
            else:
                invalida = True
                break
        if invarida or len(validas) != len(notas):
            # nota inválida encontrada
            pass
        # Simplificação rigorosa para cumprir o enunciado
        invalido_encontrado = any(not validar_nota(n) for n in notas)
        if invalido_encontrado:
            resultados.append({"nome": nome, "status": "Rejeitado: nota inválida"})
        else:
            med = calcular_media(notas)
            sit = classificar_media(med)
            resultados.append({"nome": nome, "media": med, "status": sit})
    return resultados

regs_exemplo = [
    {"nome": "Ana", "notas": [8.0, 9.0, 7.5]},
    {"nome": "Bruno", "notas": [3.0, 4.0]},
    {"nome": "Carlos", "notas": [11.0, 5.0]}
]
print("Avaliação de registros:", avaliar_registros(regs_exemplo))

# ====================================================================
# TÓPICO 10 - Arquivos, exceções e algoritmos
# ====================================================================

print("QUESTÃO 82 - TÓPICO 10")

with open("_etapas/nomes_teste.txt", "w", encoding="utf-8") as f:
    f.write("Ana\nBruno\nCarlos\n")
print("Arquivo gravado com sucesso.")

print("QUESTÃO 90 - TÓPICO 10")

vendas_linhas = [
    "Caderno;5;15.00",
    "Caneta;10;2.50",
    "Caderno;2;16.00",
    "Invalido;-1;10"
]
relatorio = {}
for linha in vendas_linhas:
    partes = linha.split(";")
    if len(partes) != 3:
        continue
    prod, q_str, p_str = partes
    try:
        q = int(q_str)
        p = float(p_str)
        if q <= 0 or p < 0:
            continue
        if prod not in relatorio:
            relatorio[prod] = {"qtd": 0, "receita": 0.0}
        relatorio[prod]["qtd"] += q
        relatorio[prod]["receita"] += q * p
    except ValueError:
        continue

ordenado = sorted(relatorio.items(), key=lambda x: (-x[1]["receita"], x[0]))
print("Relatório de vendas ordenado por receita:")
for p, dados in ordenado:
    print(f"Produto: {p}, Qtd: {dados['qtd']}, Receita: R$ {dados['receita']:.2f}")
# ====================================================================
# TÓPICO 11 - Desafios integradores
# ====================================================================

print("DESAFIO 91 • DIFICULDADE ALTA • BLOOM: CRIAR")
print("Escalonador de estudos (Backtracking)")

def resolver_escalonamento(capacidade, atividades):
   
    atividades_ord = sorted(atividades, key=lambda x: x["prazo"])
    agenda = {dia: [] for dia in range(1, 8)}
    carga = {dia: 0 for dia in range(1, 8)}

    def backtrack(index):
        if index == len(atividades_ord):
            return True
        atv = atividades_ord[index]
        for dia in range(1, atv["prazo"] + 1):
            if carga[dia] + atv["duracao"] <= capacidade:
                
                agenda[dia].append(atv)
                carga[dia] += atv["duracao"]
                if backtrack(index + 1):
                    return True
                
                agenda[dia].pop()
                carga[dia] -= atv["duracao"]
        return False

    if backtrack(0):
        return agenda
    return None

cap = 120 
atvs = [
    {"id": "A1", "nome": "Matemática", "duracao": 60, "prazo": 2},
    {"id": "A2", "nome": "Física", "duracao": 90, "prazo": 1},
    {"id": "A3", "nome": "História", "duracao": 45, "prazo": 3}
]
res_91 = resolver_escalonamento(cap, atvs)
if res_91:
    print("Agenda encontrada com sucesso:")
    for d, lista in res_91.items():
        if lista:
            print(f" Dia {d}:", [a["nome"] for a in lista])
else:
    print("Sem solução possível.")

print("\nDESAFIO 100 • DIFICULDADE ALTA • BLOOM: CRIAR")
print("Sistema integrado de biblioteca")

class Biblioteca:
    def __init__(self):
        self.livros = {}
        self.leitores = {}
        self.emprestimos = []

    def cadastrar_livro(self, codigo, titulo, qtd):
        self.livros[codigo] = {"titulo": titulo, "qtd_total": qtd, "disponiveis": qtd}

    def cadastrar_leitor(self, matricula, nome):
        self.leitores[matricula] = {"nome": nome}

    def emprestar(self, id_emp, livro_cod, leitor_mat, data):
        if livro_cod not in self.livros or leitor_mat not in self.leitores:
            return False, "Livro ou leitor inexistente"
        if self.livros[livro_cod]["disponiveis"] <= 0:
            return False, "Sem exemplares disponíveis"
        ativos = sum(1 for e in self.emprestimos if e["leitor"] == leitor_mat and "devolucao" not in e)
        if ativos >= 3:
            return False, "Leitor atingiu o limite de 3 empréstimos ativos"

        self.livros[livro_cod]["disponiveis"] -= 1
        self.emprestimos.append({"id": id_emp, "livro": livro_cod, "leitor": leitor_mat, "data": data})
        return True, "Empréstimo realizado com sucesso"

bib = Biblioteca()
bib.cadastrar_livro("L1", "Python para Iniciantes", 2)
bib.cadastrar_leitor("M1", "Alice")
print("Empréstimo 1:", bib.emprestar("E1", "L1", "M1", "2026-11-01"))
print("Empréstimo 2:", bib.emprestar("E2", "L1", "M1", "2026-11-01"))
print("Empréstimo 3 (deve falhar por limite de exemplares/exemplar esgotado):", bib.emprestar("E3", "L1", "M1", "2026-11-01"))
