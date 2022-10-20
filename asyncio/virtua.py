import asyncio

import aiofiles
from aiohttp import ClientSession
from eth_account import Account
from fake_useragent import FakeUserAgent as ua
from loguru import logger

import config

import random
from random import choice
from string import ascii_lowercase


def get_headers():
    return config.HEADERS.copy()


def get_random_twitter():
    return "".join(choice(ascii_lowercase) for i in range(8))


def get_random_mail():
    return f'{"".join(choice(ascii_lowercase) for i in range(8))}@gmail.com'

def get_random_refer():
    with open("refer.txt") as file:
        lines = file.readlines()
    return random.choice(lines).strip()


async def join_whitelist(worker: str) -> None:
    while True:
        account = Account.create("KEYSMASH FJAFJKLDSKF7JKFDJ 1530")
        public_key = account.address

        headers = get_headers()
        headers["User-Agent"] = ua().random

        async with ClientSession(headers=headers) as session:
            resp = await session.post(
                "https://audience-consumer-api.zootools.co/v1/lists/vVGRjdIyHpU1eOCI83x6/members",
                json={
                    "cryptoAddress": public_key,
                    "email": get_random_mail(),
                    "referral": get_random_refer(),  
                    "twitter": get_random_twitter(),
                },
            )

        if resp.status == 200:
            logger.success(f"{worker} {public_key[:7]}... - successfully registered!")
        else:
            logger.error(f"{worker} - {public_key[:7]}... - {await resp.text()}")
            continue

        async with aiofiles.open("accounts.txt", "a+") as f:
            await f.write(f"{account.key.hex()}|{public_key}\n")


async def main():
    await asyncio.gather(
        *[
            asyncio.create_task(join_whitelist(f"Worker {i+1}"))
            for i in range(config.THREADS)
        ]
    )
