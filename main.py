"""Main"""
# コードスタイルチェックが可能
# VSCodeのpython.lintingで設定も可能
# 記載順に厳しいチェックになっている
# pycodestyle main.py
# flake8 main.py
# pylint main.py
import roboter.controller.conversation


def main():
    """main"""
    roboter.controller.conversation.talk_about_restaurant()


if __name__ == '__main__':
    main()
