from telethon.sync import TelegramClient

api_id = 0 #Ваш ID
api_hash = '' #Ваш хеш-код

with TelegramClient('name', api_id, api_hash) as client:
    group_name = input('Доброго дня! Введіть назву контакта чи групи: ')
    for i in client.get_dialogs():
        if i.title == group_name:
            dialog = i
            if dialog.is_group or dialog.is_user:
                print('Що ві бажаете зробити?\n\t1:Отримати за назвою групи список її учаників'
        '\n\t2:Відправити повідомлення контакту чи групі')

                match input('Введіть номер бажаної дії: '):
                    case '1':
                        for member in client.get_participants(dialog.title):
                            print(f'Name:{member.first_name} @{member.username}')
                    case '2':
                        client.send_message(dialog.title, input('Ваше повідомлення: '))
                    case _:
                        print('До побачення')