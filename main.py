# August Leander Hedman
# augu1789@edu.nextkbh.dk
# NEXT Sukkertoppen, S3n    

# Controller-delen af MVC.

# Importer relevante biblioteker og funtkoner etc. fra andre filer i programmet
from visualizer import Visualizer
from sorting_algorithms import radix_sort, bubble_sort, selection_sort, insertion_sort, generate_data, stalin_sort, merge_sort
from values import n

# Tildeler visualizer en instans af klassen Visualizer med titlen "Visualisering af sorterings algoritmer"
visualizer = Visualizer("Visualisering af sorterings algoritmer")

# Controlleren (main.py) fortæller visualizeren, hvilken modellen (funktioner), der skal visualiseres samt hvilket data, der skal bruges 
# og hvilken type visualisering, der skal bruges
visualizer.bar_animation(bubble_sort, generate_data(50, type="bar"))
visualizer.await_keypress('c')
visualizer.boxSort(bubble_sort, generate_data(10, type="box"))
visualizer.await_keypress('c')

visualizer.bar_animation(radix_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')

visualizer.bar_animation(stalin_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')
visualizer.boxSort(stalin_sort, generate_data(10, type="box"))
visualizer.await_keypress('c')

visualizer.bar_animation(merge_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')

visualizer.bar_animation(selection_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')
visualizer.boxSort(selection_sort, generate_data(10, type="box"))
visualizer.await_keypress('c')

visualizer.bar_animation(insertion_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')



