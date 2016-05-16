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

print(porcentagem)  # print é a função que imprime na tela seus argumentos conteúdos da variável porcentagem 
{% endhighlight %}

Salvei esse texto como porcentagem.py e rodei o programa com o Python 3:

{% highlight bash %}
marcosrdac@201604261604:~/Desktop$ python3 porcentagem.py 
20.938628158844764
{% endhighlight %}

Wow! Já tá pronto... Mas eu não quero modificar o programa toda vez que for utilizá-lo. Vamos arrumá-lo:

