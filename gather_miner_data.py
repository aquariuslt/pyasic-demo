#!/usr/bin/env python3

import asyncio
from pyasic import get_miner


async def gather_miner_data():
    miner = await get_miner("192.168.11.160")
    if miner is not None:
        miner_data = await miner.get_data()
        print(miner_data)  # all data from the dataclass
        print(miner_data.hashrate)  # hashrate of the miner in TH/s


if __name__ == "__main__":
    asyncio.run(gather_miner_data())

# run outputs
# ip = '192.168.11.160'
# device_info = DeviceInfo(
#     make = <MinerMake.AVALONMINER: 'AvalonMiner'>,
# model = <AvalonminerModels.AvalonNano3: 'Avalon Nano 3'>,
# firmware = <MinerFirmware.STOCK: 'Stock'>,
# algo = <class 'pyasic.device.algorithm.sha256.SHA256Algo'>)
# mac = None
# api_ver = '3.7'
# fw_ver = '4.11.1'
# hostname = None
# expected_hashrate = 4.10864 TH/s
# expected_hashboards = 1
# expected_chips = 10
# expected_fans = 1
# env_temp = 59.0
# wattage = None
# voltage = None
# fans = [Fan(speed = 4290)]
# fan_psu = None
# hashboards = [
# HashBoard(
#     slot = 0,
#     hashrate = 3.66217 TH/s,
# temp = 90,
# chip_temp = 92,
# chips = 10,
# expected_chips = 10,
# serial_number = None,
# missing = False,
# tuned = None,
# active = None,
# voltage = None)
# ]
# config = MinerConfig(
# pools = PoolConfig(
#     groups = [
#         PoolGroup(
#             pools = [
#                 Pool(url = 'stratum+tcp://btc.global.luxor.tech:700', user = 'avalon33.jasonhome', password = 'x'),
#                 Pool(url = 'stratum+tcp://btc.global.luxor.tech:700', user = 'avalon33.jasonhome', password = 'x'),
#                 Pool(url = 'stratum+tcp://btc.global.luxor.tech:700', user = 'avalon33.jasonhome', password = 'x')
#             ],
#             quota = 1,
#             name = None
#         )
#     ]
# ),
# fan_mode = FanModeNormal(mode = 'normal', minimum_fans = 1, minimum_speed = 0),
# temperature = TemperatureConfig(target = None, hot = None, danger = None),
# mining_mode = MiningModeNormal(mode = 'normal')
# )
# fault_light = False
# errors = []
# is_mining = True
# uptime = 21777
# pools = [
# PoolMetrics(
#     url = PoolUrl(
#         scheme = <Scheme.STRATUM_V1: 'stratum+tcp'>,
# host = 'btc.global.luxor.tech',
# port = 700,
# pubkey = None
# ),
# accepted = 1097,
# rejected = 1,
# get_failures = 0,
# remote_failures = 0,
# active = True,
# alive = True,
# index = 0,
# user = 'avalon33.jasonhome',
# pool_rejected_percent = 0.09107468123861566,
# pool_stale_percent = 0.0
# ),
# PoolMetrics(
#     url = PoolUrl(
#         scheme = <Scheme.STRATUM_V1: 'stratum+tcp'>,
# host = 'btc.global.luxor.tech',
# port = 700,
# pubkey = None
# ),
# accepted = 0,
# rejected = 0,
# get_failures = 0,
# remote_failures = 0,
# active = False,
# alive = True,
# index = 1,
# user = 'avalon33.jasonhome',
# pool_rejected_percent = 0,
# pool_stale_percent = 0
# ),
# PoolMetrics(
#     url = PoolUrl(
#         scheme = <Scheme.STRATUM_V1: 'stratum+tcp'>,
# host = 'btc.global.luxor.tech',
# port = 700,
# pubkey = None
# ),
# accepted = 0,
# rejected = 0,
# get_failures = 0,
# remote_failures = 0,
# active = False,
# alive = True,
# index = 2,
# user = 'avalon33.jasonhome',
# pool_rejected_percent = 0,
# pool_stale_percent = 0
# )
# ]
# hashrate = 3.66217 TH/s
# wattage_limit = 125
# total_chips = 10
# nominal = True
# percent_expected_chips = 100
# percent_expected_hashrate = 89
# percent_expected_wattage = None
# temperature_avg = 90
# efficiency = None
# datetime = '2024-12-16T17:33:05.989923+08:00'
# timestamp = 1734341585
# make = 'AvalonMiner'
# model = 'Avalon Nano 3'
# firmware = 'Stock'
# algo = 'SHA256'
# unit = 'TH/s'
# rate = 3.66217
