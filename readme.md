
### 1. How do you setup local python dev environment?  
- What IDE do you use?
  PyCharm
- How do you setup python production environment in Linux?
  - List the cli commands if possible.
    1. Install pyenv . Linux system comes with python   so we can just use pyenv and use this a  
      $ sudo apt-get update
    2. Install pyenv via git ( assuming git is available )
      $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

    3. Setting up Environment variable and adding the pyenv location  in PATH
      $ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
      $ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
      $ eval "$(pyenv init --path)"
    4. install python versions
      $ pyenv install --list
      $ pyenv install 3.9.16
    5. Set up pyenv global /local for projects
      $ pyenv global 3.9.16
    6. Verify set up 
      $ pyenv versions
    6. install virtual env in the local project folder and use that 

# 2. Are you familiar using any linux distro?
- crontab
- ssh
- nfs
- nginx
      I am familiar using ubuntu ,cent os ,crontab ,ssh and nginx .
