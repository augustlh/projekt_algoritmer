from visualizer import Visualizer
from sorting_algorithms import radix_sort, bubble_sort, selection_sort, insertion_sort, generate_data, mergeSort, stalin_sort
from values import n

visualizer = Visualizer("Visualisering af sorterings algoritmer")

#visualizer.bar_animation(insertion_sort, generate_data(100, type="bar"))
#visualizer.await_keypress('c')
visualizer.boxSort(insertion_sort, generate_data(10, type="box"))
visualizer.await_keypress('c')

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

visualizer.bar_animation(mergeSort, generate_data(n, type="bar"))
visualizer.await_keypress('c')

visualizer.bar_animation(selection_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')
visualizer.boxSort(selection_sort, generate_data(10, type="box"))
visualizer.await_keypress('c')

visualizer.bar_animation(insertion_sort, generate_data(n, type="bar"))
visualizer.await_keypress('c')



