from visualizer import Visualizer
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, generate_data
from values import n

visualizer = Visualizer("Abe")

visualizer.bar_animation(insertion_sort, generate_data(n))
visualizer.bar_animation(selection_sort, generate_data(n))
visualizer.await_closure()

