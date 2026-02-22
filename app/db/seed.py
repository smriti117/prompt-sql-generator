import asyncio
from app.db.session import AsyncSessionLocal
from app.db.models import Users


async def seed_users():
    async with AsyncSessionLocal() as session:
        users = [
            Users(name="Alice", email="alice@example.com"),
            Users(name="Bob", email="bob@example.com"),
            Users(name="Charlie", email="charlie@example.com"),
            Users(name="David", email="david@example.com"),
            Users(name="Eve", email="eve@example.com"),
            Users(name="Frank", email="frank@example.com"),
            Users(name="Grace", email="grace@example.com"),
            Users(name="Hannah", email="hannah@example.com"),
            Users(name="Ivy", email="ivy@example.com"),
            Users(name="Jack", email="jack@example.com"),
        ]

        session.add_all(users)
        await session.commit()

    print("Seed data inserted successfully!")


if __name__ == "__main__":
    asyncio.run(seed_users())
