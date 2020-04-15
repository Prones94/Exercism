class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
        self.matrix = self.generate_matrix()

    def row(self, index):
        return self.matrix[index - 1]
        

    def column(self, index):
        columns = []
        for row in self.matrix:
            columns.append(row[index - 1])
        return columns
    
    def generate_matrix(self):
        split_matrix = self.matrix_string.split('\n')
        for k, v in enumerate(split_matrix):
            split_matrix[k] = [int(num) for num in v.split(' ')]
        return split_matrix

        