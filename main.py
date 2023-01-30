
# URL de exemplo
# url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
url = " "

# Sanitização e Validação da URL
if url.strip() == "":
    raise ValueError("A URL está vazia")

# Separando base e parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao + 1:]

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_do_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_do_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)
if indice_e_comercial == -1:
    valor_busca = url_parametros[indice_valor:]
else:
    valor_busca = url_parametros[indice_valor:indice_e_comercial]
print(valor_busca)