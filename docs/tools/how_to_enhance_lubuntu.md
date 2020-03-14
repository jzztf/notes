# how to enhance lubuntu

> lunbuntu is my favorite linux

## how to make lxterminal of lubuntu transparent

* first install "compton"

`sudo apt install compton`

* then run the following command for testing

`compton --opacity-rule 45:'class_g *= "X-terminal-emulator"'`

* if last command works, we can edit the config file and add it to autostart list

```bash
echo "opacity-rule = [\"90:class_g *= 'X-terminal-emulator'\"]" >> ~/.config/compton
echo compton >> ~/.config/lxsession/Lubuntu/autostart
```
