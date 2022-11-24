from main import MakeSlackEmoji


class TestMakeSlackEmoji:
    def test__calc_font_size(self):
        make_slack_emoji = MakeSlackEmoji("Test")
        make_slack_emoji.base_size = 128 * 2
        assert make_slack_emoji._calc_font_size(256, "弓")[1] == (0, 60, 217, 256)
