import time


class BasePrint:
    def __init__(self, _time: bool = True, _location: bool = True, _path: bool = True):
        self.time = _time
        self.location = _location
        self.path = _path

    def __call__(self, text: str, _time: bool = None, _location: bool = None, _path: bool = None):
        if _time is None:
            _time = self.time
        if _location is None:
            _location = self.location
        if _path is None:
            _path = self.path

        details = []
        if _time:
            details.append(str(time.ctime(time.time())))
        if _location and _path:
            # details.append(f"{stack()[1][1]}:{currentframe().f_back.f_lineno}")
            details.append("fixme")  # fixme
        elif _location:
            double_backslash = "\\"
            # details.append(
            #     f"{stack()[1][1].split('/')[-1].split(double_backslash)[-1]}:{currentframe().f_back.f_lineno}"
            # )
            details.append("fixme")  # fixme
        if details:
            print(f"[{' '.join(details)}] {text}")
