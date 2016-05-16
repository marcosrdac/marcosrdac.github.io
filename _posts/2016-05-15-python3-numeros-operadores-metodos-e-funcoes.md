---
layout: post
title:  "Python 3 - Números: Operadores, métodos e funções que os envolvem" 
---


Os operadores básicos do Python são:

Operador | Função
 :--- | :---
a + b | adição
a - b | subtração
a * b | multiplicação
a / b | divisão
a ** b | exponenciação
a // b | divisão inteira
a % b | resto da divisão inteira
divmod(a, b) | retorna (a // b, x % y)
abs(a) | módulo de *a*; é o mesmo operador usado para complexos (módulo)


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

>>> divmod(5,2)
(2, 1)
>>> div, resto = divmod(5,2)
>>> print(div)
2
>>> print(resto)
1

>>> abs(-2)        # módulo...   
2
>>> abs(-31.5)     # módulo...
31.5
>>> abs(-5+6j)      # módulo... Sim, é vetorial!
7.810249675906654

>>> 3+5j.conjugate()  # conjugado de 3+5j (3-5j)   
(3-5j)

{% endhighlight %}

