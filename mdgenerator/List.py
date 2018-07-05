class List(object):

    def alignment(self, level):
        return ''.ljust((level-1)*4, ' ')

    def add_item(self, item, ordered, level=0):
        if ordered:
            return '{}{}. {}\n'.format(self.alignment(level), 1, item)
        else:
            return '{}- {}\n'.format(self.alignment(level), item)

    def add_list(self, items, ordered, level=0):
        if ordered:
            items = ['{}{}. {}'.format(self.alignment(level), str(i+1), item) for i, item in enumerate(items)]
            result = '\n'.join(items) + '\n'
        else:
            items = ['{}- {}'.format(self.alignment(level), item) for item in items]
            result = '\n'.join(items) + '\n'
        return result

    def add_check_list(self, items, level=0):
        items = ['{}- [ ] {}'.format(self.alignment(level), item) for item in items]
        result = '\n'.join(items) + '\n'
        return result