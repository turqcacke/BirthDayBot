from aiogram.utils.callback_data import CallbackData

delete_user_callback = CallbackData('delete_user', 'db_info_id', 'last_start_id')
detail_user_callback = CallbackData('detail_user', 'db_info_id', 'last_start_id')
pagination_callback = CallbackData('pagination', 'start_id')
close_callback = CallbackData('close', 'close')
