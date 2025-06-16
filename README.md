# teste-nexasoft
Prática de teste automatizado com o GitGHub Actions da empresa NexaSoft Tech.
Este repositório foi criado para o trabalho da A3 da matéria de Gestão e Qualidade de Software. Ele demonstra a aplicação de uma pipeline básica de integração contínua (CI) com execução automática de testes usando o GitHub Actions. O objetivo desse repositório é de simular um processo DevOps moderno para a empresa fictícia NexaSoft Tech.


Este projeto que nós criamos possui três tipos de testes, cobrindo diferentes níveis de verificação de qualidade:
Testes Unitários (`teste.py`)
Verificam o funcionamento isolado das funções principais (`soma`, `subtrai`, etc.).
Utilizam a biblioteca **Pytest**.

Testes de Integração (`teste_integracao.py`)
Simulam a interação entre funções e um “repositório de dados” (como se fosse um banco).
Verificam se os dados são processados e armazenados corretamente juntos.

Testes End-to-End (`teste_e2e.py`)
Executam um fluxo completo de uso, simulando a experiência real de um usuário.
Verificam se a sequência de operações retorna o resultado final esperado.


GitHub Actions
Sempre que um novo commit ou pull request é feito na branch `main`, o GitHub executa automaticamente todos os testes definidos no projeto.
O pipeline está configurado no arquivo:  
`.github/workflows/tests.yml`
