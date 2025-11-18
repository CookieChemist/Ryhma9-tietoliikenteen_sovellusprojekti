import asyncio
from bleak import BleakClient

async def main():
    ble_address = "D2:3F:48:D1:2D:F5"

    async with BleakClient(ble_address) as client:
        # we’ll do the read/write operations here
        print("Connected to BLE device")
        print(client.is_connected)

asyncio.run(main())