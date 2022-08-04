from parser import Signal
from telethon import TelegramClient, events
import yaml
import sys
import asyncio
import json

with open("./config/config.yml", "r") as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.SafeLoader)

api_id = cfg['telethon']['api_id']
api_hash = cfg['telethon']['api_hash']
client = TelegramClient(cfg['telethon']['app_title'], api_id, api_hash)

channels = []
signals_on = False

async def async_input(prompt):
    print(prompt, end='', flush=True)
    return (await asyncio.get_running_loop().run_in_executor(None, sys.stdin.readline)).rstrip()

@client.on(events.NewMessage(outgoing=True, incoming=True))
async def handler(event):
    if signals_on == True and any([obj.get('id') == event.chat_id for obj in channels['channels']]):
        signal = Signal(event.text)
        signal.parse_signal()
        if signal.is_valid:
            print(json.dumps(signal.to_json(), indent=4))

async def load_channels():
    with open('config/channels.json', 'r') as f:
        global channels
        try:
            channels = json.load(f)
        except:
            channels = {}
            channels['channels'] = []

    number = 1
    async for dialog in client.iter_dialogs():
        channel_id = dialog.id
        channel_title = dialog.title

        if channel_title == "" or channel_id > 0:
            continue
        if any([obj.get('id') == channel_id for obj in channels['channels']]):
            continue

        channel = {
            "id": channel_id,
            "data": {
                "title": dialog.title,
                "selection_number": number,
                "enabled": False
                }
            }

        channels['channels'].append(channel)
        number += 1

    json_channels = json.dumps(channels, indent=4)
    with open('config/channels.json', 'w') as outfile:
        outfile.write(json_channels)


async def main():

    await load_channels()
    while True:
        selection = await async_input("Select an option:\n\n"
            + "1. Configure channels\n"
            + "2. Listen for signals\n"
            + "3. Exit\n")
        if selection == '1':
            with open('config/channels.json', mode= 'r') as f:
                data = f.read()
                channels = json.loads(data)
                for channel in channels['channels']:
                    out = f"{channel['data']['selection_number']} - {channel['data']['title']}"
                    if channel['data']['enabled'] == True:
                        print(out, " ENABLED")
                    else:
                        print(out, " DISABLED")

                command = await async_input("\nType a number to toggle a channel or "
                + "'break' to return to the menu\n\n")
                if command == 'break':
                    print('\n')
                    continue
                else:
                    for channel in channels['channels']:
                        if channel.get('data').get('selection_number') == int(command):
                            if channel['data']['enabled'] == True:
                                channel['data']['enabled'] = False
                            else:
                                channel['data']['enabled'] = True
                            f.close()
                            json_channels = json.dumps(channels, indent=4)
                            with open('config/channels.json', 'w') as outfile:
                                outfile.write(json_channels)
                                outfile.close()
                    continue
        if selection == "2":
            print("Listening for signals, ")
            global signals_on
            signals_on = True
            command = await async_input("type 'break' to stop listeing\n\n")
            if command == "break":
                signals_on = False
        else:
            await client.disconnect()
            return

with client:
    client.start()
    client.loop.create_task(main())
    client.run_until_disconnected()
"""
Main method.

Runs on startup
"""
    # directory = 'test_signals'

    # # iterate through example signals
    # for filename in os.listdir(directory):
    #     filename = os.path.join(directory, filename)

    #     with open(filename, 'r') as f:
    #         # convert each signal to an object using the parser.Signal class.
    #         signal = Signal(f.read())
    #         signal.parse_signal()
    #         print(signal.to_json())



