if window.get_active_class() != 'xfce4-terminal.Xfce4-terminal':
    keyboard.send_keys("<end>")
else:
    keyboard.send_keys("<ctrl>+e")