"""RankingModel"""

import csv
import collections
import os
import pathlib

from roboter.utils import logger


RANKING_COLUMN_NAME = 'NAME'
RANKING_COLUMN_COUNT = 'COUNT'
RANKING_CSV_FILE_PATH = 'ranking.csv'


class CsvModel(object):
    """Base CSV Model"""
    def __init__(self, csv_file):
        self.csv_file = csv_file
        if not os.path.exists(csv_file):
            logger.debug('make CSV')
            pathlib.Path(csv_file).touch()


class RankingModel(CsvModel):
    """RankingModel"""
    def __init__(self, csv_file=None, *args, **kwargs):
        if not csv_file:
            csv_file = self.get_csv_file_path()
        logger.debug('CSV FILE NAME : {}'.format(csv_file))
        super().__init__(csv_file, *args, **kwargs)
        self.column = [RANKING_COLUMN_NAME, RANKING_COLUMN_COUNT]
        self.data = collections.defaultdict(int)
        self.load_data()

    def get_csv_file_path(self):
        """CSVファイル取得"""
        csv_file_path = None
        try:
            import settings
            if settings.CSV_FILE_PATH:
                csv_file_path = settings.CSV_FILE_PATH
        except ImportError:
            pass

        if not csv_file_path:
            csv_file_path = RANKING_CSV_FILE_PATH

        return csv_file_path

    def load_data(self):
        """データ読み込み

        Returns:
            dict: ランキングデータ
        """
        with open(self.csv_file, 'r+') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.data[row[RANKING_COLUMN_NAME]] = int(
                    row[RANKING_COLUMN_COUNT])
        return self.data

    def save(self):
        """データ保存"""
        with open(self.csv_file, 'w+') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.column)
            writer.writeheader()

            # モデル内に保持しているデータをCSVに出力
            for name, count in self.data.items():
                writer.writerow({
                    RANKING_COLUMN_NAME: name,
                    RANKING_COLUMN_COUNT: count
                })

    def get_most_popular(self, not_list=None):
        """最も人気のあるデータを取得する

        Args:
            not_list (list): 除外リスト

        Returns:
            str: 最も人気のあるデータ
        """
        if not_list is None:
            not_list = []

        if not self.data:
            return None

        sorted_data = sorted(self.data, key=self.data.get, reverse=True)
        for name in sorted_data:
            if name in not_list:
                continue
            return name

    def increment(self, name):
        """ランキング値追加
        Args:
            name (str): データキー
        """
        self.data[name.title()] += 1
        self.save()
