# daycolor

daycolor allows you to choose a (RGB) colors for multiple times of the day and fluidly return HSV-interpolated "in-between" colors. The times of the day plus the color may be specified in a a `daycolordict` as shown below. 

This is simply a regular Python dict with strings as indicies. If you need more precision than minutes, you can specify custom patterns.

```python
daycolordict = {
    "01:00":(255,127,80),
    "02:00":(257,34,35),
    "03:00":(126,1,0),
    "10:00":(126,255,0),
    "11:00":(255,244,66),
    "12:00":(253,216,161),
    "18:00":(27,25,109),
    "19:00":(0,0,254),
    "23:00":(255,244,66),
    "23:59":(253,261,161)
    }
```

The `daycolordict` automagically "wraps around", that means unless desired there will never be a hard jumps between colors.



So for example to get the color for the current time from a dict you could run `get_current()` with your dict as an argument:

```python
import daycolor
daycolor.get_current(daycolordict)
```

If you would rather specify your own time you can do it with the `get_by_datetime()` function:

```python
import datetime
# Get the datetime for a hour into the future
a_hour_in_the_future = datetime.datetime.now() + datetime.timedelta(hours=1)
daycolor.get_by_datetime(a_hour_in_the_future, daycolordict)
```

If you like to interpolate over the colors in a completely different fashion (e.g. randomly selecting a color that is interpolated between the chosen colors) you can do so by using the `get_by_value()` function:

```python
import random
value = random.random()
daycolor.get_by_value(value, daycolordict)
```

## Custom Patterns

If you would like to get more accuracy in the timedict you could define your daycolors for example as follows:

```python
daycolordict = {
    "00:00.00":(0,0,0),
    "00:00.01":(255,0,0),
    "00:00.02":(0,0,0),
    "00:00.03":(255,0,0),
    "00:00.04":(0,0,0),
    "00:00.05":(255,0,0),
    "00:00.06":(0,0,0),
    "00:00.07":(255,0,0),
    "00:00.08":(0,0,0),
    "00:00.07":(255,0,0),
    "00:00.09":(0,0,0),
    "12:00.00":(253,216,161),
    "23:00.00":(255,244,66),
    }
```

This would return 5 red values every two seconds after midnight and then go black again. To make this wrk you need to call your `get_current()` with a pattern like so:

```python
daycolor.get_current(daycolordict, pattern="%H:%M.%S")
```

If you wanna see how these patterns are defined, check the [datetime strftime strptime behavior page](https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior). With this you could even achive microsecond precision.
