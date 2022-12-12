from telegram.client import Telegram


def create_tg_chat(
    api_id,
    api_hash,
    phone,
    db_encryption_key,
    chat_title='Название чата',
    user_ids=[]
):
    tg = Telegram(
        api_id=api_id,
        api_hash=api_hash,
        phone=phone,
        database_encryption_key=db_encryption_key
    )

    tg.login()

    result = tg.get_chats()
    result.wait()

    params = {
        'title': chat_title,
        'user_ids': user_ids,
    }

    tg.call_method('createNewBasicGroupChat', params=params, block=True)

    tg.stop()
