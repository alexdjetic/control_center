# control_center

## install python

### ubuntu/derivate

```fish
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python-pip xterm
```
### fedora

```fish
sudo dnf update && sudo dnf install python3 python-pip xterm
```

### centOS/older fedora

```fish
sudo yum update && sudo yum install python3 python-pip xterm
```

### archlinux/manjaro

```fish
sudo pacman -Syu
sudo pacman -S python3 python-pip xterm
```

### alpine

```fish
apk update && apk upgrade
apk add python
```

### gentoo
- go to the official page: [python install for gentoo](https://wiki.gentoo.org/wiki/Python)

## launch
> make sure that your terminal is support by ncurses, xterm is supported that why i use it
to launch, note that `sudo` is only required for docker, if you use it
if your not using, delete every sudo from script in `data.py`

- to launch:
```fish
chmod +x *.sh
./main.py
```

## postinstall
> if you want your script in your path terminal, add main.py and data.py in /bin directory
to do this:
```fish
cd ~/control_center
sudo cp *.py /bin/
```

## necessary tweak
> in main.py there is:
 
```python
data_obj = Data(["docker0", "virbr0", "wlp10s0"])
```

> it my network interface, you need to change to the name of YOUR network interface, to get the name of interface
```fish
ip link
```

have a nive day :)
