from PIL import ImageFont
from parent import Parent

class Bitstrap(Parent):
    def __init__(self, width, height):
        super(Bitstrap, self).__init__(width, height)
        self.x = 10
        self.y = 30
        self.bit_length = 25
        
    def check(self, l):
        previous = None
        count = 1
        repeats = {}
        for ind, i in enumerate(l):
            if i == previous:
                count += 1
            if i != previous:
                if count > 3:
                    repeats[ind - count] = count
                count = 1
            if ind == len(l)-1 and count > 3:
                repeats[ind - count + 1] = count
                count = 1
            previous = i
        return repeats
        
    def draw_strap(self, bits):
        fontsize = 16
        font = ImageFont.truetype(self.font_path, fontsize)
        repeats = self.check(bits) 
        print repeats
        
        x = self.x
        y = self.y
        repeat = False
        repeat_index = None
        already_drawn = False
        arc_x_start = 0
        arc_x_end = 0
        for ind, bit in enumerate(bits):
            if not repeat:
                self.draw.line((x, y, x + self.bit_length, y), fill=128)
                self.draw.text((x + 4, y - 20), bit, fill="black", font=font)
                x += 30
            else:
                if not already_drawn:
                    arc_x_start = x - self.bit_length / 2 - 5
                    #self.draw.line((x, y, x + self.bit_length, y), fill=128)
                    self.draw.point((x + 4, y), fill=128)
                    self.draw.point((x + 8, y), fill=128)
                    self.draw.point((x + 12, y), fill=128)
                    self.draw.point((x + 16, y), fill=128)
                    already_drawn = True
                    x += 30
            if ind in repeats.keys():
                repeat = True
                repeat_index = ind
            if repeat == True and ind == repeat_index + repeats[repeat_index] - 2:
                arc_x_end = x + self.bit_length / 2
                self.draw.arc((arc_x_start, y, arc_x_end, y + 10), 0, 180, 0)
                xt = (arc_x_start + arc_x_end) / 2
                text = str(repeats[repeat_index])
                xt = xt - len(text) * 5
                self.draw.text((xt, y + 10), text, fill="black", font=font)
                repeat = False
                repeat_index = None
                already_drawn = False
           
