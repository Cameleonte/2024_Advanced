from collections import deque

some_string = deque(input().split())
main_colours = ['red', 'yellow', 'blue']
secondary_colours = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}
my_colours = []
my_secondary_colours = []


def check_colors(color, m_colors, s_colors):
    if color in m_colors:
        my_colours.append(color)
        if len(some_string) <= 1:
            some_string.pop()
        else:
            some_string.popleft()
            some_string.pop()
    elif color in s_colors.keys():
        my_secondary_colours.append(color)
        my_colours.append(color)
        if len(some_string) <= 1:
            some_string.pop()
        else:
            some_string.popleft()
            some_string.pop()
    else:
        return 1


while some_string:
    first_sub, second_sub = some_string[0], some_string[-1]
    if len(some_string) > 1:
        new_color = first_sub + second_sub
        color_new = second_sub + first_sub
    else:
        new_color = color_new = first_sub
    f1 = check_colors(new_color, main_colours, secondary_colours)
    if f1:
        f2 = check_colors(color_new, main_colours, secondary_colours)
        if f2:
            first_sub = first_sub[:-1]
            second_sub = second_sub[:-1]
            some_string = list(some_string)
            return_index = len(some_string) // 2
            some_string = some_string[:return_index] + [first_sub, second_sub] + some_string[return_index:]
            some_string = deque(some_string)
            some_string.popleft()
            some_string.pop()
            if '' in some_string:
                some_string.remove('')

if my_secondary_colours:
    for colour in my_secondary_colours:
        for compounding_colour in secondary_colours[colour]:
            if compounding_colour not in my_colours:
                my_colours.remove(colour)

if my_colours:
    print(my_colours)
