"""Wizard Commands CLI.

This module contains the commands for the wizard helper.
use this file to generate migrations and models.
and many more things!
Enjoy the code!!

@Author:        Nawras Bukhari
@Description:   This script is used to get the environment variables
@Github:        https://github.com/NawrasBukhari
@Date:          22/Oct/2022
@LastEditors:   Nawras Bukhari
@LastEditTime:  22/Oct/2022
"""

from cleo import Application
from masoniteorm.commands import (
    MakeModelDocstringCommand as MakeModelDocstring,
    MigrateRollbackCommand as MigrateRollback,
    MigrateRefreshCommand as MigrateRefresh,
    MakeMigrationCommand as MakeMigration,
    MigrateStatusCommand as MigrateStatus,
    MakeObserverCommand as MakeObserver,
    MigrateResetCommand as MigrateReset,
    MakeModelCommand as MakeModel,
    MakeSeedCommand as MakeSeed,
    MigrateCommand as Migrate,
    SeedRunCommand as SeedRun,
)

application = Application(name="Wizard Version:", version="1.0.0")

application.add(MakeModelDocstring())
application.add(MigrateRollback())
application.add(MigrateRefresh())
application.add(MakeMigration())
application.add(MigrateStatus())
application.add(MakeObserver())
application.add(MigrateReset())
application.add(MakeModel())
application.add(MakeSeed())
application.add(Migrate())
application.add(SeedRun())

if __name__ == "__main__":
    application.run()
