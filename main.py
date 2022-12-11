from environs import Env
from telegram.client import Telegram


if __name__ == '__main__':
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

    params = {
        'title': 'Тестовый чат',
        'users': ['453039837', '253031461', '217857670'],
    }

    tg.call_method('messages.createChat', params=params)

    tg.idle()
