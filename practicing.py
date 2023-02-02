import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.satizador_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "URL Base: " + self.get_url_base() + "\n" + "Parâmetros: " + self.get_url_parametro() + "\n" + 'Conversão: ' + f'{self.get_conversao():.2f}'.replace('.', ',') + ' ' + f'{self.get_moeda()}.'

    def __eq__(self, other):
        return self.url == other.url

    def satizador_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia.')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('A URL não é válida')

    def get_url_base(self):
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

    def get_conversao(self):
        origem = self.get_valor_buscado('moedaOrigem')
        quantidade = int(self.get_valor_buscado('quantidade'))

        if origem == 'real':
            conversao = quantidade / 5.50
        else:
            conversao = quantidade * 5.50
        return conversao

    def get_moeda(self):
        if self.get_conversao() <= 1:
            moeda = self.get_valor_buscado('moedaOrigem')
        else:
            if self.get_valor_buscado('moedaOrigem') == 'dolar':
                moeda = 'reais'
            else:
                moeda = 'dólares'
        return moeda




url1 = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
url2 = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=dolar&moedaDestino=real&quantidade=5')

print(url1)
print(url2)

# parametro_busca = 'moedaOrigem'

# valor_quantidade = url1.get_valor_buscado('quantidade')
# print(indice_interrogacao)
# print(url_parametros)
# print(indice_parametro_busca)
# print(indice_e_comercial)
# print(valor_busca)

