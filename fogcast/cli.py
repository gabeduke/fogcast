# -*- coding: utf-8 -*-
from loadconfig import Config


def main():
    conf = '!include config.yml'
    c = Config(conf)

    print(c.forecast_key)
    res = fetch_forecast_by_hour(c.API_KEYS.forecast_key, c.VARS.lat, c.VARS.lng)
    calc_fog_from_dewpoint_diff(res)


if __name__ == "__main__":
    main()
