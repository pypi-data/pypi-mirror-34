from mistune import Markdown, Renderer


def render(content, extensions):
    renderer = KookiRenderer(extensions)
    markdown = Markdown(renderer=renderer)
    return markdown(content)


class KookiRenderer(Renderer):

    def __init__(self, extensions, **kwargs):
        self.extensions = extensions
        super(KookiRenderer, self).__init__(**kwargs)

    def block_quote(self, text):
        return self.extensions.__block_quote__(renderer=self, text=text)

    def block_html(self, html):
        return self.extensions.__block_html__(renderer=self, html=html)

    def inline_html(self, html):
        return self.extensions.__inline_html__(renderer=self, html=html)

    def header(self, text, level, raw):
        return self.extensions.__header__(renderer=self, text=text, level=level, raw=raw)

    def hrule(self):
        return self.extensions.__hrule__(renderer=self)

    def list(self, body, ordered):
        return self.extensions.__list__(renderer=self, body=body, ordered=ordered)

    def list_item(self, text):
        return self.extensions.__list_item__(renderer=self, text=text)

    def paragraph(self, text):
        return '{}\n\n'.format(self.extensions.__paragraph__(renderer=self, text=text))

    def table(self, header, body):
        return self.extensions.__table__(renderer=self, header=header, body=body)

    def table_row(self, content):
        return self.extensions.__table_row__(renderer=self, content=content, placeholder=False)

    def table_cell(self, content, **flags):
        return self.extensions.__table_cell__(renderer=self, content=content, placeholder=False, **flags)

    def link(self, link, title, content):
        return self.extensions.__link__(renderer=self, link=link, title=title, content=content)

    def autolink(self, link, is_email=False):
        return self.extensions.__autolink__(renderer=self, link=link, is_email=is_email)

    def block_code(self, code, language):
        return self.extensions.__block_code__(renderer=self, code=code, language=language)

    def codespan(self, text):
        return self.extensions.__codespan__(renderer=self, text=text)

    def double_emphasis(self, text):
        return self.extensions.__double_emphasis__(renderer=self, text=text)

    def emphasis(self, text):
        return self.extensions.__emphasis__(renderer=self, text=text)

    def image(self, src, title, alt_text):
        return self.extensions.__image__(renderer=self, src=src, title=title, alt_text=alt_text)

    def strikethrough(self, text):
        return self.extensions.__strikethrough__(renderer=self, text=text)

    def text(self, text):
        return self.extensions.__text__(renderer=self, text=text)

    def linebreak(self):
        return self.extensions.__linebreak__(renderer=self)

    def newline(self):
        return self.extensions.__newline__(renderer=self)

    def footnote_ref(self, key, index):
        return self.extensions.__footnote_ref__(renderer=self, key=key, index=index)

    def footnote_item(self, key, text):
        return self.extensions.__footnote_item__(renderer=self, key=key, text=text)

    def footnotes(self, text):
        return self.extensions.__footnotes__(renderer=self, text=text)
