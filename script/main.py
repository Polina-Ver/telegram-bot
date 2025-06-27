import asyncio
from classes import CodewarsLogic

async def main():
    logic = CodewarsLogic()
    tasks = await logic.parse_and_store
    print("Parsed tasks:", tasks)

if __name__ == "__main__":
    asyncio.run(main())
