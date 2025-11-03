from pytest import mark


@mark.config
class ConfigurationTests:
    alarm = True
    car_mode = "manual"
    @mark.entertainment
    def test_sound_configuration(self):
        assert True
    @mark.engine
    def test_alarm_configuration(self):
        assert self.alarm == True
    @mark.body
    def test_carmode_configuration(self):
        assert "manual" == self.car_mode