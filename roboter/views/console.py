"""コンソール出力用テンプレート取得"""
import os
import string

import termcolor

from roboter.utils import logger


def get_template_dir_path():
    """ テンプレート格納パスを返却
    settings.pyにて指定がなければデフォルトパスを利用

    Returns:
        str: テンプレートパス
    """
    template_dir_path = None
    try:
        import settings
        if settings.TEMPLATE_PATH:
            template_dir_path = settings.TEMPLATE_PATH
    except ImportError:
        pass

    if not template_dir_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_dir_path = os.path.join(base_dir, 'templates')
    return template_dir_path


class NoTemplateError(Exception):
    """テンプレート不在エラー"""


def find_tempalte(temp_file):
    """テンプレート取得

    Args:
        temp_file (str): テンプレート名
    
    Returns:
        str: テンプレートパス
    
    Raises:
        NoTemplateError: テンプレート不在時
    """
    template_dir_path = get_template_dir_path()
    logger.debug('TEMPALE DIRECTORY : {}'.format(template_dir_path))
    temp_file_path = os.path.join(template_dir_path, temp_file)
    if not os.path.exists(temp_file_path):
        raise NoTemplateError('Could not find {}'.format(temp_file))
    return temp_file_path


def get_template(tempalte_file_path, color=None):
    """テンプレート取得

    Args:
        tempalte_file_path (str): テンプレートのファイルパス
        color (str, optional): カラーフォーマット. Defaults to None.
    
    Returns:
        string.Template: テンプレート
    """
    template = find_tempalte(tempalte_file_path)
    with open(template, 'r', encoding='utf-8') as template_file:
        contents = template_file.read()
        contents = contents.rstrip(os.linesep)
        contents = '{splitter}{sep}{contents}{sep}{splitter}{sep}'.format(
            contents=contents, splitter='=' * 60, sep=os.linesep
        )
        contents = termcolor.colored(contents, color)
        return string.Template(contents)
        