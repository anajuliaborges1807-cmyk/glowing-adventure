def adicionar_pontos(pontos_atuais, pontos_ganhos):
    novos_pontos = pontos_atuais + pontos_ganhos
    print(sugestao_ia := f"Você ganhou {pontos_ganhos} pontos! Total: {novos_pontos}")
    
    # Se passar de 100 pontos, sobe de nível
    if novos_pontos >= 100:
        print("🎉 Parabéns! Você subiu de nível!")
        return novos_pontos, True
    
    return novos_pontos, False

# Testando a sugestão da IA
pontos, subiu = adicionar_pontos(80, 25)