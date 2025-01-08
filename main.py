
X_ITEMS = 3
Y_ITEMS = 2

X_GAP = 70
Y_GAP = 120

f = open("start.gcode")
start = f.read()

f = open("middle.gcode")
middle = f.read()

f = open("end.gcode")
end = f.read()

f = open("out.gcode", 'w')

f.write(start)
for i in range(Y_ITEMS):
    for i in range(X_ITEMS):
        f.write(middle)
        f.write("G1 X"+str(X_GAP)+"\n")
        f.write("G92 X0\n")
    f.write("G28 X0\n")
    f.write("G1 Y"+str(Y_GAP)+"\n")
    f.write("G92 X0\n")
f.write(end)
f.close()