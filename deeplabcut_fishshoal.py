import deeplabcut

task = "Stickleback Shoaling"  # Enter the name of your experiment Task
experimenter = "Sophie"  # Enter the name of the experimenter
video=["videos/video1.avi", "videos/video2.avi"]  # Enter the paths of your videos you want to grab frames from.

path_config_file=deeplabcut.create_new_project(task,
                                               experimenter,
                                               video,
                                               working_directory="Full path of the working directory",
                                               copy_videos=True/False)  # change the working directory to where you want the folders created.

# The function returns the path, where your project is.
# You could also enter this manually (e.g. if the project is already created and you want to pick up, where you stopped...)
# path_config_file = '/home/Mackenzie/Reaching/config.yaml' # Enter the path of the config file that was just created from the above step (check the folder)
