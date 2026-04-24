# Zipador de Componentes

Automação em Python para compactar, em lote, cada subpasta de um diretório de componentes em arquivos `.zip` individuais.

## Objetivo

Este projeto foi criado para:

- Ler uma pasta de origem contendo várias subpastas.
- Gerar um arquivo `.zip` para cada subpasta encontrada.
- Salvar todos os arquivos zipados em uma pasta de destino.

## Como Funciona

O script:

1. Carrega as variáveis `SOURCE_DIR` e `DEST_DIR` do arquivo `.env`.
2. Valida se os caminhos informados existem e se a origem é uma pasta.
3. Cria a pasta de destino automaticamente, se necessário.
4. Percorre apenas as subpastas diretas de `SOURCE_DIR`.
5. Gera um `.zip` por subpasta, preservando a estrutura interna dos arquivos.

## Estrutura do Projeto

```text
.
├── zipador.py
├── .env
├── .env.exemplo
├── .gitignore
└── LICENSE
```

## Requisitos

- Windows (ou outro sistema com Python 3.10+)
- Python instalado globalmente

## Configuração

1. Crie/edite o arquivo `.env` na raiz do projeto.
2. Defina os caminhos de origem e destino:

```env
SOURCE_DIR=C:\Users\seu.usuario\caminho\da\pasta\components
DEST_DIR=C:\Users\seu.usuario\caminho\da\pasta\zipados
```

Use o arquivo `.env.exemplo` como referência.

## Execução

No diretório do projeto, execute:

```bash
python zipador.py
```

## Saída Esperada

Exemplo de logs no terminal:

```text
Total de pastas encontradas: 74
OK: NomeDaPasta -> C:\caminho\destino\NomeDaPasta.zip
Processo finalizado.
```

## Tratamento de Erros

O script informa mensagens claras para cenários como:

- `.env` ausente ou incompleto.
- Pasta de origem inexistente.
- Pasta de origem inválida (não é diretório).
- Falha ao compactar uma pasta específica.

## Boas Práticas

- Não versionar o arquivo `.env` com caminhos sensíveis do seu ambiente.
- Versionar o `.env.exemplo` para padronizar a configuração do projeto.
- Executar o script com permissões de leitura na origem e escrita no destino.

## Licença

Este projeto esta licenciado sob a Licenca MIT.

Para mais detalhes, consulte o arquivo `LICENSE`.
