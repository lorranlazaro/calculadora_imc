# Cálculo de IMC - Índice de Massa Corporal

if __name__ == "__main__":

    while True:

        print("\nVAMOS CALCULAR O SEU IMC - ÍNDICE DE MASSA CORPORAL\n")

        try:
            inicio = (
                input("Deseja fazer o teste de IMC? Digite S ou N: ").strip().lower()
            )

            if inicio not in ("s", "n"):
                raise ValueError

        except ValueError:
            print("\nEntrada inválida! Digite apenas S ou N.\n")
            continue

        if inicio == "n":
            print("\nEncerrando o programa...")
            break

        try:
            altura = float(
                input("Informe a sua altura em metros (ex.: 1.75): ").strip()
            )
            peso = float(input("Informe o seu peso em kg (ex.: 70): ").strip())

        except ValueError:
            print(
                "\nEntrada inválida! Digite somente números usando ponto (ex.: 1.75).\n"
            )
            continue

        imc = peso / (altura**2)

        print(f"\nSeu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Você está ABAIXO DO PESO")
        elif imc >= 18.5 and imc < 24.9:
            print("Você está no PESO IDEAL")
        elif imc >= 25.0 and imc < 29.9:
            print("Você está com SOBREPESO")
        elif imc >= 30.0 and imc < 34.9:
            print("Você está com OBESIDADE GRAU I")
        elif imc >= 35.0 and imc < 39.9:
            print("Você está com OBESIDADE GRAU II (Severa)")
        else:
            print("Você está com OBESIDADE GRAU III (Grave)")

        print("\nCálculo Efetuado!\n")
