import pytest

from src.calc_y_axis import calc_y_axis


test_datas = [
    ([256], 1, 128),  # 1行のケース
    ([109, 94], 1, 54),  # 2行のケース 1行目
    ([109, 94], 2, 156),  # 2行のケース 2行目
    ([98, 145, 146], 1, 49),  # 3行のケース 1行目
    ([98, 145, 146], 2, 170),  # 3行のケース 2行目
    ([98, 145, 146], 3, 316),  # 3行のケース 3行目
]


@pytest.mark.parametrize("bounding_bottoms, count, results", test_datas)
def test_calc_y_axis(bounding_bottoms, count, results):
    assert calc_y_axis(bounding_bottoms, count) == results
