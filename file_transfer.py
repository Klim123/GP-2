import shutil
import os

for i in range(1, 101):
    filename = f"/workspaces/GP-2/chastichnaya_zanyatost_{i}.txt"
    destination_filename = f"/workspaces/GP-2/pages_a1/chastichnaya_zanyatost_{i}.txt"
    shutil.move(filename, destination_filename)