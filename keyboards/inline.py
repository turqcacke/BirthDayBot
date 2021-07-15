from models import Session, Information
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from .callbakcs import detail_user_callback, pagination_callback, delete_user_callback, close_callback


def inline_persons(pagination: int, start_index: int = 1):
    kb = InlineKeyboardMarkup()
    session = Session()

    first = session.query(Information).first()
    last = session.query(Information).order_by(Information.id.desc()).first()

    results = session.query(Information). \
        where(Information.id >= start_index).limit(pagination).all()
    for person in results:
        person: Information

        kb.add(InlineKeyboardButton(text=f'{person.id} {person.name} {person.surname}({person.day})',
                                    callback_data=detail_user_callback.new(db_info_id=person.id,
                                                                           last_start_id=start_index)))

    if results:
        down_kb = []
        if first not in results:
            back_start_id = session.query(Information)\
                .where(Information.id < start_index).order_by(Information.id.desc()).limit(10).all()[-1]
            back_start_id = back_start_id.id
            down_kb.append(InlineKeyboardButton(text='⬅️',
                                                callback_data=pagination_callback.new(
                                                    start_id=back_start_id,))
                           )

        if last not in results:
            down_kb.append(InlineKeyboardButton(text='➡️',
                                                callback_data=pagination_callback.new(
                                                    start_id=start_index + pagination))
                           )
        kb.row(*down_kb)
    kb.add(InlineKeyboardButton('Close',
                                callback_data=close_callback.new('_'))
           )
    session.close()
    return kb


def inline_options(db_info_id: int, last_start_id: int):
    kb = InlineKeyboardMarkup()
    kb.add(InlineKeyboardButton('Back',
                                callback_data=pagination_callback.new(start_id=last_start_id)))
    kb.add(InlineKeyboardButton('Delete',
                                callback_data=delete_user_callback.new(
                                    db_info_id=db_info_id,
                                    last_start_id=last_start_id
                                )))
