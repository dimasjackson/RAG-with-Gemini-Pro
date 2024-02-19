# RAG-with-Gemini-Pro
Chat com perguntas e respostas para os seus dados usando Google Gemini-Pro e Geração Aumentada por Recuperação (RAG)\
Questions and answers with your data using Google Gemini-Pro and Retrieval Augmented Generation (RAG)
![Captura de Tela 2024-02-19 às 11 43 49](https://github.com/dimasjackson/RAG-with-Gemini-Pro/assets/114688989/5d9907dc-6d9d-4314-b89c-3a528e891cf7)

Contexto fornecido:
![Captura de Tela 2024-02-19 às 11 40 15](https://github.com/dimasjackson/RAG-with-Gemini-Pro/assets/114688989/a0167a13-741b-4604-b08f-9db7ee2ff09e)

## User:	
Descreva o documento fornecido
## Model:	
O documento fornecido é uma **lista de alunos matriculados em cursos universitários**, incluindo as seguintes informações para cada aluno:

* **Nome:** O nome do aluno.
* **Inscrição:** O número de inscrição do aluno.
* **Curso:** O curso em que o aluno está matriculado.
* **Sexo:** O sexo do aluno (feminino ou masculino).
* **Bairro:** O bairro onde o aluno reside.
* **Cidade:** A cidade onde o aluno reside.
* **Data de Nascimento:** A data de nascimento do aluno.
* **Tipo de Escola:** O tipo de escola onde o aluno concluiu o ensino médio (privada ou pública).

A lista inclui dados de **7 alunos** matriculados em **6 cursos** diferentes em **4 cidades** diferentes.
User:	Quantos alunos estão inscritos no curso de direito?
Model:	**2 alunos** estão inscritos no curso de Direito, conforme a lista fornecida:

* Raquel (inscrição nº 2)
* Marcos (inscrição nº 5)

Observe que ambos os alunos inscritos em Direito são do sexo feminino.
User:	Qual o percentual de inscritos no curso de Publicidade e Propaganda?
Model:	Há **1 aluno** inscrito no curso de Publicidade e Propaganda, em um total de **7 alunos** na lista fornecida.

Portanto, o percentual de inscritos no curso de Publicidade e Propaganda é:

```
(1 / 7) * 100% ≈ 14,29%
```

Ou seja, aproximadamente **14,29%** dos alunos na lista estão inscritos no curso de Publicidade e Propaganda.

## User:
Qual o percentual de inscritos no curso de Direito?

## Model:
Há **2 alunos** inscritos no curso de Direito, em um total de **7 alunos** na lista fornecida.

Portanto, o percentual de inscritos no curso de Direito é:

```
(2 / 7) * 100% ≈ 28,57%
```

Ou seja, aproximadamente **28,57%** dos alunos na lista estão inscritos no curso de Direito.

## User:
Qual a média de idade dos inscritos?
## Model:
Para calcular a média de idade dos inscritos, precisamos primeiro calcular a idade de cada aluno com base na data de nascimento fornecida:

* Maria: 18 anos (2023 - 2004)
* Raquel: 22 anos (2023 - 2000)
* Rute: 18 anos (2023 - 2004)
* Rebeca: 20 anos (2023 - 2003)
* Marcos: 17 anos (2023 - 2005)
* Lucas: 16 anos (2023 - 2006)
* Isabel: 22 anos (2023 - 2000)

Em seguida, somamos as idades de todos os alunos e dividimos pelo número total de alunos:

```
(18 + 22 + 18 + 20 + 17 + 16 + 22) / 7 = 19,0
```

Portanto, a média de idade dos inscritos é de aproximadamente **19 anos**.
