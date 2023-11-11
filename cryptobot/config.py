

#список доступных языков.в dic_help может быть новый язык,диалоги на котором ещё не доступны, поэтому в этот словарь он не включается
dic_lang = {'/sq':'shqip', '/ru':'русский'}
#диалоги с пользователем на разных языках
dic_help = {'ru':{1:   "правила пользования ботом. отправьте сообщение боту в виде\n"
                        "<имя валюты, цену которой хотите узнать>\n"\
                        "<имя валюты, в которой надо узнать цену первой валюты>\n"\
                        "<количество первой валюты>\n"\
                        "например: биткойн доллар 1\n"\
                        "помощь /help\nсписок доступных валютов /values",
                   2:   "привет, ",
                   3:   {'биткойн':'BTC','эфириум':'ETH','доллар':'USD'},
                   4:   "список доступных валютов:"
                   },
            'sq':{1:   "si perdoret bot. ua dergoni botit nji mesazhe\n"
                        "<valuta çmimin i te ciles doni ta dini>\n"\
                        "<valuta ne te cilin doni te kembini>\n"\
                        "<sasia e valutes se pare>\n"\
                        "per shembull: bitcoin dollar 1\n"\
                        "ndihma /help\nlista e valuteve te arritshme /values",
                   2:   "mirdita, ",
                   3:   {'bitcoin':'BTC','efirium':'ETH','dollar':'USD'},
                   4:   "lista e valuteve te arritshme:"
                   }
            }
#print( dic_help['/sq'][1] )

COMMANDA = list(dic_help.keys())

#cryptocompare.com
