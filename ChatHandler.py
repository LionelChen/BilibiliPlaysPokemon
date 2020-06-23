import asyncio
import os
import socket

from blivedm import blivedm


class MyBLiveClient(blivedm.BLiveClient):
    # 演示如何自定义handler
    _COMMAND_HANDLERS = blivedm.BLiveClient._COMMAND_HANDLERS.copy()

    async def __on_vip_enter(self, command):
        print(command)
    _COMMAND_HANDLERS['WELCOME'] = __on_vip_enter  # 老爷入场

    async def _on_receive_popularity(self, popularity: int):
        print(f'当前人气值：{popularity}')

    async def _on_receive_danmaku(self, danmaku: blivedm.DanmakuMessage):
        #print(f'{danmaku.uname}：{danmaku.msg}')
        valid_cmd = ["a", "b", "u", "d", "l", "r"]
        if danmaku.msg in valid_cmd:
            # Create a TCP/IP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 50007)
            #print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)

            try:
                message = str.encode(danmaku.msg)
                #print('sending {!r}'.format(message))
                sock.sendall(message)
            finally:
                #print('closing socket')
                sock.close()
        elif danmaku.msg[0] in valid_cmd:
            for each in danmaku.msg:
                if each not in valid_cmd:
                    return;
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Connect the socket to the port where the server is listening
            server_address = ('localhost', 50007)
            # print('connecting to {} port {}'.format(*server_address))
            sock.connect(server_address)

            try:
                message = str.encode(danmaku.msg)
                # print('sending {!r}'.format(message))
                sock.sendall(message)
            finally:
                # print('closing socket')
                sock.close()


    async def _on_receive_gift(self, gift: blivedm.GiftMessage):
        print(f'{gift.uname} 赠送{gift.gift_name}x{gift.num} （{gift.coin_type}币x{gift.total_coin}）')

    async def _on_buy_guard(self, message: blivedm.GuardBuyMessage):
        print(f'{message.username} 购买{message.gift_name}')

    async def _on_super_chat(self, message: blivedm.SuperChatMessage):
        print(f'醒目留言 ¥{message.price} {message.uname}：{message.message}')


async def main():
    # 参数1是直播间ID
    # 如果SSL验证失败就把ssl设为False
    client = MyBLiveClient(8959230, ssl=True)
    future = client.start()
    try:
        # 5秒后停止，测试用
        # await asyncio.sleep(5)
        # future = client.stop()
        # 或者
        # future.cancel()

        await future
    finally:
        await client.close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
