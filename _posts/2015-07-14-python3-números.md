---
layout: post
title:  "Python 3 - Aula 1: Números" 
---

Existem três tipos de dados para números na versão atual do Python. Seja introduzido a eles e a como lidar com os mesmos abaixo.


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
                   # não sabe, tenha sua mente explodida lendo sobre o "Tau"!
{% endhighlight %}

*Float* vem do inglês *floating point* - números "de ponto flutuante" - assim chamados por usarem notação matemática similar à científica, mas em base 2, o que facilita cálculos envolvendo números fracionários nas máquinas digitais. Existe um problema com os *floating point numbers*. Leia sobre ele [aqui]({* post_url problemas-com-floating-numbers *}). ~~me lembre de fazer esse post!~~


### complex

Tipo numérico para os complexos.

{% highlight python3 %}
>>> 2 + 3j  # forma padrão "a + bi | a, b ∈ R"; j = i = sqrt(-1)
(2+3j)

>>> (2+3j)  # também dá pra mandar desse jeito diferentoso que ele retorna
(2+3j)

>>> 5j      # E assim, no caso de a parte real ser 0.
5j

>>> 
{% endhighlight %}


Não acabou ainda, Emerson e Miss. Free Hugs. Ainda tô começando isso aqui! uashuahsuahsuha
