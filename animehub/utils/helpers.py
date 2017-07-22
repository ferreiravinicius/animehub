from flask import request, url_for

def url_red(endpoint=None, **kwargs):
    """
    Gera uma url para o argumento `next` do request ou
    para um `endpoint` especificado nos argumentos ou
    url pra home (`main.home`)
    """
    return url_for(endpoint, **kwargs) or \
           url_for('main.home') or \
           request.args.get('next')
