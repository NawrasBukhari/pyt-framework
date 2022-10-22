"""Wizard Command.

This module contains the commands for the wizard helper.
use this file to generate migrations and models.
and many more things!
Enjoy the code!!
"""

from cleo import Application
from masoniteorm.commands import (
    MigrateCommand as Migrate,
    MigrateRollbackCommand as MigrateRollback,
    MigrateRefreshCommand as MigrateRefresh,
    MakeMigrationCommand as MakeMigration,
    MakeObserverCommand as MakeObserver,
    MakeModelCommand as MakeModel,
    MigrateStatusCommand as MigrateStatus,
    MigrateResetCommand as MigrateReset,
    MakeSeedCommand as MakeSeed,
    MakeModelDocstringCommand as MakeModelDocstring,
    SeedRunCommand as SeedRun,
)

application = Application(name="Wizard Version:", version="1.0.0")

application.add(Migrate())
application.add(MigrateRollback())
application.add(MigrateRefresh())
application.add(MakeMigration())
application.add(MakeObserver())
application.add(MakeModel())
application.add(MigrateStatus())
application.add(MigrateReset())
application.add(MakeSeed())
application.add(MakeModelDocstring())
application.add(SeedRun())

if __name__ == "__main__":
    application.run()
