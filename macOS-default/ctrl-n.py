if window.get_active_class() != 'xfce4-terminal.Xfce4-terminal':
    keyboard.send_keys("<down>")
else:
    keyboard.send_keys("<ctrl>+n")