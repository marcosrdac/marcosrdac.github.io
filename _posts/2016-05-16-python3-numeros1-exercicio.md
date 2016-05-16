---
layout: post
title:  "Python 3 - Números 1: Exercícios"
---

Que tal fazer um programinha simples pra exercitar o conhecimento de números em Python da aula passada?

## Um motivador de leitura

Quando estou lendo Filosofia ou qualquer outro algo de Humanas, minha alma busca o equilíbrio com Exatas por meio de uma conta simples, a cada parada: calculo a porcentagem lida até o momento. Que tal fazer um programa que faz esse cálculo pra mim e tira minha única forma de manter o equilíbrio? Parece chato? Concordo.

Uma coisa que eu acho muito legal do Python é a de que você pode declarar variáveis à hora que quiser, ao contrário de C e Pascal, por exemplo. Nestas linguagens, você deve declará-las antes de as definir e usar, numa parte específica inicial do programa. Mas o que é declarar uma variável? É criar e nomear um local de memória para dados. Vamos fazer isso a seguir.

Para calcular a porcentagem de uma coisa em relação à outra, precisamos de dois dados:
    * o número que corresponde à parte (minha página atual)
    * o número que corresponde ao todo (a quantidade de páginas do livro)

vamos declarar essas variáveis em um exemplo:

{% highlight python %}
pagAtual = 58  # página atual
numPags = 277  # número de páginas do livro

porcentagem = pagAtual / numPags * 100  # matemática do prézinho

print(porcentagem)  # print é a função que imprime na tela seus argumentos
                    # conteúdos da variável porcentagem 
{% endhighlight %}

Salvei esse texto como porcentagem.py e rodei o programa com o Python 3:

{% highlight bash %}
marcosrdac@201604261604:~/Desktop$ python3 porcentagem.py 
20.938628158844764
{% endhighlight %}

Wow! Já tá pronto... Mas eu não quero modificar o programa toda vez que for utilizá-lo. Vamos arrumá-lo. Não colocaremos mais um número fixo para o programa. Ao invés disso, será o usuário que irá fazê-lo. Usaremos a função *input*. ela toma um argumento, que será uma mensagem que indica ao usuário que dado fornecer. Esse dado será então transformado em número inteiro, pois o *input* retorna o dado fornecido como *string*, texto, e não número.

{% highlight python %}
pagAtual = input('Em que página você parou? ')    # página atual
pagAtual = int(pagAtual)
numPags = input('Quantas páginas o livro tem? ')  # número de páginas do livro
numPags = int(numPags)

porcentagem = pagAtual / numPags * 100  # matemática do prézinho

print(porcentagem)  # print é a função que imprime na tela seus argumentos
                    # conteúdos da variável porcentagem 
{% endhighlight %}

Agora ele fica assim:

{% highlight bash %}
marcosrdac@201604261604:~/Desktop$ python3 porcentagem.py 
Em que página você parou? 58
Quantas páginas o livro tem? 277
20.938628158844764
{% endhighlight %}

Mas usamos 4 linhas no lugar do que poderiam ser 2, de maneira ainda organizada. Além disso, ele está feio. Nova versão:

{% highlight python %}
livro = input('Que livro você está lendo? ')      # nome do livro
pagAtual = int(input('Em que página você parou? '))    # página atual
numPags = int(input('Quantas páginas o livro tem? '))  # número de páginas do livro

# matemática do prézinho com arredondamento na 2ª casa decimal
porcentagem = round(pagAtual / numPags * 100, 2)

print()

# essas chaves ({}) informam em que posição do texto as variáveis dadas em format serão postas
print('Você já leu {}% de {}!!! Ótimo trabalho, lindão, gostoso, casa comigo!'.format(porcentagem, livro))
{% endhighlight %}

Agora sim, tá motivador! hahaha
Veja o resultado:

{% highlight bash %}
marcosrdac@201604261604:~/Desktop$ python3 porcentagem.py 
Que livro você está lendo? Humano, demasiado humano
Em que página você parou? 58
Quantas páginas o livro tem? 277

Você já leu 20.94% de Humano, demasiado humano!!! Ótimo trabalho, lindão, gostoso, casa comigo!
{% endhighlight %}
