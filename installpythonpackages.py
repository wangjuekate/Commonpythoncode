import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"Successfully installed {package}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package}")

# Example usage
packages_to_install = ["PyPDF2", "pandas"]

for package in packages_to_install:
    install_package(package)
