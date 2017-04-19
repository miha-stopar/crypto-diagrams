from PIL import ImageFont
from parent import Parent

class Protocol(Parent):
    def __init__(self, width, height):
        super(Protocol, self).__init__(width, height)
        self.x = 20
        self.y = 40
        fontsize = 16
        self.font = ImageFont.truetype(self.font_path, fontsize)
     
    def draw_connections(self, connections):
        x = self.x
        y = self.y # y coordinate of the arrows
        x_offset = 10
        for c in connections:
            text1 = c[0]
            line_w = self.draw_multiline_text(text1, x, y, move_up_coef=0.5)
            if text1 != "":
                x = x + line_w + x_offset
 
            arrow_text = c[1]
            arrow_text_w = self.draw_multiline_text(arrow_text, x, y - 5, move_up_coef=1)
            self.draw_arrow(x, y, x+arrow_text_w, y)
            
            x = x + arrow_text_w + x_offset
            text2 = c[2]
            line_w = self.draw_multiline_text(text2, x, y, move_up_coef=0.5)
            x = x + line_w + x_offset

        

