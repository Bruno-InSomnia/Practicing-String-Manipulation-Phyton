
class ExtratorURL:
    def __init__(self, url):
        self.url = self.satizador_url(url)
        self.valida_url()

    def satizador_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url or not self.url.startswith('https'):
            raise ValueError('A URL está vazia.')

    def get_url_base(self, url):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_buscado(self, parametro_busca):
        indice_parametro_busca = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro_busca + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&', indice_parametro_busca)
        if indice_e_comercial == -1:
            valor_busca = self.get_url_parametro()[indice_valor:]
        else:
            valor_busca = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor_busca


url1 = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
valor_quantidade = url1.get_valor_buscado('quantidade')
print(valor_quantidade)

# parametro_busca = 'moedaOrigem'


# print(indice_interrogacao)
# print(url_parametros)
# print(indice_parametro_busca)
# print(indice_e_comercial)
# print(valor_busca)

