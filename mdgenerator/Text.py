class Text(object):
    def add_heading(self, text, level=1):
        return '{} {}\n'.format(''.ljust(level, '#'), str(text))

    def add_link(self, text, url):
        return '[{}]({})\n'.format(text, url)

    def add_italics(self, text):
        return '*{}*\n'.format(text)

    def add_bold(self, text):
        return '**{}**\n'.format(text)

    def add_emphasis(self, text):
        return '**_{}_**\n'.format(text)

    def add_strikethrough(self, text):
        return '~~{}~~\n'.format(text)

    def add_blockquotes(self, text):
        return '> {}\n'.format(text)

    def add_code(self, text):
        return '`{}`\n'.format(text)

    def add_code_block(self, text):
        return '```{}```\n'.format(text)

    def add_horizon_line(self):
        return '---\n'