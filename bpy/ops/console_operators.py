class ConsoleOperators:
    def autocomplete(self):
        pass

    def banner(self):
        pass

    def clear(self, scrollback=True, history=False):
        pass

    def clear_line(self):
        pass

    def copy(self):
        pass

    def copy_as_script(self):
        pass

    def delete(self, type='NEXT_CHARACTER'):
        pass

    def execute(self, interactive=False):
        pass

    def history_append(self, text='', current_character=0, remove_duplicates=False):
        pass

    def history_cycle(self, reverse=False):
        pass

    def indent(self):
        pass

    def indent_or_autocomplete(self):
        pass

    def insert(self, text=''):
        pass

    def language(self, language=''):
        pass

    def move(self, type='LINE_BEGIN'):
        pass

    def paste(self, selection=False):
        pass

    def scrollback_append(self, text='', type='OUTPUT'):
        pass

    def select_set(self):
        pass

    def select_word(self):
        pass

    def unindent(self):
        pass
