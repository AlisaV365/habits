from telebot import TeleBot
from celery import shared_task

@shared_task
def habits_notification(object_pk):
   # Получите привычку на основе object_pk
   habit = получить_привычку(object_pk)
   habit_act, habit_time, habit_place = получить_детали_привычки(habit)

   bot = TeleBot('6686791128:AAHxQRTi36OKijSyzMACSAHu4hI_jGjFQY8')
   message = f'Трекер привычек напоминает: требуется совершить {habit_act} в {habit_time} в {habit_place}'
   bot.send_message(habit.creator.chat_id, message)
