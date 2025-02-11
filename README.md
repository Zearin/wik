# WIK
wik is command based wiki. 
It let you search for any wikipedia up to date article on one query to your terminal.

<div align="center">

  ### \[[Installation](#installation)] \[[Options](#options)] \[[Examples](#example)] \[[Contribution](#contribution)]

<br>
</div>

## Requirements
- Python3
- beautifulsoup4

## Installation

#### Linux

```bash
sudo pip3 install beautifulsoup4 flit_core
git clone https://github.com/yashsinghcodes/wik.git
cd wik
sudo pip3 install .
```
<br>

#### Windows

```
pip install beautifulsoup4 flit_core
git clone https://github.com/yashsinghcodes/wik.git
cd wik
pip install .
```
>Note: Windows users should have added python to there environment variable

## Options
Using wik is acutally really simple.

```
usage: wik [-h] [-s SEARCH] [-i INFO] [-q QUICK]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search any topic
  -i INFO, --info INFO  Get info on any topic(Use correct name)
  -q QUICK, --quick QUICK
                        Get the summary on any topic
```

## Example

```bash
$ wik -i Linux
```
![carbon (6)](https://user-images.githubusercontent.com/32360914/155836508-63c7424f-b7d6-4871-a170-e2f0fdd6617d.png)

```bash
$ wik -q Linux
```
![carbon (7)](https://user-images.githubusercontent.com/32360914/155836565-281eb678-9605-4131-a6c9-9a6c871bdc77.png)


## Contribution
You can contribute to the project by opening a issue if you face any or making a pull
requests, if you think you can fix somthing or make improvment on the code. If you have some
ideas related to the project you can [contact me](https://yashwastaken.xyz/contact).

### Want to work with me?
This is the task [list](https://trello.com/b/ZW0eYT62/wik) if you think you can implement any please make a pull request.
>Note: Do things which are under To-do do not make a pull request for tasks which are already under development.
