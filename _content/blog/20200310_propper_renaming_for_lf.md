---
title: Proper renaming for LF
date: 20200310
draft: false
---

I've definitely changed to *LF* file manager, but I still wanted the renaming power I've had in other TUI file managers, like *ranger* and *VIFM*'s "I", "A" and "a" mappings, or their "bulk-rename" function. So today I'm going to show you how to get those functionalities in *LF*.


## rename

I've written this on my lfrc (inside `$HOME/.config/lf/`):

```lf
cmd rename %{{
  base="$(dirname "$f")"
  srcfn=$(basename -- "$f")
  srcext="${srcfn##*.}"
  srcfn="$(basename "$f" ".$srcext")"
  srcdot="" && [ ! -z $srcext ] && srcdot="."

  filename_only="" ; extension_only=""
  case $1 in
    -n)
      filename_only=true && shift
      dst="$base/$@$srcdot$srcext" ;;
    -e)
      extension_only=true && shift
      dst="$base/$srcfn$srcdot$@" ;;
    *) dst="$base/$@" ;;
  esac

  please=''
  for path in $f $dst
  do
    [ ! -w $(dirname "$path") ] && please='sudo' && break
  done
  [ $# -eq 0 ] && echo "Destination not given." && exit 1
  [ -e "$dst" ] && printf "  Not renamed: "$dst" exists." || $please mv "$f" "$dst"
}}
```

It is a rename function for the current file your cursor points to. Inside *LF*, type the following while pointing to "somefile.png":
```vim
:rename someanotherfile.png
```
Now "somefile.png" is called someanotherfile.png"

With *-n* option for rename, as in `:rename -n newname`, it just renames the filename, without extension. In the other hand, with the *-e* option, as in `:rename -e jpg`, it just changes the file extension to "jpg". Anyway, options are really just fancy stuff. Look at how we are going to use this function in our mappings:

```vim
# unmap c (default to "clear" selection)
map c
map cW &lf -remote "send $id push :rename<space>"
```

What this line does is, whenever *cW* is pressed from *LF*, user is prompted with our rename function. This approach is certainly useful, but it turns out that *LF* freezes a little when ":" is pushed, as it is leaving normal mode and entering command mode. For it being frozen, sometimes the next character after ":" is not typed and we end up with `:ename -n ` afterr pressing "cW" at a file... So, to avoid it, we can send two push commands to lf:
  1. one for sending just ":";
  2. another one for sending the rest of the text.

Our final polished mappings become:
```vim
# unmap c (default to "clear" selection)
map c
map cW &lf -remote "send $id push :" && lf -remote "send $id push $(echo "rename " | sed 's/\s/<space>/g')"
map C  &lf -remote "send $id push :" && lf -remote "send $id push $(echo "rename " | sed 's/\s/<space>/g')"
map A  &lf -remote "send $id push :" && lf -remote "send $id push $(echo "rename $(basename $f)" | sed 's/\s/<space>/g')"
map I  &lf -remote "send $id push :" && lf -remote "send $id push $(echo "rename $(basename $f)" | sed 's/\s/<space>/g')" && lf -remote "send $id push $(echo "<home>lllllll" | sed 's/l/<right>/g')"
map a  &lf -remote "send $id push :" && fn=$(basename $f) && ext="${fn##*.}" && go_back=0 && [ $(echo $fn | grep "\." 2>/dev/null) ] && go_back=$(echo "$ext" | wc -c); fn=$(printf "$fn" && awk 'BEGIN{for(c=0;c<'$go_back';c++) printf "<left>"}') && lf -remote "send $id push $(echo "rename $fn" | sed 's/\s/<space>/g')"
map cw &lf -remote "send $id push :" && fn=$(basename $f) && ext="${fn##*.}" && go_back=0 && [ $(echo $fn | grep "\." 2>/dev/null) ] && go_back=$(echo "$ext" | wc -c) && fn="" && ext=".$ext" || ext=""; fn=$(printf "$ext" && awk 'BEGIN{for(c=0;c<'$go_back';c++) printf "<left>"}') && lf -remote "send $id push $(echo "rename $fn" | sed 's/\s/<space>/g')"
```

Now:
  - *A*: prompts filename and puts cursor at the end of it;
  - *I*: prompts filename and puts cursor at it's begining
  - *a*: prompts filename and puts cursor right before the first "." (before extension);
  - *cw*: prompts filename after extension, puts cursor before it;
  - *cW* and *C*: nothing is prompted as default for new filename;


## bulk-rename

bulk-rename here reads to "rename various files in a text editor".

