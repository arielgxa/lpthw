# LPtHW Appendix A: Command Line Crash Course

## Exercise 1: The Setup

1. Use Powershell!
1. Never type `rm -rf /` (This can destroy your computer)
1. Get help from people you trust, not random idiots on the internet

#### Commands to memorize
* [ ] Memorized

| command         | action                                 |
|-----------------|----------------------------------------|
| `pwd`           | print working directory                |
| `hostname`      | my computer's network name             |
| `mkdir`         | make directory                         |
| `cd`            | change directory                       |
| `ls`            | list directory                         |
| `rmdir`         | remove directory                       |
| `pushd`         | push directory                         |
| `popd`          | pop directory                          |
| `cp`            | copy a file or directory               |
| `robocopy`      | robust copy                            |
| `mv`            | move a file or directory               |
| `more`          | page through a file                    |
| `type`          | print the whole file                   |
| `forfiles`      | run a command on lots of files         |
| `dir -r`        | find files                             |
| `select-string` | find things inside files               |
| `help`          | read a manual page                     |
| `helpctr`       | find what man page is appropriate      |
| `echo`          | print some arguments                   |
| `set`           | export/set a new environment variable  |
| `exit`          | exit the shell                         |
| `runas`         | DANGER! become super user root DANGER! |

## Exercise 2: Paths, Folders, Directories (pwd)

Directories are the same thing as folders!  
* Path: C:\Users\Ariel

## Exercise 3: If You Get Lost

If you get lost at any time, type:

```
pwd
cd ~
```

First command `pwd` tells you where you are, second command `cd ~` takes you home so you can try again

## Exercise 4: Make a Directory (mkdir)

1. Always go home before completing an exercise
1. When making directories in Windows, you can use both slashes and backslashes (e.g. `mkdir temp/stuff/hello` / `mkdir temp\stuff\hello`)
  * I will use backslashes from now on
1. Put directory names with spaces in quotes (e.g. `mkdir temp\"I Have Fun"`)

## Exercise 5: Change Directory (cd)

* `cd ..` moves you "up" in the tree and path
  * `cd ..\..` to move up two nodes at once (or any other number)
