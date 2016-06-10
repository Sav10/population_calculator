# population_calculator

The goal is to calculate population size around a geographic point.

It is somehow forked from an original method from Anna (https://github.com/anouchk/PopCentrales). I used the same conversion method, but using pandas dataframe, which made it much easier to do.
* If you just want to convert a population, just use distances_geostat_convert notebook
* If you want to understand the method, you are welcome to use the distances_geostat_exploration notebook

It works with Python 3, there could be bugs with Python 2 (the .pkl format from distances_geostat_convert, could be tricky in Python 2)
