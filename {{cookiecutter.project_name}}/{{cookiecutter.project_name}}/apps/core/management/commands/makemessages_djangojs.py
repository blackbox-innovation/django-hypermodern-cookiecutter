from django.core.management.commands.makemessages import Command as MMCommand


class Command(MMCommand):
    msgmerge_options = ["-q", "--previous", "--no-fuzzy-matching"]

    """ "
    This is a wrapper for the makemessages command and
    it is used to force makemessages call xgettext with the language
    provided as input    The solution is really hacky and takes advantage of the fact
    that in makemessages TranslatableFile process()
    the options in command.xgettext_options are appended to the end
    of the xgettext command.
    """

    def handle(self, *args, **options):
        language = options.get("language")
        self.xgettext_options.append("--language={lang}".format(lang=language))
        super(Command, self).handle(*args, **options)

    def add_arguments(self, parser):
        parser.add_argument(
            "--language", "-lang", default="Python", dest="language", help="Language to be used by xgettext"
        )

        super(Command, self).add_arguments(parser)
