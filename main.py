from faker import Faker
import json

new_fake = Faker()

color_list = []
for color in range(20):
  new_color = new_fake.color_name()
  color_list.append(new_color)
print(color_list)

def remove_dups(your_list):
  new_set = set(your_list)
  new_fake.new_list = list(new_set)
   
remove_dups(color_list)

color_dict = {key : len(key) for key in new_fake.new_list}

with open("./colors.json", "w") as colors_json:
  json.dump(color_dict, colors_json)

with open("./colors.json", "r") as colors_json:
  colors = json.load(colors_json)
for color, length in colors.items():
  if length >= 4:
    print(f"Color: {color}, Length: {length}")