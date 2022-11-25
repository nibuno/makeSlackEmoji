from main import MakeSlackEmoji


class TestMakeSlackEmoji:
    def test__calc_font_size(self):
        make_slack_emoji = MakeSlackEmoji("弓")
        make_slack_emoji.base_size = 100
        assert make_slack_emoji._calc_font_size(100, "弓")[1] \
               == (0, 23, 84, 100)

        make_slack_emoji = MakeSlackEmoji("Yumihiki")
        make_slack_emoji.base_size = 100
        assert make_slack_emoji._calc_font_size(100, "Yumihiki")[1] \
               == (0, 7, 99, 25)
