import turtle

def striangle(depth,base):
   turtle.down()

   if depth == 0:
      turtle.begin_fill()
      for i in 0,1,2:
         turtle.forward(base)
         turtle.left(120)
      turtle.end_fill()
   else:
      for i in 0,1,2:
         striangle(depth-1,base)
         turtle.up()
         turtle.forward(base*2**depth)
         turtle.left(120)
         turtle.down()

turtle.reset()
striangle(10,20)