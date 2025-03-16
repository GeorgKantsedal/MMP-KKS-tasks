import asyncio


# імітація асинхронного з'єднання з деякою периферією
async def get_conn(host, port):
    class Conn:
        async def put_data(self):
            print('Надсилання даних...')
            await asyncio.sleep(2)
            print('Дані надіслано.')

        async def get_data(self):
            print('Отримання даних...')
            await asyncio.sleep(2)
            print('Дані отримано.')

        async def close(self):
            print('Завершення зєднання...')
            await asyncio.sleep(2)
            print('Зєднання завершено.')

    print('Встановлюємо зєднання...')
    await asyncio.sleep(2)
    print('Зєднання встановлено.')
    return Conn()


class Connection:
    # цей конструктор буде виконаний у заголовку with
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # цей метод буде неявно виконаний під час входу в with
    async def __aenter__(self):
        self.conn = await get_conn(self.host, self.port)
        return self.conn

    # цей метод буде неявно виконаний під час виходу з with
    async def __aexit__(self, exc_type, exc, tb):
        await self.conn.close()


async def main():
    async with Connection('localhost', 9001) as conn:
        send_task = asyncio.create_task(conn.put_data())
        receive_task = asyncio.create_task(conn.get_data())

        # операції надсилання та отримання даних виконуємо конкурентно
        await send_task
        await receive_task


asyncio.run(main())
