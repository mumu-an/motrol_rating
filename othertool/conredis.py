# -*- coding: UTF-8 -*-
import asyncio
import json
import aioredis
import redis
import time


class AsyncRedisTool:
    def __init__(
        self,
        host: str = "127.0.0.1",
        port: int = 6379,
        db: int = 0,
        password: str | None = None,
        url: str | None = None,
    ):
        self.url = (
            url
            or (
                f"redis://:{password}@{host}:{port}/{db}"
                if password
                else f"redis://{host}:{port}/{db}"
            )
        )
        self.redis = None


    async def connect(self):
        if not self.redis:
            self.redis = await aioredis.from_url(self.url, decode_responses=True)

    async def push(self, key: str, value: dict):
        await self.connect()
        await self.redis.rpush(key, json.dumps(value))

    async def push_batch(self, key: str, values: list[dict]):
        if not values:
            return
        await self.connect()

        data = [json.dumps(v) for v in values]
        await self.redis.rpush(key, *data)

    async def push_before(self, key: str, value: dict):
        await self.connect()
        await self.redis.lpush(key, json.dumps(value))

    async def push_batch_before(self, key: str, values: list[dict]):
        if not values:
            return
        await self.connect()

        data = [json.dumps(v) for v in values]
        await self.redis.lpush(key, *data)

    async def delete_batch(self, key: str, values: list[dict], batch_size: int = 1000):
        if not values:
            return

        # 连接 Redis
        await self.connect()

        # 将每个字典转换成 JSON 字符串
        data = [json.dumps(v) for v in values]

        # 使用管道进行批量删除操作
        pipe = self.redis.pipeline()

        # 分批处理，避免一次性删除过多
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]  # 获取当前批次的数据
            for item in batch:
                # 使用管道添加删除命令
                pipe.lrem(key, 0, item)

            # 执行当前批次的删除操作
            await pipe.execute()

            # 你可以在这里添加一些日志或者延时操作来防止 Redis 负载过高
            # await asyncio.sleep(0.1)  # 可选：每批次之间加一点延迟，避免Redis过载

    async def pop(self, key: str, timeout=0):
        await self.connect()
        result = await self.redis.blpop(key, timeout=timeout)
        if result:
            _, msg = result
            return json.loads(msg)
        return None

    async def pop_batch(self, key: str, batch_size=50, wait_time=0):
        await self.connect()

        first = await self.redis.blpop(key)

        if not first:
            return []

        _, msg = first
        results = [json.loads(msg)]

        # =========================
        # 2️⃣ 时间窗口开始
        # =========================
        start = time.time()

        while len(results) < batch_size:
            # 超时判断
            if time.time() - start >= wait_time:
                break

            # 尝试非阻塞取
            msg = await self.redis.lpop(key)

            if not msg:
                # 没数据 → 小睡一下避免空转
                await asyncio.sleep(0.01)
                continue

            results.append(json.loads(msg))

        return results


    async def close(self):
        if self.redis:
            await self.redis.close()



class SyncRedisTool:
    def __init__(self, host="127.0.0.1", port=6379, password=None, db=0):
        self.redis = redis.Redis(
            host=host,
            port=port,
            password=password,
            db=db,
            decode_responses=True
        )

    def push(self, key: str, value: dict):
        self.redis.rpush(key, json.dumps(value))

    def pop(self, key: str, timeout=0):
        result = self.redis.blpop(key, timeout=timeout)
        if result:
            _, msg = result
            return json.loads(msg)
        return None

if __name__ == "__main__":
    myredis = AsyncRedisTool(db=1)
    asyncio.run(myredis.connect())
    # keys = asyncio.run(myredis.redis.keys())
    asyncio.run(myredis.close())
    print(1)