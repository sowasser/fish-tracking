import deeplabcut

# Start a new project:
task = "Stickleback Shoaling"  # Enter the name of your experiment Task
experimenter = "Sophie"  # Enter the name of the experimenter
video = ["tracking_videos/sticklebacks1.avi"]  # Enter the paths of your videos you want to grab frames from.

path_config_file = deeplabcut.create_new_project(task,
                                                 experimenter,
                                                 video,
                                                 working_directory="sticklebacks",
                                                 copy_videos=True)

# Pick up from where you left off:
# path_config_file = "/Users/user/Desktop/Local/Mackerel/fish-tracking/sticklebacks/Stickleback Shoaling-Sophie-2019-05-10/config.yaml"
