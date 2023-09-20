from visualizer import Visualizer
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, generate_data, quick_sort, mergeSort, merge, augussySort
from values import n

visualizer = Visualizer("Visualisering af sorterings algoritmer")
#visualizer.bar_animation(mergeSort, generate_data(n))
#visualizer.await_keypress('c')
#visualizer.bar_animation(augussySort, generate_data(n))
#visualizer.await_keypress('c')
visualizer.bar_animation(bubble_sort, generate_data(n))
visualizer.await_keypress('c')
visualizer.bar_animation(selection_sort, generate_data(n))
visualizer.await_keypress('c')
visualizer.bar_animation(insertion_sort, generate_data(n))
visualizer.await_closure()