class ExtratorURL:
    def __init__(self, url):
        self.url = url.strip()
        self.valida_url()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL está vazia")

    def __str__(self):
        return self.url

    def get_url_base(self, url):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_do_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_do_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor_busca = self.get_url_parametros()[indice_valor:]
        else:
            valor_busca = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor_busca

















extrator_url = ExtratorURL('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
print(extrator_url)
valor_quantidade = extrator_url.get_valor_parametro("quanidade")
print(valor_quantidade)