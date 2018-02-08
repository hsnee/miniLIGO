# miniLIGO
Real time plotting for michelson interferometer signal

### Visualisation
This code was written to be run on a raspberry pi connected to a [tsl2591 lux sensor from adafruit](https://www.adafruit.com/product/1980) and has [this python libaray as a dependency](https://github.com/maxlklaxl/python-tsl2591) and plots inputted data (after rewriting `calibrate`). 

### Audio
Since gravitational waves (or the noise) is in the audible frequency range, it is intuitive to audiolise it. This part is still under development in the `audio` branch.

### Signal injection
The code also senses button presses from buttons connected to the raspberry-pi and injects a signal that looks like a black hole-black hole merger.

## Build18
This project was originally built for [CMU](www.cmu.edu)'s [ECE](ece.cmu.edu)'s [Build18](www.build18.org) [2018 edition](www.build18.org/garage/2018) and was supported with an $800 budget through Build18. 

