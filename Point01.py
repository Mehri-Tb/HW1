import matplotlib.pyplot as plt

def Draw(x1, y1, x2, y2):
    XV = [x1, x2]
    YV = [y1, y2]
    plt.plot(XV, YV, marker='*')  #Draw Plot 
    # Adjust range
    plt.xlim(min(x1, x2) - 1, max(x1, x2) + 1)
    plt.ylim(min(y1, y2) - 1, max(y1, y2) + 1)
    plt.text(x1, y1, f'({x1}, {y1})', verticalalignment='bottom', horizontalalignment='right')
    plt.text(x2, y2, f'({x2}, {y2})', verticalalignment='bottom', horizontalalignment='right')
    plt.xlabel('X') #X Name
    plt.ylabel('Y') #Y Name
    
    plt.show()
    
#Read data
x1 = float(input("X1: "))
y1 = float(input("Y1 "))
x2 = float(input("X2 "))
y2 = float(input("Y2 "))
print (x1, y1, x2, y2)
Draw(x1, y1, x2, y2)
