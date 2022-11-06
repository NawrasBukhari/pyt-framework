"""Craft Command.

This module is really used for backup only if the masonite CLI cannot import this for you.
This can be used by running "python craft". This module is not ran when the CLI can
successfully import commands for you.
"""
from . import (
    MakeModelDocstringCommand as MakeModelDocstring,
    MigrateRollbackCommand as MigrateRollback,
    MigrateRefreshCommand as MigrateRefresh,
    MakeMigrationCommand as MakeMigration,
    MigrateStatusCommand as MigrateStatus,
    MakeObserverCommand as MakeObserver,
    MigrateResetCommand as MigrateReset,
    GenerateKeyCommand as GenerateKey,
    MakeModelCommand as MakeModel,
    MakeSeedCommand as MakeSeed,
    MigrateCommand as Migrate,
    SeedRunCommand as SeedRun,
    ShellCommand as Shell,
)

from cleo import Application

application = Application("ORM:", str(0.1))

application.add(MakeModelDocstring())
application.add(MigrateRollback())
application.add(MigrateRefresh())
application.add(MakeMigration())
application.add(MigrateStatus())
application.add(MakeObserver())
application.add(MigrateReset())
application.add(MakeModel())
application.add(GenerateKey())
application.add(MakeSeed())
application.add(Migrate())
application.add(SeedRun())
application.add(Shell())

if __name__ == "__main__":
    application.run()
