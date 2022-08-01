class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate


class Rectangle:
    def __init__(self, starting_point, width, height):
        self.starting_point = starting_point
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def end_points(self):
        top_right = self.starting_point.x_coordinate + self.width
        bottom_left = self.starting_point.y_coordinate + self.height
        print('Starting Point (X)): ' + str(self.starting_point.x_coordinate))
        print('Starting Point (Y)): ' + str(self.starting_point.y_coordinate))
        print('End Point X-Axis (Top Right): ' + str(top_right))
        print('End Point Y-Axis (Bottom Left): ' + str(bottom_left))


def build_rectangle():
    main_point = Point(50, 100)
    rect = Rectangle(main_point, 90, 10)

    return rect


my_rect = build_rectangle()

print(my_rect.area())
my_rect.end_points()
