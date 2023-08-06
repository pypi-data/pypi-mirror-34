# Stain 

Stain helps you color your terminal output without having to worry about formatting classes,
replacement print functions, or using anything more than familiar string manipulations. 

## Getting Started

Using the basics of stain is fast and easy. 

Stain provides a context manager that handles pre and post-printing of formatting
characters. 

Ex:
```PYTHON
from stain import Stain

stain = Stain()

with stain.red(): # the context manager __enter__ prints \033[31m
    print("This line is red.")
    print("So is this one.")
# the context manager __exit__ prints \033[0m

print("But this one is not.")
```

For more complex coloring, stain also provides formatting constants.

```PYTHON
from stain import Stain

stain = Stain()

print("Hello " + stain.BLACK + " darkness " + stain.RESET + "my old friend.")
```


Both forms of stain can take stacked attributes in any order:

```PYTHON
stain.BLACK_ON_RED
```
or
```PYTHON
with stain.bold_green():
```
or even
```PYTHON
stain.BOLD_RED_ON_BLACK_UNDERLINE
```

### Terminal Detection
Stain is TTY-aware, meaning it will not print coloring characters when your output
has been redirected to files, pagers, etc. 


### Supported Formatting

Stain supports 16-Color ANSI foreground and background colors, and the common formatters.

Whether or not a given terminal supports them is another matter. 

COLORS:
* Black
* Red
* Green
* Yellow
* Blue
* Magenta
* Cyan
* Light gray
* Dark gray
* Light red
* Light green
* Light yellow
* Light magenta
* Light cyan
* White

FORMATS:
* Bold
* Reset Bold
* Dim
* Reset Dim
* Underline
* Reset Underline
* Blink
* Reset Blink
* Reverse
* Reset Reverse
* Hidden
* Reset Hidden
* Reset All

#### Caveat Regarding Background Coloring

By default, background coloring is disabled in the context manager form of stain.
This is due to how background color determination works when scrolling a terminal.

When printing a newline at the bottom of the screen such that everything needs to shift
upward, the background color will bleed onto the next line. The context manager cannot
print the reset before print statements in the block print their newlines, so ugly background
color bleeding will occur. 

This is also true of the Reverse formatter.

To enable background colors with the context manager, do the following:
```PYTHON
from stain import Stain

stain = Stain(unsafe=True)

with stain.black_on_light_gray():
    print("This will have a background color" + stain.RESET)
```

You will need to hand-reset at the end of each line to prevent scrolling background bleed.


### Prerequisites

 None

### Installing

pip install stain

## Running the tests

make tests

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
