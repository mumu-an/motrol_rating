from test_api.test import AmaeKoromo, Motrol
import time
import asyncio
from othertool.conredis import AsyncRedisTool
from mytool import logger

async def fetch_tasks_from_redis(redis, task_queue):
    while True:
        task_id = await redis.pop("get_json")
        if not task_id:
            continue
        # 计划执行时间 = 当前时间 + 180秒
        await task_queue.put({
            "task_id": task_id,
            "execute_at": time.time() + 180
        })
        await asyncio.sleep(0.5)


async def scheduler(task_queue, results):
    motrol = Motrol()
    while True:
        now = time.time()
        size = task_queue.qsize()
        for _ in range(size):
            task_id = await task_queue.get()
            if now >= task_id["execute_at"]:
                logger.info(f"开始处理 {task_id['task_id']}")

                rating = motrol.get_rating(task_id['task_id']["agent"], task_id['task_id']["cookie"], task_id['task_id']["task_id"])
                if rating:
                    results[task_id['task_id']['result_key']][task_id['task_id']['paipu']] = rating
                    continue
            await task_queue.put(task_id)
        await asyncio.sleep(1)


async def run():
    task_queue = asyncio.Queue()
    results = {}

    redis = AsyncRedisTool(db=8)
    asyncio.create_task(fetch_tasks_from_redis(redis, task_queue))
    asyncio.create_task(scheduler(task_queue, results))

    user_name = "小诗乃"
    user_count = 20
    mode = "16,12"
    dict = {
        "金": "8",
        "玉": "12",
        "王": "16",
    }
    if mode in dict.keys():
        mode = dict[mode]

    amae = AmaeKoromo()
    user_id = amae.search_player_id(user_name)
    if not user_count:
        user_count = amae.search_player_msg(user_id, mode)
    logger.info(f"查询数量：{user_count}")
    logger.info(f'开始时间：{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))}')
    user_motrol_id = amae.get_motroplayid(user_id)
    user_uuids_dict = amae.get_historydata(player_id=user_id, limit=user_count, mode=mode)
    results[f"{user_id}_{user_count}"] = {}
    for i in user_uuids_dict.keys():
        paipu = f"{i}_a{user_motrol_id}"
        results[f"{user_id}_{user_count}"][paipu] = None
        await redis.push("get_task", {"paipu": paipu, "result_key": f"{user_id}_{user_count}"})


    processed_tasks = set()
    while True:
        await asyncio.sleep(1)  # 每5秒检查一次
        for task_id, uid_dict in results.items():
            # 判断任务是否全部完成且还没处理过
            if task_id not in processed_tasks and all(r is not None for r in uid_dict.values()):
                # 执行后续处理，比如写文件或打印
                logger.info(f"任务 {task_id} 全部完成，结果：{uid_dict}")
                if uid_dict:  # 确保不为空
                    avg_rating = sum(uid_dict.values()) / len(uid_dict)
                    logger.info(f"任务 {task_id} 全部完成，平均值：{avg_rating*100:.2f}")
                    logger.info(time.time())
                # 标记为已处理
                processed_tasks.add(task_id)


if __name__ == '__main__':
    asyncio.run(run())
