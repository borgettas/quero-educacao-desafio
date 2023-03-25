# 📄 Documentação

## Objetivo geral
Desenvolver um ambiente onde é possivel exibir e exportar um relaório de forma resumida sobre logs.

</br>

## Solução
Criado um ambiente conteinerizado utilizando uma imagem do Python. A partir dessa imagem,  foi criado um CI de forma a facilitar a usablidade da aplicação.

</br>
</br>

# 🗂️ Estrutura do projeto
```
.
├── app
│   └── index.py
├── Dockerfile
├── Makefile
├── README.md
├── requirements.txt
├── sre-intern-test
│   └── output.json
└── tests
    ├── __init__.py
    └── test_index.py

```

</br>

## App
Diretório responsável por armazenar os scripts que realizam a consulta dos logs e manipula a função do Argparse.

## Tests
Diretório responsável por armazenar os testes unitários.

</br>
</br>

# ⛏️ Preparando o ambiente localmente
## Requisitos
- Makefile
- Docker;
- 5GB de armazenamento;
- Conexão a internet.

</br>

## ⚠️ Importante saber
Todos os comandos necessários para construção do ambiente estão no arquivo <kbd>Makefile</kbd>.

</br>

## A. Instalando
Os comando abaixo precisam ser inseridos no terminal da pasta raiz do projeto.
1. Construindo o ambiente <kbd>make start</kbd>

</br>

## B. CI

No terminal, insira os comandos abaixo:
1. <kbd>python app/index.py -h</kbd> - mostrará todas as opções do CI.

</br>

## C. Output

Os dados quando forem escolhidos para serem exportados irão para o diretório
<kbd>app/sre-intern-test/</kbd>.

</br>

## D. Testes

Para execução dos testes insira na pasta raiz do projeto <kbd>make test</kbd>.

</br>
</br>

# 👌 Ambiente Finalizado

</br>

# Outros comandos
1. Saindo do container <kbd>CTRL + D</kbd>
2. Excluindo o ambiente <kbd>make finish</kbd>