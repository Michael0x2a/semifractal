# semifractal #

This program is designed to generate fractals based on elementary cellular
automata. It's currently just a short app, which I made because I was
bored. I might go ahead and polish it up later.

## Implementation details ##

I basically wrote a program that generates a set of 
[1-d](http://en.wikipedia.org/wiki/Elementary_cellular_automaton) 
[cellular automaton](http://mathworld.wolfram.com/ElementaryCellularAutomaton.html). 
Basically, it generates this (rule 150):

![simple triangle][1]

...and rotates it to form this:

![simple square][2]

I then introduced an element of randomness to it, so it could form images like this:

![complex square][3]

## Usage ##

Click the program to generate a new image. It will print out a number to the 
console -- that's the seed for the image, so that you can regenerate the 
image later (support for this is built into the code, but I haven't got around
to creating a usable front-end for it yet).

Press any keyboard key to save the image as a png file. The filename is 
the seed for the image.

## Modification ##

Currently, the code is set to produce squares with 511x511 cells, and with
cells being 1 pixel wide. You can examine the code to change these
constants.


  [1]: http://i.stack.imgur.com/WJie4.png
  [2]: http://i.stack.imgur.com/UX71V.png
  [3]: http://i.stack.imgur.com/fN9rA.png
