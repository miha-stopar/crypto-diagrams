from PIL import ImageFont
from _collections import defaultdict
from parent import Parent

class Table(Parent):
    def __init__(self, width, height):
        super(Table, self).__init__(width, height)
        self.x_offset = 5
        #self.y_offset = height / 2 - 5
        #self.x = 10
        #self.y = 10
        
    def draw_table(self, cols_num, texts):
        rows_num = len(texts) / cols_num
        if len(texts) % cols_num != 0:
            rows_num += 1
        x_init = 10; y_init = 10
        x = x_init; y = y_init
        x_offset = 10
        y_offset = 5
        fontsize = 16
        font = ImageFont.truetype(self.font_path, fontsize)
        cols_width = defaultdict(int)
        rows_height = defaultdict(int)
        col_index = 0
        row_index = 0
        for ind, text in enumerate(texts):
            w, h = self.draw.textsize(text, font)
            print text
            if h > rows_height[row_index] - 2 * y_offset:
                rows_height[row_index] = h + 2 * y_offset
            if w > cols_width[col_index] - 2 * x_offset:
                cols_width[col_index] = w + 2 * x_offset
            if ind % cols_num == cols_num-1:
                col_index = 0
                row_index += 1
            else:
                col_index += 1
        
        col_index = 0
        row_index = 0
        for ind, text in enumerate(texts):
            self.draw.text((x + x_offset, y + y_offset), text, fill="black", font=font)
            x += cols_width[col_index]
            if ind % cols_num == cols_num-1:
                y += rows_height[row_index]
                x = x_init
                col_index = 0
                row_index += 1
            else:
                col_index += 1
        
        x = x_init; y = y_init
        line_length_x = reduce(lambda x,y:x+y, cols_width.values())
        line_length_y = reduce(lambda x,y:x+y, rows_height.values())
        for i in range(rows_num + 1):
            self.draw.line((x, y, x + line_length_x, y), fill=128)
            y += rows_height[i]
        y = y_init
        for i in range(cols_num + 1):
            self.draw.line((x, y, x, y + line_length_y), fill=128)
            x += cols_width[i]
       

