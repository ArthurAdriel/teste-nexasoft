from codigo import soma, subtrai, multiplica, divide

def test_fluxo_completo_usuario():
    # Usuário faz várias operações seguidas
    resultado1 = soma(10, 5)
    resultado2 = subtrai(resultado1, 3)
    resultado3 = multiplica(resultado2, 2)
    resultado4 = divide(resultado3, 4)
    # Fluxo: (10+5)=15 -> (15-3)=12 -> (12*2)=24 -> (24/4)=6
    assert resultado4 == 6
