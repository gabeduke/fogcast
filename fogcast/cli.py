# -*- coding: utf-8 -*-
import sys
import click
from loadconfig import Config

sys.path.append('/fogcast/fogcast')
import fogcast

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
def main():
    """Return a chance of fog for any hour in the subsequent 48 hours where the difference
     between dewpoint and temperature is greater than 5 degrees"""
    conf = '!include config.yml'
    c = Config(conf)

    print(c.forecast_key)
    res = fogcast.fetch_forecast_by_hour(c.API_KEYS.forecast_key, c.VARS.lat, c.VARS.lng)
    fogcast.calc_fog_from_dewpoint_diff(res)


if __name__ == "__main__":
    main()
