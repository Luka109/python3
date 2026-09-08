produtos = []

for i in range(10):
    print(f"\nProduto {i + 1}")

    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço: R$ "))

    produtos.append({
        "nome": nome,
        "preco": preco
    })

# Encontrando o mais caro e o mais barato
mais_caro = max(produtos, key=lambda produto: produto["preco"])
mais_barato = min(produtos, key=lambda produto: produto["preco"])

print("\n===== RESULTADO =====")
print(f"Total de produtos: {len(produtos)}")
print(f"Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")
print(f"Produto mais barato: {mais_barato['nome']} - R$ {mais_barato['preco']:.2f}")
