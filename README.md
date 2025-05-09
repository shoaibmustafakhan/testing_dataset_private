# Free_CVAT_Workaround

This code should act as a workaround for the free CVAT not exporting images.
To make this work, please make sure you do the following:

1. download the dataset from CVAT.
2. Extract the .zip folder.
3. place the "cvat_workaround.py" file into the root of the database directory, next to "data.yaml", "labels" folder and "train.txt".
4. place the video into the same place.
5. make a .venv in the same directory. note: please make sure you have python installed btw.
6. activate the venv (you can refer on venv's and how to activate them on the internet or chatgpt).
7. install opencv library using pip (you can refer to the internet or chatgpt on how to install it, depending on if you use conda or pip).
8. open "cvat_workaround.py" and change the name of the video at the top of the code where the comment points (make sure to put .mp4 at the end).
9. run the file "cvat_workaround.py"
10. you will be able to see the outputs in your terminal of the video being divided into frames (please make sure to close other systems running on your system because it might get slower and in edge cases, might crash your system).
11. at the end you will get "Done extracting required frames."
12. move the "labels" folder into the newly created "data" folder in the same directory.
13. .zip the entire thing and you should be good to go.
