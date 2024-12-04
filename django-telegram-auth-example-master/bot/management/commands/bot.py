# async def start(update: Update, context: CallbackContext) -> None:
#     user_id = update.effective_user.id
#     try:
#         user_data = await sync_to_async(UserData.objects.get)(id=user_id)
#         await update.message.reply_text(f'Welcome back {user_data.first_name}!')
#     except UserData.DoesNotExist:
#         new_user = UserData(id=user_id, first_name=update.effective_user.first_name, last_name=update.effective_user.last_name, username=update.effective_user.username)
#         await sync_to_async(new_user.save)()
#         logging.info(f'New user {new_user.first_name} has been added to the database')
#         await update.message.reply_text('Welcome to django-telegram-bot!')
SOCIAL_AUTH_TELEGRAM_BOT_TOKEN='7669051527:AAHLXw5aQSVJJfdL2iiPuQlvrT6jZx6nAzU'
from django.core.management.base import BaseCommand
from telegram import Bot, Update
from django.contrib.auth import authenticate
from telegram.ext import CommandHandler, CallbackContext, Updater


class Command(BaseCommand):
    help = 'Starts the Telegram bot'
    
    def handle(self, *args, **kwargs):
        from telegram.ext import Application

        application = Application.builder().token(SOCIAL_AUTH_TELEGRAM_BOT_TOKEN).build()   
        
        # telegram_login_widget = create_redirect_login_widget(
                # redirect_url, bot_name, size=LARGE, user_photo=DISABLE_USER_PHOTO)

        async def start(update: Update, context: CallbackContext):
        #    telegram_login_widget = create_callback_login_widget(bot_name, size=SMALL)
        #    def _generate_widget_parameters(bot_name, user_photo, size, corner_radius, access_write):
        #         """
        #         Generate common widget embed code parameters.
        #         """
        #         user_photo_bool = str(user_photo).lower()

        #         data_telegram_login = 'data-telegram-login="{}" '.format(bot_name)
        #         data_size = 'data-size="{}" '.format(size)
        #         data_userpic = 'data-userpic="{}" '.format(user_photo_bool) if not user_photo else ''
        #         data_radius = 'data-radius="{}" '.format(corner_radius) if corner_radius else ''
        #         data_request_access = 'data-request-access="write"' if access_write else ''


        #    user = authenticate(user=user, password=user.password)
           await update.message.reply_text('Hello! I  lam your bot.')
        
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)

        application.run_polling()
           