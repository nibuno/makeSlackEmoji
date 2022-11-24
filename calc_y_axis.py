# -*- coding: utf-8 -*-

def calc_y_axis(bounding_boxs, count) -> int:
    """Y軸の描画位置を取得する

    境界ボックスの位置を利用して各出力位置の中心を取得する

    以下計算結果のイメージ:
    count: 1 bounding_boxs[0] / 2
    count: 2 bounding_boxs[0] + (bounding_boxs[1] / 2)
    count: 3 bounding_boxs[0] + bounding_boxs[1] + (bounding_boxs[2] / 2)

    :param bounding_boxs: 境界ボックス
    :param count: カウント
    :return: 描画位置
    """
    results = []
    for i in range(count):
        if i == count - 1:
            results.append(bounding_boxs[i] / 2)
        else:
            results.append(bounding_boxs[i])
    return int(sum(results))
