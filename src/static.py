import os, shutil
from converter import *

def copy_static(source, destination):
    
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    
    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)
        if os.path.isfile(src):
            print(f"Copying file: {src} -> {dst}")
            shutil.copy(src, dst)
        if os.path.isdir(src):
            os.mkdir(dst)
            copy_static(src, dst)

def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.split("# ")[1].strip()
            if len(header) > 0:
                return header
    raise Exception("Error: No h1 header found.")
    
    

def generate_page(from_path, template_path, dest_path):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    try:
        with open(from_path, "r") as f:
            markdown = f.read()
        with open(template_path, "r") as f:
            template = f.read()
    except Exception as e:
        return f"Error: {e}"
    
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    html = template.replace("{{ Title }}",  title).replace("{{ Content }}", content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    try:
        with open(dest_path, "w") as f:
            f.write(html)
    except Exception as e:
        return f"Error: {e}"
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        content = os.path.join(dir_path_content, item)
        if os.path.isfile(content):
            file, ext = os.path.splitext(item)
            if ext.lower() == ".md":
                to_html = file+".html"
                generate_page(content, template_path, os.path.join(dest_dir_path, to_html))
        if os.path.isdir(content):
            new_dest_dir = os.path.join(dest_dir_path, item)
            os.makedirs(new_dest_dir, exist_ok=True)
            generate_pages_recursive(content, template_path, new_dest_dir)