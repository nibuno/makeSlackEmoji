from main import MakeSlackEmoji


class TestMakeSlackEmoji:
    def test__calc_font_size(self):
        make_slack_emoji = MakeSlackEmoji("弓")
        make_slack_emoji.base_size = 128
        assert make_slack_emoji._calc_font_size(256, "弓")[1] == (0, 30, 108, 128)

        make_slack_emoji = MakeSlackEmoji("hello")
        make_slack_emoji.base_size = 128
        assert make_slack_emoji._calc_font_size(256, "hello")[1] == (0, 16, 127, 55)

        make_slack_emoji = MakeSlackEmoji("Yumihiki")
        make_slack_emoji.base_size = 128
        assert make_slack_emoji._calc_font_size(256, "Yumihiki")[1] == (0, 10, 127, 32)
