darwin
======

Creature evolution through natural selection.


## Introduction

`darwin` is an evolution simulation that uses natural selection to evolve creatures over many generations.  Each creature is an NxN pixel image with NxN RGB values.  The "environment" dictates how fit each creature is during the death phase of the generation.  The closer the image pixels are to the "ideal image" or "ideal color", the better chance it will have to outsurvive its peers.  A number of creatures are set to die each generation.  After this, the population gap is filled by randomly selecting surviving creatures, and having them reproduce asexually by replication and mutation.  Mutation is in the form of a small fraction of pixels being changed to a random RGB color.  This proceess continues generation after generation with the most fit creatures (most similiar to target color) successfully breeding the next generation of creatures.

Examples are included in the "examples" directory.

##Purple color example
Here, the more the creatures blend in with the enviornment, the more likely they will outlive their peers and replicate.  A population size of 400 (8x8 pixel) creatures are evolved for over 21,800 generations with the following results:
![purple gen 0](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/purple_run/0.png)
![purple gen 485](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/purple_run/485.png)
![purple gen 2955](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/purple_run/2955.png)
![purple gen 21840](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/purple_run/21840.png)


##Eye example
Here, the more the creatures look like an eye, the more likely they will outlive their peers and replicate.  A population of 64 (16x16 pixel) creatures are evolved for over 27,000 generations with the following results:
![eye gen 0](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/eye_run/0.png)
![eye gen 650](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/eye_run/650.png)
![eye gen 4500](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/eye_run/4500.png)
![eye gen 27120](https://raw.githubusercontent.com/tomhettinger/darwin/master/examples/eye_run/27120.png)
