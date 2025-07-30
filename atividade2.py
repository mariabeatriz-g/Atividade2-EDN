#Calculadora de Desconto
nome_do_produto = "Camiseta"
preco_original = 50.00
porcentagem_de_desconto = 20

#Aplicando o desconto
desconto = preco_original * (porcentagem_de_desconto / 100)

# Cálculo do preço final com desconto
preco_final = preco_original - porcentagem_de_desconto

#Resultado
print("Produto:", nome_do_produto)
print("Preço original: R$ {:.2f}".format(preco_original))
print("Desconto: {}% (R$ {:.2f})".format(porcentagem_de_desconto, desconto))
print("Preço final com desconto: R$ {:.2f}".format(preco_final))