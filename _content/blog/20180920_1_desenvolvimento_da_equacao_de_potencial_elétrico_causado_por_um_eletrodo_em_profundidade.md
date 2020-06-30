---
date: 20180920
title: Desenvolvimento da equação do potencial elétrico para um único eletrodo de corrente em subsuperfície homogênea e isotrópica
draft: false
---

<p>A equação laplaciana para o potencial é \(\vec{\nabla}^2 V = 0\). Além disso, \( V = V(r,\theta,\phi) = V(r) \), uma vez que o meio é homogêneo e isotrópico. Nestas condições, a equação laplaciana se escreve:</p>

<p>
\( {1 \over r^2} {\partial \over \partial r} \left( r^2 {\partial V \over \partial r} \right) +\)
\( {1 \over r^2 \sin \theta} {\partial \over \partial \theta}  \left( \sin \theta {\partial V\over \partial \theta} \right) +\)
\({1 \over r^2 \sin^2 \theta} {\partial^2 V \over \partial \phi^2} = 0\)
</p>

<p>
\( \longrightarrow {1 \over r^2} {\partial \over \partial r} \left( r^2 {\partial V \over \partial r} \right) = 0 \)
</p>

<p>
\( \longrightarrow \frac{\partial^2 V}{\partial r^2} + {2 \over r} {\partial V \over \partial r}= 0 \)
</p>

<p>
\( \longrightarrow {\partial V \over {\partial r}} = {C_1 \over {r^2}}, \qquad C_1 \in \Re \)
</p>

<p>
\[ \therefore V = -{C_1 \over {r}} + C_2, \qquad C_1, C_2 \in \Re \]
</p>

<p>
donde \(C_2\) pode ser arbitrariamente escolhido \(0\):
</p>

<p>
\[ \therefore V = -{C_1 \over {r}}, \qquad C_1 \in \Re \]
</p>
