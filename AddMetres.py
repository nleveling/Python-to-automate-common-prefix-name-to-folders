import os

master_folder = "O:/NathanLeveling/PythonAddMetres/Exports"

#List all subdirectories in the 'Master' folder
subfolders = [f for f in os.listdir(master_folder) if os.path.isdir(os.path.join(master_folder, f))]

#Loop through the subfolders and rename them
for subfolder in subfolders:
    old_path = os.path.join(master_folder, subfolder)
    new_name = "metres" + subfolder  # Add 'metres' to the name
    new_path = os.path.join(master_folder, new_name)

    #Rename the subfolder
    os.rename(old_path, new_path)

print("Subfolders renamed successfully.")