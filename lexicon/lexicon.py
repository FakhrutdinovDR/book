MENU_COMMANDS: dict[str, str] = {'/start': 'Начать работу с ботом',
                                 '/help': 'Справка по работе бота',
                                 '/continue': 'Продолжить чтение',
                                 '/bookmarks': 'Посмотреть список закладок',
                                 '/beginning': 'Перейти в начало книги'}

BOOKMARK_COMMANDS = {'edit_bookmarks': 'РЕДАКТИРОВАТЬ',
                     'cancel': 'ОТМЕНИТЬ',}

ANSWER_MENU_COMMANDS: dict[str, str] = {'/start': 'Привет, читатель!\n'
                                          '\n'
                                          'Это бот, в котором ты можешь причтать книгу '
                                          'Михаила Булгакова: Мастер и Маргарита\n'
                                          '\n'
                                          'Чтобы посмотреть список доступных команд нажми /help',
                                 '/help': 'Это бот-читалка:\n'
                                         '\n'
                                         'Доступные команды:\n'
                                         '\n'
                                         f'/beginning - {MENU_COMMANDS["/beginning"]}\n'
                                         f'/continue - {MENU_COMMANDS["/continue"]}\n'
                                         f'/bookmarks - {MENU_COMMANDS["/bookmarks"]}\n'
                                         f'/help - {MENU_COMMANDS["/help"]}\n'
                                         '\n'
                                         'Чтобы сохранить закладку нажми на кнопку с номером страницы\n'
                                         '\n'
                                         'Приятного чтения!'}

LEXICON_PAGE_BUTTONS: dict[str, str] = {'backward': '<<',
                                        'forward': '>>'}

OTHER_ANS: dict[str, str] = {'other': 'Я могу только дать прочитать тебе книгу, и дать инструкции /help'}

