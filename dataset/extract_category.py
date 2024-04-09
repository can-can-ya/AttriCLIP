import os
import shutil
import json

# Specify the categories to keep
desired_classes = [
    'American robin', 'Gila monster', 'eastern hog-nosed snake', 'garter snake', 'green mamba',
    'European garden spider', 'lorikeet', 'goose', 'rock crab', 'fiddler crab', 'American lobster',
    'little blue heron', 'American coot', 'Chihuahua', 'Shih Tzu', 'Papillon', 'toy terrier',
    'Treeing Walker Coonhound', 'English foxhound', 'borzoi', 'Saluki', 'American Staffordshire Terrier',
    'Chesapeake Bay Retriever', 'Vizsla', 'Kuvasz', 'Komondor', 'Rottweiler', 'Dobermann', 'Boxer',
    'Great Dane', 'Standard Poodle', 'Mexican hairless dog (xoloitzcuintli)', 'coyote', 'African wild dog',
    'red fox','tabby cat', 'meerkat', 'dung beetle', 'stick insect', 'leafhopper', 'hare', 'wild boar',
    'gibbon', 'langur', 'ambulance', 'baluster handrail', 'bassinet', 'boathouse', 'poke bonnet',
    'bottle cap', 'car wheel', 'bell or wind chime', 'movie theater', 'cocktail shaker', 'computer keyboard',
    'Dutch oven', 'football helmet', 'gas mask or respirator', 'hard disk drive', 'harmonica', 'honeycomb',
    'clothes iron', 'jeans', 'lampshade', 'laptop computer', 'milk can', 'mixing bowl', 'modem', 'moped',
    'graduation cap', 'mousetrap', 'obelisk', 'park bench', 'pedestal', 'pickup truck', 'pirate ship',
    'purse', 'fishing casting reel', 'rocking chair', 'rotisserie', 'safety pin', 'sarong', 'balaclava ski mask',
    'slide rule', 'stretcher', 'front curtain', 'throne', 'tile roof', 'tripod', 'hot tub', 'vacuum cleaner',
    'window screen', 'airplane wing', 'cabbage', 'cauliflower', 'pineapple', 'carbonara', 'chocolate syrup',
    'gyromitra', 'stinkhorn mushroom'
]

# Specifies the path to the original dataset
train_dir = '/NAS02/RawData/ILSVRC2012/train'
val_dir = '/NAS02/RawData/ILSVRC2012/val'

# Specify a new output folder path
output_dir = '/NAS02/RawData/ILSVRC2012_100'

# Create output folder
os.makedirs(output_dir, exist_ok=True)

# Specify JSON file path
json_file_path = 'imagenet_class_index.json'

# Open and load JSON file
with open(json_file_path, 'r') as json_file:
    json_data = json.load(json_file)
    class_dict = {i[1]: i[0] for i in list(json_data.values())}

# Change the category name to the corresponding category ID
desired_classes = [class_dict[i] for i in desired_classes]

def copy_desired_classes(source_dir, destination_dir):
    for class_folder in os.listdir(source_dir):
        if class_folder in desired_classes:
            class_source = os.path.join(source_dir, class_folder)
            class_destination = os.path.join(destination_dir, class_folder)
            shutil.copytree(class_source, class_destination)

# Copy the desired category from the train folder
copy_desired_classes(train_dir, os.path.join(output_dir, 'train'))

# Copy the desired category from the val folder
copy_desired_classes(val_dir, os.path.join(output_dir, 'val'))
