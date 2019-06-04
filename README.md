# aimusic
Projects that compose lyrics using ai

# Environments
* python 3.6
* tensorflow 1.13.1
* magenta 1.1.1
* [torch rnn](https://github.com/jcjohnson/torch-rnn)

#  Usage
1. clone our code
```
git clone https://github.com/ai-lyric-composition/aimusic
```
<br>
2. install dependencies

```
cd magenta
pip install -e
```
<br>
3. add project path to system environment 

* add ~/.bash_profile
```
vi ~/.bash_profile
```
* edit ~/.bash_profile
```
PYTHONPATH=$PYTHONPATH:/home/pirl/Desktop/aimusic
export PYTHONPATH
```
* execute ~/.bash_profile
```
source ~/.bash_profile
```
<br>
4. execute our code in [src][src_id] directory!

[src_id]: https://github.com/ai-lyric-composition/aimusic/tree/master/src
