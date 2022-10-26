from orm.commands.CanOverrideConfig import CanOverrideConfig
from orm.commands.CanOverrideOptionsDefault import CanOverrideOptionsDefault


class Command(CanOverrideOptionsDefault, CanOverrideConfig):
    pass
