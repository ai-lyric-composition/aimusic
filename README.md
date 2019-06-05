# aimusic
Projects that compose lyrics using ai

# Environments
* python 3.6
* tensorflow 1.13.1
* cuda 10
* magenta 1.1.1
* [torch rnn](https://github.com/jcjohnson/torch-rnn)

# Set Environment
Step 1. clone our code

```
git clone https://github.com/ai-lyric-composition/aimusic
```

Step 2. set virtualenv (If you do not want to configure the virtual environment, skip to step 3)
* First, install virtualenv 

```
pip3 install virtualenv virtualenvwrapper
```

* Second, create virtualenv (in Proejct directory)

```
cd aimusic
virtualenv --python=python3.6 [your_env_name]

if you get the error "The path x.x does not exist":
    virtualenv --python=[which python3 PATH] [your_env_name]
```

* Third, activate your virtualenv

```
source [your_env_name]/bin/activate
```

Step 3. install tensorflow 1.13.1 & CUDA 10

Visit the page below and install the correct version
https://www.tensorflow.org/install/gpu

Step 4. install magenta
```
if CPU:
    pip install magenta 
elif GPU:
    pip install magenta-gpu
    
sudo apt-get install build-essential libasound2-dev libjack-dev
```
Step 5. add project path to system environment 

* add ~/.bash_profile
```
vi ~/.bash_profile
```
* write ~/.bash_profile
```
PYTHONPATH=$PYTHONPATH:Your Project Root Directory Abs Path
export PYTHONPATH
```
* execute ~/.bash_profile
```
source ~/.bash_profile
```
Now, execute our code in [src]( https://github.com/ai-lyric-composition/aimusic/tree/master/src) directory!
