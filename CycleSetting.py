import sublime, sublime_plugin

class CycleSettingCommand(sublime_plugin.ApplicationCommand):
	def run(self, setting, options):
		if not isinstance(options, list) or len(options) == 0:
			return
		
		s = sublime.load_settings('Preferences.sublime-settings')
		
		setting_name = setting
		setting_value = s.get(setting_name)
		
		index = 0
		
		if setting_value in options:
			index = options.index(setting_value) + 1
		
		if index >= len(options):
			index = 0
		
		setting_value = options[index]
		s.set(setting_name, setting_value)
		
		sublime.save_settings('Preferences.sublime-settings')
		
		self.view.set_status(
			'cycle_setting',
			"Setting '{setting_name}' cycled to value '{setting_value}'".format(**locals())
		)
