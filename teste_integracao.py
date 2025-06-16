from codigo import soma, subtrai

class Repositorio:
    def __init__(self):
        self.historico = []
    def salvar_operacao(self, operacao, resultado):
        self.historico.append((operacao, resultado))
        return True
def executar_e_salvar(repo, operacao, a, b):
    if operacao == "soma":
        resultado = soma(a, b)
    elif operacao == "subtrai":
        resultado = subtrai(a, b)
    else:
        raise ValueError("Operação inválida")
    repo.salvar_operacao(operacao, resultado)
    return resultado
def test_salvar_operacao():
    repo = Repositorio()
    resultado = executar_e_salvar(repo, "soma", 5, 5)
    assert resultado == 10
    assert repo.historico[-1] == ("soma", 10)
