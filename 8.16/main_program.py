import my_module
my_module.favorite_book('Alice in wonderland')

from my_module import favorite_book
favorite_book('Alice in wonderland')

from my_module import favorite_book as dm
dm('Alice in wonderland')

import my_module as mm
mm.favorite_book('Alice in wonderland')

from my_module import *
favorite_book('Alice in wonderland')