def img(self, file_name, height=10, width=10, size=0):
    if size>0:
        height=size
        width=size
    return f'<img src="images/{file_name}.png" height="{height}", wdith="{width}">'

