from PIL import ImageFont
from parent import Parent

class Protocol2(Parent):
    def __init__(self, width, height, font_size=16):
        super(Protocol2, self).__init__(width, height)
        self.x = 20
        self.y = 40
        self.font = ImageFont.truetype(self.font_path, font_size)
        
    def _get_connections_length(self, connections):
        l = 0
        lengths = []
        for c in connections:
            w, _ = self.draw.textsize(c, self.font)
            lengths.append(w)
            if w > l:
                l = w
        return l, lengths
     
    def draw_protocol(self, parties, connections, box_height=200, first_arrow_to_right=True):
        c_length, lengths = self._get_connections_length(connections)

        rect1_w = self.draw_multiline_text(parties[0], self.x, self.y, offset=20)
        self.draw.rectangle(((self.x, self.y), (self.x + rect1_w, self.y + box_height)), outline="black")

        rect2_w = self.draw_multiline_text(parties[1], self.x + rect1_w + c_length + 20, 
                                           self.y, offset=20)
        self.draw.rectangle(((self.x + rect1_w + c_length + 20, self.y), 
                             (self.x + rect1_w + c_length + 20 + rect2_w, self.y + box_height)), 
                            outline="black")
        x = self.x
        y = self.y
        arrow_back = not first_arrow_to_right
        for ind, c in enumerate(connections):
            x_offset = (c_length - lengths[ind]) / 2
            line_w = self.draw_multiline_text(c, x + rect1_w + 10 + x_offset, y + 5, 
                                              move_up_coef=0)
            self.draw_arrow(x + rect1_w + 10, y, x + rect1_w + 10 + c_length, y, back=arrow_back)
            y += 40
            arrow_back = not arrow_back
        
        
        
        
        
        
        
        