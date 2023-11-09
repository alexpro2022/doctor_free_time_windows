from datetime import datetime as dt
from datetime import timedelta

TIME_FORMAT = '%H:%M'
START = 'start'
STOP = 'stop'


def _str_to_time(time: str) -> dt:
    return dt.strptime(time, TIME_FORMAT)


def _time_to_str(time: dt) -> str:
    return time.strftime(TIME_FORMAT)


def calc(busy: list[dict[str, str]],
         start_time: str,
         end_time: str,
         interval_minutes: str) -> list[dict[str, str]]:
    def get_time(key: str) -> str:
        try:
            return busy[busy_idx][key]
        except IndexError:
            return end_time

    interval = timedelta(seconds=60 * int(interval_minutes))
    busy.sort(key=lambda x: x['start'])
    busy_idx = 0
    start = _str_to_time(start_time)
    end = _str_to_time(get_time(START))
    temp_end = start + interval
    free_windows = []
    while busy_idx <= len(busy):
        if temp_end <= end:
            free_windows.append({START: _time_to_str(start),
                                 STOP: _time_to_str(temp_end)})
            start = temp_end
            temp_end = start + interval
        else:
            start = _str_to_time(get_time(STOP))
            busy_idx += 1
            end = _str_to_time(get_time(START))
            temp_end = start + interval
    return free_windows
