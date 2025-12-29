win = [[-1,1], [0, 1]]
line1 = [ 1, 1, -1.5]
line2 = [ 0.1, 1, -0.7 ]
ray = [[-0.5, 0.3], pi/4]
ray2 = [[-1.8, 2.1], -pi/4]
draw_line_in_window(line1, win, 'red')
draw_line_in_window(line2, win, 'grey')
draw_ray_in_window(ray, win, 'blue')
draw_ray_in_window(ray2, win, 'pink')
plt.show()
