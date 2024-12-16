#!/usr/bin/env python3

import asyncio  # asyncio for handling the async part
from pyasic import get_miner  # handles miner creation


async def get_miners():  # define async scan function to allow awaiting
    # get the miner with the miner factory
    # the miner factory is a singleton, and will always use the same object and cache
    # this means you can always call it as MinerFactory().get_miner(), or just get_miner()
    miner_1 = await get_miner("192.168.11.160")
    print(miner_1)


if __name__ == "__main__":
    asyncio.run(get_miners())  # get the miners asynchronously with asyncio.run()

# run outputs

# $ ./get_miner.py
# Avalon Nano 3 (Stock): 192.168.11.160
# (pyasic-demo-py3.12)
