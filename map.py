# 0 - поле
# 1 - дерево
# 2 - река

class Map:
    #def generate_rivers():

    #def generate_forest():

    def print_map():
        for row in self.cells:
            for cell in row:
                if cell == 0:
                    print('❎', end ='')
                elif cell == 1:
                    print('🌳', end ='')
                elif cell == 2:
                    print('🌊', end = '')
            print()

    def __init__(self, w, h):
        self.cells = [[0 for i in range(w)] for j in range(h)]
