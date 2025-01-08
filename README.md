# gcode-arrays
This is a repository for making an array of the same part on a 3D printer, by duplicating the gcode.
The parts are printed in one go, one at a time, as opposed to all at once layer by layer.

The advantage of this is that if one of the prints fail, the print can be cancelled and you will still have some parts succeed.

Great for small parts if you need them in high volume, like I did in a recent project. I assume you are using a marlin style gcode printer for using this code.

# Usage
-Start by slicing your stl file in your favorite marlin style slicer!
-Divide the outputted gcode into three files: start.gcode, middle.gcode, and end.gcode
-Enter in main.py your desired parameters: x and y GAP for the distance between each part, x and y items for the quantity of parts in each axis.
-Create a out.gcode file, and run main.py. The program will automatically write in the created out.gcode file.

# licesnse
I applied the MIT open source license to this project.

Thanks, and enjoy!!