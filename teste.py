import psycopg2

config = {
    "dbname": "postgres", 
    "user": "postgres", 
    "password": "1234", 
    "host": "localhost",  
    "port": 5432          
}

try:
    
    conn = psycopg2.connect(**config)
    cursor = conn.cursor()

    
    def listar_jogos_por_string(busca):
        busca = f"%{busca}%" 
        cursor.execute("""
            SELECT titulo, subtitulo FROM jogos
            WHERE titulo ILIKE %s OR subtitulo ILIKE %s
        """, (busca, busca))
        resultados = cursor.fetchall()
        if resultados:
            print("Jogos encontrados:")
            for titulo, subtitulo in resultados:
                print(f"- {titulo} ({subtitulo})")
        else:
            print("Nenhum jogo encontrado com a string fornecida.")

    def listar_jogos_ordenados():
        cursor.execute("SELECT titulo, subtitulo FROM jogos ORDER BY titulo ASC")
        jogos = cursor.fetchall()
        print("Jogos ordenados por título:")
        for titulo, subtitulo in jogos:
            print(f"- {titulo} ({subtitulo})")

    def listar_jogos_com_k():
        cursor.execute("""
            SELECT titulo, subtitulo FROM jogos
            WHERE titulo ILIKE '%k%' OR subtitulo ILIKE '%k%'
        """)
        jogos = cursor.fetchall()
        if jogos:
            print("Jogos que contêm a letra 'k':")
            for titulo, subtitulo in jogos:
                print(f"- {titulo} ({subtitulo})")
        else:
            print("Nenhum jogo contém a letra 'k'.")

    while True:
        print("\nMenu:")
        print("1 - Buscar jogos por string")
        print("2 - Listar jogos ordenados por título")
        print("3 - Listar jogos que contêm 'k'")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            busca = input("Digite a string para buscar: ")
            listar_jogos_por_string(busca)
        elif opcao == "2":
            listar_jogos_ordenados()
        elif opcao == "3":
            listar_jogos_com_k()
        elif opcao == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

except psycopg2.Error as e:
    print(f"Erro ao conectar ao banco de dados: {e}")
finally:
    if 'conn' in locals():
        cursor.close()
        conn.close()
        print("Conexão com o banco de dados encerrada.")
