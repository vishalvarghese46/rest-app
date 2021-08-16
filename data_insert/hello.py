import asyncpg
import asyncio
 
async def main():
    connection = await asyncpg.connect(host='127.0.0.1',
                                       port=5432,
                                       user='root',
                                       database='postgres',
                                       password='root')
    version = connection.get_server_version()
    print(f'Connected! Postgres version is {version}')
    await connection.close()
 
asyncio.run(main())