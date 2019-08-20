color_in = input("Please enter a name of color: ")
colordic = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "AntiqueWhite1": "#ffefdb",
    "AntiqueWhite2": "#eedfcc",
    "AntiqueWhite3": "#cdc0b0",
    "AntiqueWhite4": "#8b8378",
    "aquamarine1": "#7fffd4",
    "aquamarine2": "#76eec6"
}
index = 0
for key in colordic:
    if key == color_in:
        print("The hex-color of {} is {} ".format(key,colordic[key]))
        index = 1
        break
if index == 0:
    print("NOT FOUND !!")