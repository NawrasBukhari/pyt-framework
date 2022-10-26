"""CreateUsersTable Migration."""

from orm.migrations import Migration


class CreateUsersTable(Migration):
    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create("users") as table:
            table.increments("id").primary()
            table.string("name", length=191, nullable=False).unique()
            table.string("email", length=191, nullable=True)
            table.string("password", length=191, nullable=False)
            table.string("remember_token", length=191, nullable=True)
            table.string("role", length=191, nullable=True).default("user")
            table.timestamps()

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop("users")
