import sublime, sublime_plugin

import datetime


class InsertIsoDateCommand(sublime_plugin.TextCommand):

    """Prints the current date in ISO format."""

    def run(self, edit):
        isoDate = datetime.date.today().strftime("%Y-%m-%d")

        # Do replacements
        for r in self.view.sel():
            # Insert when sel is empty to not select the contents
            if r.empty():
                self.view.insert (edit, r.a, isoDate)
            else:
                self.view.replace(edit, r,   isoDate)
        # self.view.insert(edit, 0, isoDate)


class InsertIsoTimeCommand(sublime_plugin.TextCommand):

    """Prints the current time in ISO format."""

    def run(self, edit):
        isoTime = datetime.datetime.now().strftime("%H:%M:%S")

        # Do replacements
        for r in self.view.sel():
            # Insert when sel is empty to not select the contents
            if r.empty():
                self.view.insert (edit, r.a, isoTime)
            else:
                self.view.replace(edit, r,   isoTime)


class InsertIsoDateTimeCommand(sublime_plugin.TextCommand):

    """Prints the current date and time in ISO format."""

    def run(self, edit):
        isoDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Do replacements
        for r in self.view.sel():
            # Insert when sel is empty to not select the contents
            if r.empty():
                self.view.insert (edit, r.a, isoDateTime)
            else:
                self.view.replace(edit, r,   isoDateTime)
