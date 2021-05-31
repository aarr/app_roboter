# setup.py
# パッケージングする際に利用する。下記でtar.gzを作成可能
# distフォルダに作成されたパッケージが配置される
# sdist形式
# python setup.py sdist
#
# bdist形式（事前にwheelのインストールが必要）
# python setyp.py bdist_wheel

# setuptoolsが存在しない場合、distutilsからインポートする
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='roboter',
    version='0.1',
    description='Roboter',
    url='https://github.com/todo',
    author='dev',
    author_email='dev@address.com',
    license='FREE',
    # setuptoolsを利用する場合、便利な機能が追加されているので利用可能
    # 必要パッケージのインストール
    # アプリインストール時に必要なパッケージをインストールしてくれる。依存関係解決
    #install_required = ['termcolor==1.0.0', 'logging'=='*'],
    # パッケージの自動追加
    #packages=find_packages(),
    packages=[
        "roboter",
        "roboter.models",
        "roboter.controller",
        "roboter.views",
        "roboter.utils"
    ],
    # パッケージを利用する際に必要なファイル
    # パッケージに含めるには、package_dataで定義する
    package_data={'roboter' : ['templates/*.txt']}
)
