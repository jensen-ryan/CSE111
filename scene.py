#Author: Ryan Jensen
#Class: CSE 111
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

def main():
    scene_width = 800
    scene_height = 500

    #Call the start_drawing function in the draw2d.py
    #library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    #Call the draw_sky and draw_ground functions in this file.
    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)

    #Call the draw_clouds functions in this file.
    draw_clouds(canvas, 100, 250, 100, 200)
    draw_clouds1(canvas, 75, 600, 400, 350)
    draw_clouds2(canvas, 150, 500, 200, 400)

    #Call the draw_house and its body functions in this file.
    draw_house(canvas, 550, 50, 250)
    draw_door(canvas, 620, 50, 250)
    draw_window_1(canvas, 500, 60, 200)
    draw_window_2(canvas, 550, 60, 200)

    #Call the function draw_sun
    draw_sun(canvas, 200, 200, 650, 350)

    #Call the finish_drawing function in the draw2d.py library.
    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 7,
        scene_width, scene_height, width=0, fill="dodgerBlue3")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 7, width=0, fill="green3")

    #Draw a pine tree.
    tree_center_x = 700
    tree_bottom = 20
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #Draw a pine tree.
    tree_center_x = 300
    tree_bottom = 25
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x, tree_bottom, tree_height)

    #Draw a pine tree.
    tree_center_x = 200
    tree_bottom = 60
    tree_height = 150
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)
    
    #Draw a pine tree.
    tree_center_x = 60
    tree_bottom = 35
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,tree_bottom, tree_height)

def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 15
    trunk_height = height / 10
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    #Draw the trunk of the pine tree.
    draw_rectangle(canvas, trunk_left, trunk_top, trunk_right, bottom, outline="black", width=1, fill="sienna4")
    crown_width = height / 2
    crown_height = height - trunk_height
    crown_left = center_x - crown_width / 2
    crown_right = center_x + crown_width / 2
    crown_top = bottom + height

    #Draw the crown of the pine tree.
    draw_polygon(canvas, center_x, crown_top, crown_right, trunk_top, crown_left, trunk_top, outline="black", width=1, fill="forest green")

def draw_clouds(canvas, cloud_height, cloud_width, reference_x, reference_y):
    x_zero = reference_x
    y_zero = reference_y
    x_two = reference_x + cloud_width/2
    y_two = reference_y + cloud_height/2
    draw_oval(canvas, x_zero, y_zero, x_two, y_two, width=0, outline="black", fill="snow1")
    x_zero2 = reference_x + cloud_width/5
    y_zero2 = reference_y + (2 * cloud_height)/5
    x_two2 = reference_x + cloud_width
    y_two2 = reference_y + cloud_height
    draw_oval(canvas, x_zero2, y_zero2, x_two2, y_two2, width=0, outline="black", fill="snow1")

def draw_clouds1(canvas, cloud_height, cloud_width, reference_x, reference_y):
    x_zero = reference_x
    y_zero = reference_y
    x_two = reference_x + cloud_width/2
    y_two = reference_y + cloud_height/2
    draw_oval(canvas, x_zero, y_zero, x_two, y_two, width=0, outline="black", fill="snow1")
    x_zero2 = reference_x + cloud_width/5
    y_zero2 = reference_y + (2 * cloud_height)/5
    x_two2 = reference_x + cloud_width
    y_two2 = reference_y + cloud_height
    draw_oval(canvas, x_zero2, y_zero2, x_two2, y_two2, width=0, outline="black", fill="snow1")

def draw_clouds2(canvas, cloud_height, cloud_width, reference_x, reference_y):
    x_zero = reference_x
    y_zero = reference_y
    x_two = reference_x + cloud_width/3
    y_two = reference_y + cloud_height/4
    draw_oval(canvas, x_zero, y_zero, x_two, y_two, width=0, outline="black", fill="snow1")
    x_zero2 = reference_x + cloud_width/5
    y_zero2 = reference_y + (2 * cloud_height)/5
    x_two2 = reference_x + cloud_width
    y_two2 = reference_y + cloud_height
    draw_oval(canvas, x_zero2, y_zero2, x_two2, y_two2, width=0, outline="black", fill="snow1")

def draw_house(canvas, center_x, bottom, height):
    body_width = height / 2.5
    body_height = height / 3
    body_left = center_x - body_width
    body_bottom = bottom
    body_right = center_x + body_width / 1
    body_top = bottom + body_height
    draw_rectangle(canvas, body_right, body_bottom, body_left, body_top, fill="firebrick2")
    roof_width = height / 1
    roof_left = center_x - roof_width / 2
    roof_bottom = body_top
    roof_x = center_x
    roof_y = bottom + height
    roof_top = bottom + height
    roof_right = center_x + roof_width / 2
    draw_polygon(canvas, roof_right, roof_bottom, roof_x, roof_y, roof_left, roof_bottom, fill="antiqueWhite4")

def draw_door(canvas, center_x, bottom, height):
    doors_width = height / 8
    doors_height = height / 4
    doors_left = center_x - doors_width / 2
    doors_right = center_x + doors_width / 2
    doors_top = bottom + doors_height
    draw_rectangle(canvas, doors_left, doors_top, doors_right, bottom, outline="black", width=1, fill="antiqueWhite4")

def draw_window_1(canvas, center_x, bottom, height):
    window_width = height / 6
    window_height = height / 4
    window_left = center_x - window_width / 2
    window_right = center_x + window_width / 2
    window_top = bottom + window_height
    draw_rectangle(canvas, window_left, window_top, window_right, bottom, outline="black", width=1, fill="lightSkyBlue")

def draw_window_2(canvas, center_x, bottom, height):
    window1_width = height / 6
    window1_height = height / 4
    window1_left = center_x - window1_width / 2
    window1_right = center_x + window1_width / 2
    window1_top = bottom + window1_height
    draw_rectangle(canvas, window1_left, window1_top, window1_right, bottom, outline="black", width=1, fill="lightSkyBlue")

def draw_sun(canvas, sun_height, sun_width, reference_x, reference_y):
    x_zero = reference_x
    y_zero = reference_y
    x_two = reference_x + sun_width/1
    y_two = reference_y + sun_height/1
    draw_oval(canvas, x_zero, y_zero, x_two, y_two, width=0, outline="orange", fill="orange")

#Call the main function so that this program will start executing.
main()
