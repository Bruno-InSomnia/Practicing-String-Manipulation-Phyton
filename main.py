from abc import ABC
from collections.abc import MutableSequence


class Url(MutableSequence):
    def __init__(self, endereco):
        self.endereco = endereco

    def __getitem__(self, item):
       return super().__getitem__(index=0)

    def __delitem__(self, key):
        super().__delitem__()

    def __len__(self):
        super().__delitem__()

    def __setitem__(self, key, value):
        super().__setitem__()

    def insert(self, index: int, value: 5) -> None:
        pass


url1 = Url('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
print(url1.endereco)

palavras_url = [Url]

lista_de_caracteres = []

for caractere in url1:
    index = 0
    caractere = lista_de_caracteres[index]
    index += 1

print(lista_de_caracteres)

# for letra in palavras_url[]:
#     if letra == 'a':
#         print('Tem mesmo!')
#     else:
#         print('Não tem!')



#
# url_base = url[0:27]
# print(url_base)
#
# url_parametro = url[27:78]
# print(url_parametro)
