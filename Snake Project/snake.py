from turtle import Screen, Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_blocks = []
        self.starting()
        self.head = self.snake_blocks[0]

    def starting(self):
        for position in STARTING_POSITIONS:
            new_seg = Turtle("square")
            new_seg.color("white")
            new_seg.penup()
            new_seg.goto(position)
            self.snake_blocks.append(new_seg)

    def move(self):
        for seg_num in range(len(self.snake_blocks) - 1, 0, -1):
            new_x = self.snake_blocks[seg_num - 1].xcor()
            new_y = self.snake_blocks[seg_num - 1].ycor()
            self.snake_blocks[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



