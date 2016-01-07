CycleSetting
==========

[Cycle Setting plugin for Sublime Text 2](https://github.com/jmm/Sublime-Text-Cycle-Setting)を改造したもの。Sublime Text 2とSublime Text 3の両方で使える。

インストール方法
----------

Packagesディレクトリに入れよ。

設定例
----------

Default (*YourOS*).sublime-keymapに次のように書け。

```
[
	...
	{
		"keys": ["alt+w"],
		"command": "cycle_setting",
		"args": {
			"setting": "draw_white_space",
			"options": ["none", "all"]
		}
	},
	{
		"keys": ["alt+s"],
		"command": "cycle_setting",
		"args": {
			"setting": "font_size",
			"options": [13, 14]
		}
	},
	...
]
```
