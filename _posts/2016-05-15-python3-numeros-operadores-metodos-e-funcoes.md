---
layout: post
title:  "Python 3 - Números: Operadores, métodos e funções que os envolvem" 
---


Os operadores básicos do Python são:

| sinal | função                |
|:--:|:------------------------ |
| +  | adição                   |
| -  | subtração                |
| *  | multiplicação            |
| /  | divisão                  |
| ** | exponenciação            |
| // | divisão inteira          |
| %  | resto da divisão inteira |

Obs.: a norma PEP-8 recomenda a utilização de espaços entre os operadores e os operandos para uma maior legibilidade.

Exemplos e explicações:

{% highlight python3 %}
>>> 1 + 1  # soma
2

>>> 1 - 2  # subtração
-1

>>> 3 * 3  # multiplicação
9

>>> 3 / 4  # divisão
0.75

>>> 2 ** 2  # exponenciação
4

>>> 2 ** (1/2)      # raiz --> exponenciação de fração:
1.4142135623730951  # raiz de xº grau de um número n = n ** (1/x)

>>> 5 // 2  # divizão inteira --> aquela divisão moleque, aquela divisão raiz,
2           # aquela divisão da alfabetização. A que sobra resto e você para aí.

>>> 5 % 2   # o resto de uma divisão inteira
1           # 5/2 = 2; 5 = 2 * 2 (+ 1 de resto)
{% endhighlight %}


