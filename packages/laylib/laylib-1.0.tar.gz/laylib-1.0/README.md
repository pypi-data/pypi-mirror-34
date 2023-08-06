# laylib package for pygame 

This package is made to fast prototype your multimedia applications like games on pygame. 
Write clean and pragmatic design. It lets you focus on the game engine itself, so you dont have
to take care about several details like setting up the window, loading and cheking data (images,
sound, font, fx, music, resources names...).
All you need to do is to put your resources into a specific data folder and use them 
in your game class 'MyEngine()'. 

You don't need to reinvent the wheel, some repetitive parts of code (main loop, getting the delta time, 
closing the window, drawing text...) are already described and ready to use in the 
default engine.

     1)- Environment class:
         This is the first class to call on your main file, to set the
         pygame environement.
         By default the pygame display,the mixer and the font are initialized.

     2)- load_complete(self, instance, dataFolder=None, fileLevels=None):
         This is the second method to call on your main file
         to load your resources if any.(see load_complete for parameters
         description).

     # Note that this is important to respect the following scheme
     for all types of game:
         1- Set the environement
         2- load all resources only once.
         3- main loop function called by an instance of your game engine.
         4- at the end of the game destroy resources and quit the environement.
         Your main file should always look like the following example:
     
Usage example:

```python
>>> from laylib import Environment
>>> from engine import Engine
>>>
>>> def main():
>>> 	demo = Environment(800, 600, False, 'My game')
>>> 	demo.load_complete(Engine(), 'data', 'resources.res')
>>> 	demo.gInstance.main_loop()
>>> 	demo.destroy()

>>> if __name__ == "__main__":
>>>     main()
```
	
### INSTALLATION

First, install the dependencies:
- Python3 (3.1 or later) <http://www.python.org>
- Pygame 1.9.1 or later <http://pygame.org/download.shtml>

Then install laylib: 

```os
  pip install laylib
```
Or alternatively, you can just copy the "laylib" folder into the same
directory as the Python program that uses it.

### USAGE

For usage see examples provided with laylib. 
For more details, all other parts of documentation are described in the source file.

### TODO

 - [ ] add unittest module.
 - [ ] more automation for resources management
 - [ ] improve util.py module
 - [x] add more examples for demo