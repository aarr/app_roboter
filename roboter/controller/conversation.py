
from roboter.models import robot
from roboter.utils import logger


def talk_about_restaurant():
    """メイン関数
    """
    logger.debug('---- START ----')
    # Roboter生成
    restaurant_robot = robot.RestaurantRobot()

    # Roboter会話開始
    restaurant_robot.hello()

    # Roboterレストラン評価確認
    restaurant_robot.ask_user_favorite()

    # Roboterお勧めレストラン確認
    restaurant_robot.recommend_restaurant()

    # Roboter会話終了
    restaurant_robot.thank_you()

    logger.debug('---- END ----')
