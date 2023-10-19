from visualizer import Visualizer
from sorting_algorithms import radixSort, bubble_sort, selection_sort, insertion_sort, generate_data, quick_sort, mergeSort, merge, augussySort, stalin_sort
from values import n
import random

visualizer = Visualizer("Visualisering af sorterings algoritmer")

visualizer.bar_animation(radixSort, generate_data(n, type="bar"))
visualizer.await_keypress('c')

visualizer.bar_animation(mergeSort, generate_data(n, type="bar"))
visualizer.await_keypress('c')
#visualizer.bar_animation(augussySort, generate_data(n))
#visualizer.await_keypress('c')
#visualizer.bar_animation(bubble_sort, generate_data(n, type="bar"))
#visualizer.await_keypress('c')
visualizer.bar_animation(selection_sort, generate_data(size=n, type="bar"))
visualizer.await_keypress('c')
visualizer.bar_animation(insertion_sort, generate_data(size=n, type="bar"))
visualizer.await_keypress('c')

#visualizer.bar_animation(stalin_sort, generate_data(size=n, type="bar"))
#visualizer.await_keypress('c')
#visualizer.bar_animation(selection_sort, generate_data(n, type="bar"))

#box animations
visualizer.box_animation(stalin_sort, generate_data(size=10, type="box"))
visualizer.await_keypress('c')
visualizer.box_animation(bubble_sort, generate_data(size=10, type="box"))
visualizer.await_keypress('c')
visualizer.box_animation(selection_sort, generate_data(size=10, type="box"))
visualizer.await_keypress('c')
visualizer.box_animation(insertion_sort, generate_data(size=10, type="box"))
visualizer.await_keypress('c')