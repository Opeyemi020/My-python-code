egg_per_box = 6
total_eggs = 28
number_of_box = total_eggs // egg_per_box
last_uncompleted_box = total_eggs % egg_per_box
additional_eggs_needed_to_fill_the_last_box = total_eggs - egg_per_box
print("Number of box needed:", number_of_box)
print("Egg placed in the last uncompleted box:", last_uncompleted_box)
print("additional_eggs_needed_to_fill_the_last_box:", additional_eggs_needed_to_fill_the_last_box)
