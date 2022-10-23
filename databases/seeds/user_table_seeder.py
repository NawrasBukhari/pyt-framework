"""UserTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.User import User
from config.security import hash_password


class UserTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        User.create(
            name="admin",
            email="user@pyt.com",
            password=hash_password("password"),
            role="user",
        )
