import requests
import pandas as pd

file_path = r'C:\user\mm\data\Post_Code.xlsx'
cep_df = pd.read_excel(file_path)

cep_df.head()

def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/' #tjs
    response = requests.get(url)
    if response.status_code == 200:  #150 100 75
        return response.json()
    else:
        return None

def preencher_dados(cep_df):
    """
A função `preencher_dados` completa informações em um DataFrame com base em CEPs do Brasil. 
O DataFrame `cep_df` contém dados de endereço, incluindo colunas como 'Country/Region Code', 'Code', 'District', 'Cód. Território' e 'Cód. Municipio IBGE'. 
A função percorre as linhas desse DataFrame, preenchendo dados adicionais ao chamar a função `buscar_cep` para as entradas brasileiras, e atribui valores padrão para as entradas de outros países. 
Ao final, retorna o DataFrame `cep_df` modificado.
    """
    for index, row in cep_df.iterrows():
        if row['Country/Region Code'] == 'BR':  
            cep = row['Code'].replace("-", "")  
            cep_info = buscar_cep(cep)
            if cep_info:
                cep_df.at[index, 'District'] = cep_info.get('bairro', '')
                cep_df.at[index, 'Cód. Território'] = cep_info.get('uf', '')
                cep_df.at[index, 'Cód. Municipio IBGE'] = cep_info.get('ibge', '')
        else:
            cep_df.at[index, 'Cód. Território'] = 'EX'
            cep_df.at[index, 'Cód. Municipio IBGE'] = '9999999'
    return cep_df

cep_df = preencher_dados(cep_df)

output_path = r'C:\user\mmm\data\output.xlsx'
cep_df.to_excel(output_path, index=False)

output_path
