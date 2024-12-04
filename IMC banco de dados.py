import sqlite3


def calcular_imc(peso, altura_cm):
    altura_m = altura_cm / 100
    return peso / (altura_m ** 2)


conn = sqlite3.connect('pacientes.db')
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS pacientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    altura_cm REAL NOT NULL,
    peso_kg REAL NOT NULL,
    imc REAL NOT NULL
)
''')


nome = input("Digite seu nome: ")
endereco = input("Digite seu endereço: ")
altura_cm = float(input("Digite sua altura em centímetros: "))
peso_kg = float(input("Digite seu peso em quilos: "))


imc = calcular_imc(peso_kg, altura_cm)
print(f"\n{nome}, seu IMC é: {imc:.2f}")


cursor.execute('''
INSERT INTO pacientes (nome, endereco, altura_cm, peso_kg, imc)
VALUES (?, ?, ?, ?, ?)
''', (nome, endereco, altura_cm, peso_kg, imc))


conn.commit()
conn.close()

print("Seus dados foram salvos no banco de dados com sucesso!")

