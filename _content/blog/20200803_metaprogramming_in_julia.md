---
date: 20200803
title: Making various functions in one only block of code
subtitle: a little of metaprogramming in julia
---

Have you ever needed to create numerous very similar functions? Today I'm showing you how to do that thing you always wanted to do in pure julia: create various functions in a loop.

<p>Supose you want to create three functions in julia: \(f(x)=x\), \(g(x)=x^2\) and \(h(x)=x^3\). So you could workfully write:</p>

```julia
function f(x)
  return x
end

function g(x)
  return x^2
end

function h(x)
  return x^3
end
```

But I know, when you are about to write "function" for the second time, your thoughts sudenly start to bother you: "man, there must be a way for me to do it efficiently...". I'm glad to tell you that **you would be right!** Lets expand our objectives for 6 functions and do it without all this machine work!

```julia
for func in (:f, :g, :h, :i, :j, :k)

  if     func == :f  E = 1
  elseif func == :g  E = 2
  elseif func == :h  E = 3
  elseif func == :i  E = 4
  elseif func == :j  E = 5
  elseif func == :k  E = 6
  end

  quote
    function $func(x)
      return x^$E
    end
  end |> eval

end
```

<p>And you can then start using \(k(x)\) to get \(x^6\).</p>


# The downside

Although you might think that our last code would then be slower at runtime, after all it's all super high level code, it will not. These definitions are run at parse time, before actual compilation. So, roughly speaking, the only downside is that compiling your code is going to take more time.


# For those who want to understand what's going on...

  - we enter a loop block at line 1. One iteration is done for each of the symbols f, g, h, i, j, k. At each iteration, func is assigned to one of them.
  - then we enter the `if elseif` block. Depending on the symbol we are working on, we define a constant value E, the exponent used in the function.
  - the next block `quote`s the code that we actually want to run: the function definition. We make use of the symbols previously defined by interpolating their values. For that we make use of the \$ operator.
  - the end: all inside this quotation returns a block object and, by itself, does nothing. It only becomes code when put this result inside the `eval` function. I could indeed be done like this:

```julia
  eval(
    quote
      function $func(x)
        return x^$E
      end
    end
  )
```

  but I think it's prettier to pipe the quotation end to the eval function with `|> eval`.
