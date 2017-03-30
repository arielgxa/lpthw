# LPtHW Appendix A: Command Line Crash Course

## Exercise 1: The Setup

1. Use Powershell!
1. Never type `rm -rf /` (This can destroy your computer)
1. Get help from people you trust, not random idiots on the internet

#### <font color="red">Commands to memorize</font>
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

## Exercise 2: Paths, Folders, Directories (`pwd`)

Directories are the same thing as folders!  
* Path: C:\Users\Ariel

## Exercise 3: If You Get Lost

If you get lost at any time, type:

```
pwd
cd ~
```

First command `pwd` tells you where you are, second command `cd ~` takes you home so you can try again

## Exercise 4: Make a Directory (`mkdir`)

* Always go home before completing an exercise
* Syntax: `mkdir <dir>`
  * Makes a new directory within the current directory
* When making directories in Windows, you can use both slashes and backslashes (e.g. `mkdir temp/stuff/hello` / `mkdir temp\stuff\hello`)
  * I will use backslashes from now on
* Put directory names with spaces in quotes (e.g. `mkdir temp\"I Have Fun"`)

## Exercise 5: Change Directory (`cd`)

* Syntax:
  * `cd <dir>`
    * Changes to chosen directory (must be within the current directory)
  * `cd ..` moves you "up" in the tree and path
    * `cd ..\..` to move up two nodes at once (or any other number)

## Exercise 6: List Directory (`ls`)

* Syntax:
  * `ls`
    * Lists the contents of current directory
  * `ls <dir>`
    * Lists the contents of a directory within the current directory
* Won't list anything if directory is empty

#### <font color="red"> Question: What does `dir -R` do?</font>
* Preliminary answer: Seems to list out all directories within the current directory and their subfolders
* Later answer: Seems to list out all files within the current directory (and I mean ALL of them...)

## Exercise 7: Remove Directory (`rmdir`)

* Syntax: `rmdir <dir>`
  * Removes an empty directory
  * Must be in the directory right above it

## Exercise 8: Moving Around (`pushd`, `popd`)

* Syntax:
  * `pushd <dir>`
    * Save current location and go to a new one
  * `popd`
    * Return to the saved location

Works as a stack - `pushd` pushes a directory to the end of the stack, and `popd` pops the last directory in the stack

## Exercise 9: Making Empty Files (`New-Item`)

Makes a new empty file or directory)!
* New file syntax: `New-Item <filename.format> -type file`
* New directory syntax: `New-Item <dir> -type dir`

## Exercise 10: Copy a File (`cp`)

* Syntax:
  * `cp <filename.format> <newfilename.format>`
    * Makes a copy of file with a new name within the current directory
  * `cp <filename.format> <givendir>\<newfilename.format>`
    * Makes a copy of file with a new name in given directory (directory must exist; leave newfilename out to keep the same name)
  *  `cp -r <dir> <newdir>` / `cp -recurse <dir> <newdir>`
    * Makes a copy of a directory (including files) with a new name within the current directory
* You can make copies of things in your home directory like this: `cp <filename.format> ~\<newfilename.format>`

Putting a `\` at the end of a directory makes sure that the file you're giving it really is a directory, so if the directory doesn't exist it'll throw an error

#### <font color="red">Question: Are `-r` and `-recurse` the same thing?</font>
* Preliminary answer: It sure seems that way

## Exercise 11: Moving a File (`mv`)

* Move file syntax:
  * `mv <filename.format> <newfilename.format>`
    * Renames a file within the current directory
  * `mv <filename.format> <givendir>\<newfilename.format>`
    * Moves a file to given directory with a new name (directory must exist; leave newfilename out to keep the same name)
* Move directory syntax:
  * `mv <dir> <newdir>`
    * Renames a directory within the current directory
  * `mv <dir> <givendir>`
    * Moves a directory and its contents to given directory
