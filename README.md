# Filtro de Pedido Minimo para o Ifood

## Filtro Minimo Ifood

A aplicação corrige uma deficiencia que o sistema do Ifood de Web e App apresenta, não se encontra disponivel a opção para filtrar os restaurante do Ifood por 'Pedido Minimo' que é um valor minimo que o pedido precisa ter para ser confirmado! Basta informar o Local para obter a lista de restaurante filtrado.

## O que o projeto contém
- Request em Python

## Instalação
Para rodar o projeto faça essas configurações:
- Clone o projeto (utilizando comando git ou baixando em zip)
- Instale o Python (recomendado versão 3.8)
- Configure o main.py substituindo o latitude e longitude pelo local desejado para o filtro de restaurante da área, a Lat e Long pode ser obtido via [Google Maps](https://maps.google.com)
```
latitude = '-23.5401128'
longitude = '-46.6130155'
```
- Altere o Valor minimo procurado em main.py
```
valor_minimo = 10.0
```

## Endpoints
Lista de restaurantes abertos que correspondem critério específicado, resultado direto no Console no formato abaixo<br>
```
--------------

Restaurante: Nome do Restaurante
Link: https://www.ifood.com.br/delivery/sao-paulo-sp/restaurante-teste/11111
```
<br>![image](https://user-images.githubusercontent.com/19514153/164339599-7202df6d-5bfd-463a-8ba9-60cda531c848.png)

