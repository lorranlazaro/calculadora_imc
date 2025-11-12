# 🧮 Calculadora de IMC (Índice de Massa Corporal)

Projeto desenvolvido para calcular o **IMC (Índice de Massa Corporal)** e informar a classificação de acordo com a OMS.  

------------------------------------------------------------------------

## 📘 O que é IMC?

O **IMC** é um índice usado mundialmente para identificar se uma pessoa está com:

- Peso abaixo do ideal
- Peso adequado
- Sobrepeso
- Algum grau de obesidade

É um cálculo simples, porém eficiente para avaliação inicial do estado nutricional.

------------------------------------------------------------------------

## 🧠 Fórmula do IMC

```
IMC = peso / (altura²)
```

Onde:

- **peso** → quilogramas (kg)
- **altura** → metros (m)

Exemplo:

```
Peso: 70 kg
Altura: 1,75 m

IMC = 70 / (1.75 * 1.75)
IMC = 22.86
```

------------------------------------------------------------------------

## 📊 Classificação do IMC (OMS)

| Resultado do IMC       | Classificação                    |
|------------------------|----------------------------------|
| Menor que 18,5         | Abaixo do peso                   |
| Entre 18,5 e 24,9      | Peso ideal (normal)              |
| Entre 25,0 e 29,9      | Sobrepeso                        |
| Entre 30,0 e 34,9      | Obesidade Grau I                 |
| Entre 35,0 e 39,9      | Obesidade Grau II (Severa)       |
| Maior ou igual a 40,0  | Obesidade Grau III (Grave)       |

------------------------------------------------------------------------

## 📁 Estrutura do projeto

```
CALCULADORA_IMC/
│── src/
│   └── calculadora_imc.py
│── .gitignore
│── README.md
│── requirements.txt

```
------------------------------------------------------------------------

## ▶️ Como executar o projeto

1. Clone o repositório:
   ```bash
   git clone https://github.com/lorranlazaro/calculadora_imc.git
   ```

2. Instale as dependências (se houver):
   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:
   ```bash
   python calculadora_imc.py
   ```
------------------------------------------------------------------------

## 🧰 Tecnologias Utilizadas

- **Linguagem:** Python  
- **Ferramentas recomendadas:** VS Code, terminal do sistema operacional

------------------------------------------------------------------------

## ✍️ Autor

Desenvolvido por **[Lorran Lázaro]** 💻  
📧 E-mail: [lorranfelippe81@gmail.com]  
🌐 GitHub: [https://github.com/lorranlazaro]

------------------------------------------------------------------------

## 📜 Licença MIT

Este projeto está licenciado sob a **Licença MIT** — sinta-se livre para usar, modificar e distribuir.

```
MIT License

Copyright (c) 2025 Lorran Lázaro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```

✨ Desenvolvido para fins de estudo e evolução contínua na linguagem Python.
