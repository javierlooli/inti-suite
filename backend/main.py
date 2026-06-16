import sqlite3
from pathlib import Path
from datetime import datetime

DB_DIR = Path("data")
DB_DIR.mkdir(exist_ok=True)

DB_PATH = DB_DIR / "inti_suite.db"


def conectar():
    return sqlite3.connect(DB_PATH)


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            documento TEXT,
            telefone TEXT,
            email TEXT,
            cidade TEXT,
            endereco TEXT,
            data_cadastro TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            whatsapp TEXT,
            cidade TEXT,
            consumo_medio REAL,
            potencia_kwp REAL,
            qtd_modulos INTEGER,
            data_cadastro TEXT
        )
    """)

    conn.commit()
    conn.close()


def salvar_cliente(nome, documento, telefone, email, cidade, endereco):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO clientes 
        (nome, documento, telefone, email, cidade, endereco, data_cadastro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        documento,
        telefone,
        email,
        cidade,
        endereco,
        datetime.now().strftime("%d/%m/%Y %H:%M")
    ))

    conn.commit()
    conn.close()


def listar_clientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, documento, telefone, email, cidade, data_cadastro
        FROM clientes
        ORDER BY id DESC
    """)

    dados = cursor.fetchall()
    conn.close()
    return dados


def salvar_lead(nome, whatsapp, cidade, consumo_medio, potencia_kwp, qtd_modulos):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO leads
        (nome, whatsapp, cidade, consumo_medio, potencia_kwp, qtd_modulos, data_cadastro)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nome,
        whatsapp,
        cidade,
        consumo_medio,
        potencia_kwp,
        qtd_modulos,
        datetime.now().strftime("%d/%m/%Y %H:%M")
    ))

    conn.commit()
    conn.close()


def listar_leads():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, nome, whatsapp, cidade, consumo_medio, potencia_kwp, qtd_modulos, data_cadastro
        FROM leads
        ORDER BY id DESC
    """)

    dados = cursor.fetchall()
    conn.close()
    return dados