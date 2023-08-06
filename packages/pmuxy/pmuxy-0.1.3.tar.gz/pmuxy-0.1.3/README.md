[![PyPI version](https://badge.fury.io/py/pmuxy.svg)](https://badge.fury.io/py/pmuxy)
# pmuxy

A simple tmux windows manager.

## Install

```yaml
$ pip3 install pmuxy
```

## Commands

List all configurations under ~/.pmuxy:
```
$ pmuxy list
```

Open a configuration:
```
$ pmuxy open <configuration>
```
pmuxy will look for the first session on the tmux server and open a new window in there.

## Configuration

Configuration files are simple yaml files and they should be stored under ~/.pmuxy

Example file:
```yaml
window_name: test-window
attach: false
shell_commands:
  - export TEST_VAR=test #Sets a new variable
tmux_commands:
  - select-pane -P bg=colour236 #The first pane will have the background color 236
```
* `window_name` - The new window name.
* `attach` - Boolean to tell pmuxy whether we want to attach to the new window or no, defaults to `true`.
* `shell_commands` - These commands will be launched on the shell within the first pane of the new window.
* `tmux_commands` - These commands will be launched on the new tmux window.
