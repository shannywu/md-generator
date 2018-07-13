class Table(object):

    def alignment(self, level):
        return ''.ljust((level-1)*4, ' ')

    def add_row(self, row, level=0):
        result = '{}|{}|\n'.format(self.alignment(level), '|'.join(row))
        return result

    def add_sep_row(self, cols=2, level=0):
        result = '{}|{}|\n'.format(self.alignment(level), '|'.join(['----'] * cols))
        return result