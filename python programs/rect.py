print("enter the center coordinate of the 1st rectangle (x,y): ")
X=eval(input())
Y=eval(input())
print("enter the height and width of the 1st rectangle: ")
width=eval(input())
height=eval(input())
print("enter the center coordinate of the 2st rectangle (x,y): ")
X1=eval(input())
Y1=eval(input())
print("enter the height and width of the 2st rectangle: ")
width1=eval(input())
height1=eval(input())

def checker(value, min, max):
	if((value >= min) and (value<=max)):
		return True
def rectlogic():
	xoverlap = bool(checker(X,X1,X1+width1) or checker(X1,X,X+width))
	yoverlap = bool(checker(Y,Y1,Y1+height1) or checker(Y1,Y,Y+height))
	return bool(xoverlap and yoverlap)
if(rectlogic()):
	print("Overlapping Rectangles")
else:
	print("Rectangle Doesn't Overlap")

