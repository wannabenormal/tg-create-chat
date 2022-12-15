import json
import argparse
import time

from environs import Env
from telegram.client import Telegram


def create_tg_chat(
    tg,
    chat_title='Название чата',
    user_ids=[]
):
    params = {
        'title': chat_title,
        'user_ids': user_ids,
    }

    tg.call_method('createNewBasicGroupChat', params=params, block=True)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Function to create telegram chat'
    )
    parser.add_argument('path', type=str, help='Path to JSON')
    args = parser.parse_args()

    env = Env()
    env.read_env()
    tg_api_id = env.str('TG_API_ID')
    tg_api_hash = env.str('TG_API_HASH')
    tg_phone = env.str('TG_PHONE')
    db_encryption_key = env.str('DB_ENCRYPTION_KEY')

    tg = Telegram(
        api_id=tg_api_id,
        api_hash=tg_api_hash,
        phone=tg_phone,
        database_encryption_key=db_encryption_key
    )

    tg.login()

    result = tg.get_chats()
    result.wait()

    with open(args.path, 'r') as file:
        groups = json.load(file)

    for index, group in enumerate(groups, start=1):
        create_tg_chat(tg, f'Тестовая группа {index}', group)
        time.sleep(5)
