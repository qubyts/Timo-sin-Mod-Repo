import os
import shutil

def install_mods(mods_directory, minecraft_mods_folder):
    if not os.path.exists(mods_directory):
        print(f"Mods directory '{mods_directory}' does not exist.")
        return

    jar_files = [f for f in os.listdir(mods_directory) if f.endswith('.jar')]
    
    if not jar_files:
        print("No .jar files found in the mods directory.")
        return

    for jar_file in jar_files:
        source = os.path.join(mods_directory, jar_file)
        destination = os.path.join(minecraft_mods_folder, jar_file)

        try:
            shutil.copy(source, destination)
            print(f"Installed mod: {jar_file}")
        except Exception as e:
            print(f"Error installing {jar_file}: {e}")

if __name__ == "__main__":
    mods_directory = './mods'  # Path to the mods directory
    minecraft_mods_folder = './path/to/minecraft/mods'  # Path to the Minecraft mods folder

    install_mods(mods_directory, minecraft_mods_folder)