My code for this functionality is inpired @blairdrummond's response at [github/gokcehan/lf/issues/149](https://github.com/gokcehan/lf/issues/149). It has grown a bit, so I'll tell you why you should use it first:

  1. You can rename various files in the program you've set for $EDITOR;
  2. Have you ever wanted to rename both a movie and its subtitle to the same name but not to bother with their extensions in the process? Here you can bulk-rename without extension (and the task easily becomes as simple as "yypGddZZ" at VIM screen). This is done by using *-n* option.
  3. Have you ever wanted to transform that bunch of free note text files into *.md*'s? You can rename just extensions! The option for this is *-e*.
  4. You can also rename including all filepath (using option *-A*);

Running `:bulk-rename` function in *LF* will take items in selection and show their names for edition in your text editor. If there are no items selected, all the current directory files are to be renamed, instead.

Everything you need to do is sign a pact by adding this to your *lfrc*:

```lf
cmd bulk-rename ${{
  case $1 in
    # do not query extensions for renaming
    -n) mode="no-exts" ;;
    # only rename extensions
    -e) mode="only-exts" ;;
    # rename entire filepaths
    -A) mode="all-path" ;;
    # else, just rename filenames
  esac
  # make tmp files
  oldnames=$(mktemp /tmp/lf-bulk-oldnames.XXXXXXXXXX)
  newnames=$(mktemp /tmp/lf-bulk-newnames.XXXXXXXXXX)
  if [ "$mode" != "all-path" ]
  then
    dirnames=$(mktemp /tmp/lf-bulk-dirnames.XXXXXXXXXX)
    aux=$(mktemp /tmp/lf-bulk-aux.XXXXXXXXXX)
  fi
  # query selected files or all files in directory
  if [ -n "$fs" ]
  then
    index="$fs"
  else
    index="$(ls $(dirname "$f"))"
  fi
  # separate and save useful variables in files
  for path in $index
  do
    dir="$(dirname "$path")"
    fullfilename=$(basename -- "$path")
    filename="${fullfilename%.*}"  # must be here
    ext="" && [ $(echo $fullfilename | grep "\." 2>/dev/null) ] && ext="${fullfilename##*.}"

    case "$mode" in
      "all-path") echo "$(realpath "$path")" >> $oldnames ;;
      "no-exts")
        echo "$filename" >> $oldnames
        [ "$ext" != "" ] && ext=".$ext"
        echo "$ext" >> $aux
        ;;
      "only-exts")
        echo "$ext" >> $oldnames
        echo $filename >> $aux
        ;;
      "") echo "$fullfilename" >> $oldnames ;;
    esac
    [ "$mode" != "all-path" ] && echo "$dir" >> $dirnames
  done
  cp $oldnames $newnames
  # interact with user
  $EDITOR $newnames
  # run mv on each path if they were modified
  n=$(cat $oldnames | wc -l)
  if [ $(cat $newnames | wc -l) -eq $n ]
  then
    counter=1
    while [ $counter -le $((n+1)) ]
    do
      case $mode in
        "no-exts")
          dir="$(cat $dirnames | sed "${counter}q;d")"
          old="$(cat $oldnames | sed "${counter}q;d")"
          new="$(cat $newnames | sed "${counter}q;d")"
          ext="$(cat $aux      | sed "${counter}q;d")"
          old="$dir/$old$ext" ; new="$dir/$new$ext"
        ;;
        "all-path")
          old="$(cat $oldnames | sed "${counter}q;d")"
          new="$(cat $newnames | sed "${counter}q;d")"
        ;;
        "only-exts")
          old="$(cat $oldnames | sed "${counter}q;d")"
          new="$(cat $newnames | sed "${counter}q;d")"
          filename="$(cat $aux | sed "${counter}q;d")"
          echo $old $new
          [ "$old" != "" ] && old=".$old"
          [ "$new" != "" ] && new=".$new"
          old="$dir/$filename$old"
          new="$dir/$filename$new"
        ;;
        *)
          dir="$(cat $dirnames | sed "${counter}q;d")"
          old="$(cat $oldnames | sed "${counter}q;d")"
          new="$(cat $newnames | sed "${counter}q;d")"
          old="$dir/$old" ; new="$dir/$new"
        ;;
      esac
      counter=$(($counter+1))
      [ "$old" = "$new" ] && continue
      [ -e "$new" ] && echo "File exists: $b" && continue
      # check write permission
      please=''
      for path in $old $new
      do
        [ ! -w $(dirname "$path") ] && please='sudo' && break
      done
      $please mv "$old" "$new"
    done
  else
    echo "Number of filenames differ."
  fi

  # removing tmp files
  rm $oldnames $newnames
  if [ "$mode" != "all-path" ]
  then
    rm $dirnames
    rm $aux
  fi
}}
```

I hope you enjoy my codes!
