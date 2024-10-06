import os
import subprocess

def compile_ui_to_py(ui_path, output_path):
    command = f"pyuic6 -o {output_path} {ui_path}"
    subprocess.run(command, shell=True)

def compile_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.endswith(".ui"):
            ui_path = os.path.join(input_folder, file)
            file_name = os.path.splitext(file)[0]  # Remove extension
            output_path = os.path.join(output_folder, f"{file_name}.py")
            
            compile_ui_to_py(ui_path, output_path)

if __name__ == "__main__":
    input_folder = "./ui_views/"
    output_folder = "./view/"

    compile_folder(input_folder, output_folder)