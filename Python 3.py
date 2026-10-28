
produtos = []

for i in range(10):
    print(f"\nProduto {i + 1}")

    nome = input("Digite o nome do produto: ").strip()

    while not nome:
        print("O nome não pode ficar vazio.")
        nome = input("Digite o nome do produto: ").strip()

    while True:
        try:
            entrada = input("Digite o preço: R$ ").strip()
            preco = float(entrada.replace(",", "."))

            if preco < 0:
                print("O preço não pode ser negativo.")
                continue

            break
        except ValueError:
            print("Preço inválido! Digite um valor como 10,50 ou 10.50.")

    produtos.append({
        "nome": nome,
        "preco": preco
    })

# Encontrando o produto mais caro e o mais barato
mais_caro = max(produtos, key=lambda produto: produto["preco"])
mais_barato = min(produtos, key=lambda produto: produto["preco"])

print("\n===== RESULTADO =====")
print(f"Total de produtos: {len(produtos)}")
print(f"Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")
print(f"Produto mais barato: {mais_barato['nome']} - R$ {mais_barato['preco']:.2f}")
