---
layout: post
title:  "Python 3 - Números: introdução aos tipos numéricos" 
---


Existem três tipos de dados para números na versão atual do Python. Seja introduzido a eles e a como lidar com os mesmos abaixo.


## Tipos de dados numéricos


### O tipo "int"

Tipo de dados para números inteiros (engloba o antigo tipo *long*).

{% highlight python3 %}
>>> 1  # bem chato, mesmo... A perfeição é chata.
1
{% endhighlight %}


### O tipo "float"

Tipo para os reais. 

{% highlight python3 %}
>>> 6.2831853072  # isto é um float; um número racional. Na verdade, se você
6.2831853072      # sabe que número é esse, sabe que ele não é racional. Se
                  # não sabe, tenha sua mente explodida lendo sobre o "Tau"!
{% endhighlight %}

*Float* vem do inglês *floating point* - números "de ponto flutuante" - assim chamados por usarem notação matemática similar à científica, mas em base 2, o que facilita cálculos envolvendo números fracionários nas máquinas digitais. Existe um problema com os *floating point numbers*. Leia sobre ele [aqui]({* post_url problemas-com-floating-numbers *}). ~~me lembre de fazer esse post!~~


### O tipo "complex"

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


## Ordem de abrangência numérica

Uma operação entre números sempre tem como resultado um outro número de tipo igual ou mais geral. O tipo será igual ao tipo mais abrangente entre os operandos, a menos que estejamos falando de uma divisão entre inteiros quaisquer, o que geraria um "float", ou da raiz de um negativo, que retornaria um "complex".
A ordem de abrangência numérica (em ordem crescente) é a seguinte:

* int
* float
* complex

Para provar isso no Python, vou utilizar a função type(), que retorna o tipo (seja número, lista, string, ou classe que for) da informação posta entre os parêntesis (argumento).

{% highlight python3 %}
>>> type(1 + 1)
<class 'int'>

>>> type(2 - 1)
<class 'int'>

>>> type(4 * 2)
<class 'int'>

>>> type(4 / 2)
<class 'float'>

>>> type(2 ** 2)
<class 'int'>

>>> type(4 ** (1/2))
<class 'float'>

>>> type(3 // 2)
<class 'int'>

>>> type(2j - 3)
<class 'complex'>

>>> type(3 * 2j)
<class 'complex'>

type(2.28/2.28)
<class 'float'>

>>> type(2j / 2j)
<class 'complex'>
{% endhighlight %}


## Transformando tipos numéricos em outros

Pode-se transformar um float num inteiro, cortando seus decimais, pela função int(umFloatQualquer). Pode-se ainda transformar um inteiro num float pela função float(umIntQualquer). pode-se passar qualquer um destes para complex, o tipo numérico mais abrangente, por meio da função complex(umNúmeroQualquer), mas a recíproca não é verdadeira. Caso um int ou float seja transformado para seu próprio tipo, nenhum erro será acionado. Nada acontecerá, além do retorno do argumento dado.

Aqui:

{% highlight python3 %}
>>> int(3.0)  # float
3             # int

>>> float(3)  # int
3.0           # float

>>> complex(3)  #int
(3+0j)          #complex

>>> complex(3.0)  #float
(3+0j)            # complex

>>> int(1j)  # vai dar erro; a parte complexa não é simplesmente cortada
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: can't convert complex to int

>>> float(1j)  # igualmente
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: can't convert complex to float

>>> int(1)  # int
1           # int

>>> float(1.0)  # float
1.0             # float
{% endhighlight %}
