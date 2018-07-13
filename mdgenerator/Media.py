class Media(object):
    def add_image(self, link, title_text, alt_text="image"):
        return '![{}]({} "{}")'.format(alt_text, link, title_text)