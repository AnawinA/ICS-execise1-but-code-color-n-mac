"""color_n_dec"""

def color2dec(color, index=False) -> int | None:
    """color2dec"""
    color = color.replace("#", "")
    col_list = []
    if len(color) == 3:
        col_list = [int(color[0] * 2, 16), int(color[1] * 2, 16), int(color[2] * 2, 16)]
    if len(color) == 6:
        col_list = [int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)]
    if col_list:
        if index:
            return {"R": col_list[0], "G": col_list[1], "B": col_list[2]}
        else:
            return col_list
    else:
        return None

def dec2color(dec, h=True, upper=True) -> str:
    """dec2color"""
    h = "#" if h else ""
    x = "X" if upper else "x"
    if type(dec) == list:
        return f"{h}{dec[0]:02{x}}{dec[1]:02{x}}{dec[2]:02{x}}"
    elif type(dec) == dict:
        return f"{h}{dec['R']:02{x}}{dec['G']:02{x}}{dec['B']:02{x}}"
    else:
        return None
