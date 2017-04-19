from PIL import Image, ImageDraw

class Parent(object):
    def __init__(self, width, height):
        img = Image.new("RGB", (width, height), color="white")
        self.img = img
        self.draw = ImageDraw.Draw(img)
        self.font_path = '/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf'
      
    def draw_arrow(self, x, y, x1, y1, back=False):
        self.draw.line((x, y, x1, y1), fill=128)
        if not back:
            self.draw.line((x1-5, y1-5, x1, y1), fill=128)
            self.draw.line((x1-5, y1+5, x1, y1), fill=128)
        else:
            self.draw.line((x, y, x+5, y-5), fill=128)
            self.draw.line((x, y, x+5, y+5), fill=128)
        
    def draw_multiline_text(self, text, x, y, move_up_coef = 0, offset=0):
        """ Split text by new line sign into a list and draw each element of a list.

         Parameters
        ----------
        text : string
            Text which is to be written.
        x : int
            Coordinate x where text is to be written.
        y : int
            Coordinate y where text is to be written.
        move_up_coef: float
            The height of the text is multiplied by this coefficient and then the whole text
            is moved up by this value.
        """
        text_lines = text.split('\n')
        text_lines = map(lambda x: x.strip(), text_lines)
        text_lines = filter(lambda x: x!='', text_lines)
        if text == "":
            text_lines.append("dummy") # just to calculate text_size
        line_w, line_h = self.draw.textsize(text_lines[0], self.font)
        if text == "":
            text_lines = []
        for ind, t in enumerate(text_lines):
            w, _ = self.draw.textsize(t, self.font)
            if w > line_w:
                line_w = w
        
        line_w += offset
        move_up = line_h * len(text_lines) * move_up_coef
        for ind, t in enumerate(text_lines):
            self.draw.text((x + offset/2, y + ind * line_h - move_up), 
                            t, fill="black", font=self.font)
        return line_w


    def save(self, path):
        self.img.save(path, "PNG")
