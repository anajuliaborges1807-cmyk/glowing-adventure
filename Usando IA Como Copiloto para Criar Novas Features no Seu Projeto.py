def testar_sistema_de_pontos():
    # Teste 1: Não deve subir de nível ainda
    pontos, subiu = adicionar_pontos(50, 20)
    assert pontos == 70 and subiu == False

    # Teste 2: Deve subir de nível
    pontos, subiu = adicionar_pontos(90, 15)
    assert pontos == 105 and subiu == True
    
    print("✅ Todos os testes gerados pela IA passaram!")

testar_sistema_de_pontos()