#!/usr/bin/env python3

import asyncio

from pyasic import get_miner


async def gather_miner_data():
    miner = await get_miner("192.168.11.160")
    if miner is not None:
        miner_data = await miner.get_data()
        # print(json.dumps(miner_data))  # all data from the dataclass
        # print(json.dumps(miner_data.hashrate))  # hashrate of the miner in TH/s
        print(miner_data.json())


if __name__ == "__main__":
    asyncio.run(gather_miner_data())

## Run Output

# {
#     "ip": "192.168.11.160",
#     "device_info": {
#         "make": "AvalonMiner",
#         "model": "Avalon Nano 3",
#         "firmware": "Stock",
#         "algo": "SHA256"
#     },
#     "mac": null,
#     "api_ver": "3.7",
#     "fw_ver": "4.11.1",
#     "hostname": null,
#     "expected_hashrate": 4.11272,
#     "expected_hashboards": 1,
#     "expected_chips": 10,
#     "expected_fans": 1,
#     "env_temp": 62.0,
#     "wattage": null,
#     "voltage": null,
#     "fans": [
#         {
#             "speed": 4800
#         }
#     ],
#     "fan_psu": null,
#     "hashboards": [
#         {
#             "slot": 0,
#             "hashrate": 3.66148,
#             "temp": 90.0,
#             "chip_temp": 93.0,
#             "chips": 10,
#             "expected_chips": 10,
#             "serial_number": null,
#             "missing": false,
#             "tuned": null,
#             "active": null,
#             "voltage": null
#         }
#     ],
#     "config": {
#         "pools": {
#             "groups": [
#                 {
#                     "pools": [
#                         {
#                             "url": "stratum+tcp://btc.global.luxor.tech:700",
#                             "user": "avalon33.jasonhome",
#                             "password": "x"
#                         },
#                         {
#                             "url": "stratum+tcp://btc.global.luxor.tech:700",
#                             "user": "avalon33.jasonhome",
#                             "password": "x"
#                         },
#                         {
#                             "url": "stratum+tcp://btc.global.luxor.tech:700",
#                             "user": "avalon33.jasonhome",
#                             "password": "x"
#                         }
#                     ],
#                     "quota": 1,
#                     "name": null
#                 }
#             ]
#         },
#         "fan_mode": {
#             "mode": "normal",
#             "minimum_fans": 1,
#             "minimum_speed": 0
#         },
#         "temperature": {
#             "target": null,
#             "hot": null,
#             "danger": null
#         },
#         "mining_mode": {
#             "mode": "normal"
#         }
#     },
#     "fault_light": false,
#     "errors": [],
#     "is_mining": true,
#     "uptime": 174687,
#     "pools": [
#         {
#             "url": "stratum+tcp://btc.global.luxor.tech:700",
#             "accepted": 8936,
#             "rejected": 31,
#             "get_failures": 2,
#             "remote_failures": 0,
#             "active": true,
#             "alive": true,
#             "index": 0,
#             "user": "avalon33.jasonhome",
#             "pool_rejected_percent": 0.34571205531392885,
#             "pool_stale_percent": 0.02230400356864057
#         },
#         {
#             "url": "stratum+tcp://btc.global.luxor.tech:700",
#             "accepted": 0,
#             "rejected": 0,
#             "get_failures": 0,
#             "remote_failures": 0,
#             "active": false,
#             "alive": true,
#             "index": 1,
#             "user": "avalon33.jasonhome",
#             "pool_rejected_percent": 0.0,
#             "pool_stale_percent": 0.0
#         },
#         {
#             "url": "stratum+tcp://btc.global.luxor.tech:700",
#             "accepted": 0,
#             "rejected": 0,
#             "get_failures": 0,
#             "remote_failures": 0,
#             "active": false,
#             "alive": true,
#             "index": 2,
#             "user": "avalon33.jasonhome",
#             "pool_rejected_percent": 0.0,
#             "pool_stale_percent": 0.0
#         }
#     ],
#     "hashrate": 3.66148,
#     "wattage_limit": 125,
#     "total_chips": 10,
#     "nominal": true,
#     "percent_expected_chips": 100,
#     "percent_expected_hashrate": 89,
#     "percent_expected_wattage": null,
#     "temperature_avg": 90,
#     "efficiency": null,
#     "datetime": "2024-12-18T12:01:38.930777+08:00",
#     "timestamp": 1734494498,
#     "make": "AvalonMiner",
#     "model": "Avalon Nano 3",
#     "firmware": "Stock",
#     "algo": "SHA256"
# }
