import mdgenerator as mg

if __name__ == '__main__':
    outfile = open('test.md', 'a')

    text = mg.Text()
    outfile.write(text.add_heading('test', 5))
    outfile.write(text.add_italics('test'))
    outfile.write(text.add_bold('test'))
    outfile.write(text.add_emphasis('test'))
    outfile.write(text.add_blockquotes('test'))

    _list = mg.List()
    outfile.write(_list.add_list(['a', 'b', 'c'], ordered=False))

    table = mg.Table()
    outfile.write('\n')
    outfile.write(table.add_row(['English', 'Chinese']))
    outfile.write(table.add_sep_row(cols=2))
    outfile.write(table.add_row(['Apple', '蘋果']))
    outfile.write(table.add_row(['Banana', '香蕉']))
    outfile.write(table.add_row(['Cherry', '櫻桃']))

    outfile.close()