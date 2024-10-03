# Preenchimento de Dados com CEPs

Este script tem como objetivo preencher informações de endereço em um arquivo Excel com base nos CEPs fornecidos. Ele utiliza a API pública **ViaCEP** para buscar os dados referentes a CEPs do Brasil e atribui informações como bairro, UF e código do município IBGE no arquivo Excel.

## Funcionalidades

- **Consulta de CEP**: Utiliza a API do **ViaCEP** para buscar informações detalhadas de endereços do Brasil com base nos CEPs.
- **Atualização de Dados**: Preenche colunas específicas do arquivo Excel (`District`, `Cód. Território`, `Cód. Municipio IBGE`) com os dados obtidos pela consulta.
- **Suporte para Países Exteriores**: Para CEPs fora do Brasil, atribui valores padrão para os campos (`Cód. Território` e `Cód. Municipio IBGE`).

## Pré-requisitos

Para executar este script, é necessário:

- **Python 3.x** instalado.
- Bibliotecas Python necessárias: **pandas** e **requests**.

Você pode instalar as bibliotecas usando o seguinte comando:

```sh
pip install pandas requests
```

## Como usar

1. **Preparar o Arquivo Excel de Entrada**:
   - Prepare um arquivo Excel chamado `Post_Code.xlsx` com a seguinte estrutura de colunas:
     - `Country/Region Code`: Código do país, por exemplo, 'BR' para Brasil.
     - `Code`: O CEP a ser pesquisado.
     - Outras colunas opcionais, como `District`, `Cód. Território`, `Cód. Municipio IBGE`, que serão preenchidas pelo script.

   Exemplo de como deve ser a estrutura do Excel:

   | Country/Region Code | Code    | District | Cód. Território | Cód. Municipio IBGE |
   |---------------------|---------|----------|-----------------|---------------------|
   | BR                  | 01001-000 |          |                 |                     |
   | US                  | 10001   |          |                 |                     |

2. **Executar o Script**:
   - Atualize o caminho do arquivo Excel (`file_path`) e o caminho de saída (`output_path`) no script conforme necessário.
   - Execute o script Python:

   ```sh
   python preencher_cep.py
   ```

3. **Arquivo de Saída**:
   - O script gera um arquivo Excel de saída contendo as informações adicionais preenchidas. O arquivo é salvo no caminho definido como `output_path`.

## Observações

- **API ViaCEP**: Este script utiliza a API gratuita do ViaCEP para buscar informações sobre os CEPs do Brasil. Caso o CEP não seja encontrado, os campos são preenchidos com valores padrão vazios.
- **Limitações**: A API ViaCEP só fornece informações para CEPs do Brasil. Para outros países, são atribuídos valores como `EX` (Exterior) para `Cód. Território` e `9999999` para `Cód. Municipio IBGE`.

