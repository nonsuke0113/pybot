import wikipedia

def wikiedia_command(command):
    cmd, keyword = command.split(maxsplit=1)
    wikipedia.set_lang('ja')
    try:
        page = wikipedia.page(keyword)
        title = page.title
        summary = page.summary
        response = page.title
        response = '「{}」ニツイテ。\n{}'.format(title, summary)
    except wikipedia.exceptions.PageError:
        response = '「{}」ノ情報ガ見ツカリマセンデシタ'.format(keyword)
    return response
