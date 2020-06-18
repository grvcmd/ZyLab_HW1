# Prompt user to input wall's height and width
wall_height = int(input('Enter wall height (feet):' + '\n'))
wall_width = int(input('Enter wall width (feet):' + '\n'))
# calculate and output wall's area
wall_area = wall_height * wall_width
print('Wall area:', int(wall_area), 'square feet')

# calculate and output amt. of paint in gallons needed (floating point)
gallon_paint = 350
paint_needed = wall_area/gallon_paint
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')

# calculate and output number of 1 gallon cans needed to paint the wall
cans_needed = round(paint_needed)
print('Cans needed:', cans_needed, 'can(s)')

# prompt user for a color
colors = {'red': 35, 'blue': 25, 'green': 23}
choose_color = input('\n' + 'Choose a color to paint the wall:' + '\n')
if choose_color in colors:
    print('Cost of purchasing', choose_color, 'paint:', '$' + str(colors[choose_color]*cans_needed))
else:
    print('You can only choose red, blue, or green')


