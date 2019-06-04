# aimusic
Projects that compose lyrics using ai

# Environments
* python 3.6
* tensorflow 1.13.1
* magenta 1.1.1
* [torch rnn](https://github.com/jcjohnson/torch-rnn)

# Set Environment
1.clone our code

```
git clone https://github.com/ai-lyric-composition/aimusic
```

2.set virtualenv
* First, install virtualenv 

```
pip3 install virtualenv virtualenvwrapper
```

* Second, create virtualenv (in Proejct directory)

```
cd aimusic
virtualenv --python=3.6 your_env_name
```

* Third, activate your virtualenv

```
source your_env_name/bin/activate
```

3.install dependencies

```
cd magenta
pip install -e .
```
4.add project path to system environment 

* add ~/.bash_profile
```
vi ~/.bash_profile
```
* write ~/.bash_profile
```
PYTHONPATH=$PYTHONPATH:Your Project Abs Path
export PYTHONPATH
```
* execute ~/.bash_profile
```
source ~/.bash_profile
```
now, execute our code in [src]( https://github.com/ai-lyric-composition/aimusic/tree/master/src) directory!