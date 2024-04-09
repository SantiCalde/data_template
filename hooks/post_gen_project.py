import subprocess
import os

# Iniciar ambiente virtual
subprocess.call(['python', '-m', 'venv', 'venv'])

# Path to a Python interpreter that runs any Python script
# under the virtualenv /path/to/virtualenv/
python_venv =   os.getcwd()+"\\venv\\Scripts\\python.exe"

subprocess.call([python_venv,'-m', 'pip', '--upgrade', 'pip'])
subprocess.call([python_venv,'-m', 'pip', 'install', '-r', 'requirements.txt'])


# Configurar el ambiente para recibir notebooks.
if '{{ cookiecutter.project_packages }}' == 'Notebook':
  subprocess.call([python_venv,'-m', 'ipykernel', 'install', '--user', '--name', 'venv'])


# Guardar las dependencias instaladas
packages = subprocess.check_output(['pip', 'list']).decode('utf-8')
with open('installed_packages.txt', 'w') as f:
    f.write(packages)


# Iniciar git
subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])