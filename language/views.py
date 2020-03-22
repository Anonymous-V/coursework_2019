from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from .forms import AddLanguage
from django.core import management
from django.conf.global_settings import LANGUAGES
import os


@user_passes_test(lambda u: u.is_superuser)
def add_language(request):
    # Проверить, что язык является стандартным для Django
    print('ady' in [x[0] for x in LANGUAGES])

    if request.method == 'POST':
        form = AddLanguage(request.POST)
        if form.is_valid():
            new_lang = form.cleaned_data
            path = os.getcwd() + '\cousework\settings_language.py'


            try:
                os.mkdir(os.getcwd() + '\locale\\' + new_lang['code'])
            except OSError:
                pass

            f = open(path, 'r', encoding='utf-8')
            lang = f.readline()
            str = list()
            line = f.readline()
            while line.strip() != ')':
                str.append(line)
                line = f.readline()
            f.close()

            f = open(path, 'w', encoding='utf-8')
            f.write(lang)
            f.write(''.join(str))
            f.write("    ('{}', '{}'),\n".format(new_lang['code'], new_lang['language']))
            f.write(")")
            f.close()

            if new_lang['code'] not in [x[0] for x in LANGUAGES]:
                path = os.getcwd() + '\cousework\settings_language_extra.py'
                f = open(path, 'r', encoding='utf-8')
                str = list()
                line = f.readline()

                while line.strip() != '}':
                    str.append(line)
                    line = f.readline()
                f.close()

                print(''.join(str))

                structure = "    '" + new_lang['code'] + "': {\n" + \
                            "        'bidi': False,\n" \
                            "        'code': '{code}',\n" \
                            "        'name': '{lang}',\n" \
                            "        'name_local': u'{lang}',\n".format(
                                code=new_lang['code'], lang=new_lang['language']
                            ) + "    },\n}"

                f = open(path, 'w', encoding='utf-8')
                f.write(''.join(str))
                f.write(structure)
                f.close()

            # options = {}
            # options['ignore'] = 'myvenv'
            # management.call_command('makemessages', **options)
            management.call_command('makemessages')

            return redirect(reverse('index_page'))

    else:
        form = AddLanguage()

    return render(request, 'language/temp.html', {'form': form})


    # f = open(os.getcwd() + '\cousework\settings_language.py', 'r', encoding='utf-8')
    # str = list()
    #
    # # Считывание кодов и языков
    # lang = f.readline()
    # variable = f.readline()
    # while (variable != ')'):
    #     str.append(variable)
    #     variable = f.readline()
    # f.close()
    #
    # f2 = open(os.getcwd() + '\cousework\settings_language2.py', 'w', encoding='utf-8')
    #
    # f2.write(lang)
    # for ls in str:
    #     f2.write(ls)
    # f2.write("    ('ua', 'Украина'),\n")
    # f2.write(')')
    # f2.close()
    #
    # # Извлечение кода и названия языка
    # lst = str.pop(1)
    # dt = dict()
    #
    # inx = lst.index("'") + 1
    # inx2 = lst.index("'", inx + 1)
    # code = lst[inx : inx2]
    #
    # inx = lst.index("'", inx2 + 1) + 1
    # inx2 = lst.index("'", inx + 1)
    # language = lst[inx : inx2]
    #
    # dt[code] = language
    # dt[code + '1'] = language
    # dt[code + '2'] = language

    # return HttpResponse(dt.items())
    # return render(request, 'language/temp.html', {'dt': dt})