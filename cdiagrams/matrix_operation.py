from PIL import ImageFont 
from parent import Parent

class MatrixOperation(Parent):
    def __init__(self, width, height):
        super(MatrixOperation, self).__init__(width, height)
        self.x_offset = 5
        #self.y_offset = height / 2 - 5
        self.x_init = 10
        self.y_init = 10
        self.x = 10
        self.y = 10
        self.x_offset = 5
        self.y_offset = 5
        self.y_max = 0
        self.cols_width = 0
        self.rows_height = 0
        fontsize = 16
        self.font = ImageFont.truetype(self.font_path, fontsize)
        
    def draw_matrices(self, matrices):
        for m in matrices:
            cols_num = m[0]
            texts = m[1]
            if type(texts) != list:
                continue
            for text in texts:
                w, h = self.draw.textsize(text, self.font)
                if h > self.rows_height - 2 * self.y_offset:
                    self.rows_height = h + 2 * self.y_offset
                if w > self.cols_width - 2 * self.x_offset:
                    self.cols_width = w + 2 * self.x_offset
   
        for m in matrices:
            cols_num = m[0]
            texts = m[1]
            self.x += 10
            if type(texts) != list:
                operation = texts
                self.draw_operation_sign(operation)
            else:
                self.draw_matrix(cols_num, texts)
            
    def draw_operation_sign(self, operation):
        y = (self.y_init + self.y_max) / 2
        self.draw.text((self.x, y), operation, fill="black", font=self.font)
        self.x += 10 * len(operation)
                
    def draw_matrix(self, cols_num, texts):
        rows_num = len(texts) / cols_num
        if len(texts) % cols_num != 0:
            rows_num += 1
        x = self.x; y = self.y
        col_index = 0
        row_index = 0
        for ind, text in enumerate(texts):
            self.draw.text((x + self.x_offset, y + self.y_offset), text, fill="black", font=self.font)
            x += self.cols_width
            if ind % cols_num == cols_num-1:
                y += self.rows_height
                x = self.x
                col_index = 0
                row_index += 1
            else:
                col_index += 1
        
        x = self.x; y = self.y
        line_length_x = cols_num * self.cols_width
        line_length_y = rows_num * self.rows_height
        
        # do not left space in the last column (the value is written at the beginning of the cell
        # plus self.x_offset:
        w, _ = self.draw.textsize(text, self.font)
        r = self.cols_width - w - 2 * self.x_offset
        print(r)
        
        for i in range(rows_num + 1):
            if i == 0 or i == rows_num:
                self.draw.line((x, y, x + 5, y), fill=128)
                self.draw.line((x - r + line_length_x - 5, y, x - r + line_length_x, y), fill=128)
            y += self.rows_height
        y = self.y
        for i in range(cols_num + 1):
            if i == 0:
                self.draw.line((x, y, x, y + line_length_y), fill=128)
            if i == cols_num:
                self.draw.line((x - r, y, x - r, y + line_length_y), fill=128)
            x += self.cols_width
        self.x = x - self.cols_width
        self.y_max = y + line_length_y - self.rows_height
       

