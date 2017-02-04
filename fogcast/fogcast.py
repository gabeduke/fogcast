# fetching weather
import sys
import click
import forecastio


def fetch_forecast_by_hour(forecast_key, lat, lng):
    forecast = forecastio.load_forecast(forecast_key, lat, lng)
    return forecast.hourly()


def calc_fog_from_dewpoint_diff(response_by_hour):
    fogTimes = []
    debug = []

    for hourlyData in response_by_hour.data:
        deg = hourlyData.temperature
        dew = hourlyData.dewPoint
        diff = abs(dew - deg)
        debug.append('{:%a: %I %P}'.format(hourlyData.time) + " | dewpoint = " + str(int(dew)) + " | deg = " + str(
            int(deg)) + " | diff = " + str(int(diff)))
        if deg <= 66 and int(diff) <= 5:
            fogTimes.append('Chance of fog on ' + '{:%a at %I %P}'.format(hourlyData.time))

    if len(sys.argv) > 1 and "debug" in sys.argv[1:]:
        click.echo('\n').join(debug)

    if not fogTimes:
        click.echo('There is no fog forecasted in the next 48 hours')
    else:
        click.echo('\n').join(fogTimes)
