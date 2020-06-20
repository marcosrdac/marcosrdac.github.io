---
title: TUI file managers battle
subtitle: Comparing `ranger`, `Vifm` and `LF`
date: 20200228
draft: false
---

# 

Since two years ago, I've tried some terminal file managers and ended up finding three of my taste.

The first one was `ranger`. It conquered me for being controled in a vim-like style, having a vim-like config file, having 3 panes (the first showing the parent directory files, the middle one, the files at your directory, and the third, a preview of the selected folder/file), being able to show me pitures directly on the terminal via `w3m` (although it was not very stable), and also been written in *Python*, which was my first programming language! Then I perceived it was really a good piece of software, but this last "advatage" turned out to be a disgustful characteristic: anything written in *Python* is inherently slower than it might be. And `ranger` is really slow, sometimes as slow as a gui file browser.

So I tried `Vifm` and loved it: it is written in *C*, that is a language that not only I comprehend, as it is usually refference in velocity marks. And `Vifm` is *de facto* way faster than `ranger`. I could also preview images here, both using w3m or, better, using `ueberzug`, that is much better (gets me no fickering or instabilities). Another thing I liked about `Vifm` was that its config files were even closer to `vim`'s than `ranger`'s were.

Well, the only thing that annoyed me was its panes. You always open to directories at once and looks at them both in panes. It makes te screen a mess by default. You could hide the seccond, but, if you wanted to preview a file with a pager or anything, you would have to reopen it and transform that seccond pane into a preview pane. I didn't like it at all.

So some time ago I've discovered `LF`. `LF` is basically `ranger`, but almost as fast as `Vifm`, as it is well written in *Go*. It has some advantages, though: you can create functions inside the config file, and you write it in *shell script*, not in *Python* (it has never made sense). Also, the overall advage is: it launches a daemon at the first time you launch the program. And what it means? It means you can copy a file at one instance of `LF`, open another one in another terminal or multiplexer section, and then paste the file there! It is just amazing, something I missed in my previous TUI file managers. The only current disavantage is: image previwing is still not easily solved. I'm trying to make it work, though!

So I'll make them three be evaluated in a table:

| Atribute \ File manager | ranger | vifm | **lf** |
|-|:-:|:-:|:-:|
| Velocity | 3 | **10** | 9 |
| Ease viewing of files | **10** | 3 | **10** |
| Integrated multple instances | 0 | 0 | **10** |
| Improvability | 4 | 8 | **10** |
| Vim-like | 8 | **9** | **9** |
| Image previews | 5 | **8** | 0 |
| **Rounded Normalized total** | 6 | 7 | **9** |

Then I conclude with my criteria that `LF` is the most switable TUI file manager for users like me. It is a very extensible tool and I recommend you to check my *lfrc* --- the LF configuration file --- settings in [my dotfiles at GitHub](https://github.com/marcosrdac/dotfiles/blob/dotfiles_bspwm/.config/lf/lfrc).

For Arch users: both `ranger` and `vifm` are in Arch's official repositories. You can install `LF` from AUR.
