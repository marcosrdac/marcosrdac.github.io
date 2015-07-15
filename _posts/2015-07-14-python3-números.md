---
layout: post
title:  "Python 3 - Aula 1: Números" 
---

Existem três tipos de dados para números na versão atual do Python. Seja introduzido a eles e a como lidar com eles abaixo.


## Tipos de dados numéricos


### int (obs.: engloba o antigo tipo *long*)

Tipo de dados para números inteiros.

{% highlight python3 %}
>>> 1              # bem chato, mesmo... A perfeição é chata.
1
{% endhighlight %}


### float

Tipo para os reais. 

{% highlight python3 %}
>>> 6.2831853072   # isto é um float; um número racional. Na verdade, se você
6.2831853072       # sabe que número é esse, sabe que ele não é racional. Se
                   # não sabe, tenha sua mente explodida lendo sobre ele!
{% endhighlight %}

*Float* vem do inglês *floating point* - números "de ponto flutuante" - assim chamados por usarem notação matemática similar à científica, mas em base 2, o que facilita cálculos de números fracionários nas máquinas digitais. Existe um problema com os *floating point numbers*. Leia sobre ele [aqui]({* post_url problemas-com-floating-numbers *}).


### complex

Tipo numérico para os complexos.

{% highlight python3 %}
>>> 2 + 3j         # forma padrão "a + bi | a, b ∉ R"; j = i = sqrt(-1)
(2+3j)

>>> (2+3j)         # dá pra mandar desse jeito diferentoso que ele retorna,
(2+3j)             # também

>>> 5j             # dá pra fazer assim, também, no caso de não haver um 
5j

>>> 
{% endhighlight %}


Não acabou ainda, Emerson. Tô terminando isso aqui ainda. uashuahsuahsuha
