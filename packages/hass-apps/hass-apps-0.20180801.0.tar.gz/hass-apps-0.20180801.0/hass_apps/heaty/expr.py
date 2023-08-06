"""
Module containing functionality to evaluate temperature expressions.
"""

import typing as T
if T.TYPE_CHECKING:
    # pylint: disable=cyclic-import,unused-import
    from . import schedule
    from .app import HeatyApp
import types

import datetime
import functools


__all__ = ["Add", "Break", "Ignore", "IncludeSchedule", "OFF", "Off",
           "Result", "Skip", "SkipSubSchedule", "Temp"]


# type of an evaluable expression
ExprType = T.Union[str, types.CodeType, "Temp"]
# allowed types of values to initialize Temp() with
TempValueType = T.Union[float, int, str, "Off", "Temp"]


class AddibleMixin:
    """Mixin that makes a temperature expression result addible."""
    pass

class ResultBase:
    """Holds the result of a temperature expression."""

    def __init__(self, temp: T.Any) -> None:
        self.temp = Temp(temp)  # type: T.Optional[Temp]

    def __eq__(self, other: T.Any) -> bool:
        return type(self) is type(other) and self.temp == other.temp


class Result(ResultBase, AddibleMixin):
    """Final result of a temperature expression."""

    def __repr__(self) -> str:
        return "Result({})".format(self.temp)

class Add(ResultBase, AddibleMixin):
    """Result of a temperature expression that is intended to be added
    to the result of a consequent expression."""

    def __add__(self, other: ResultBase) -> ResultBase:
        if not isinstance(other, AddibleMixin):
            raise TypeError("can't add {} and {}"
                            .format(repr(type(self)), repr(type(other))))

        return type(other)(self.temp + other.temp)

    def __repr__(self) -> str:
        return "Add({})".format(self.temp)

class Break(ResultBase):
    """Result of a temperature expression that should abort scheduling and
    leave the temperature unchanged."""

    def __init__(self) -> None:
        # pylint: disable=super-init-not-called
        self.temp = None

    def __repr__(self) -> str:
        return "Break()"


class IncludeSchedule(ResultBase):
    """Result that includes a schedule for processing."""

    def __init__(self, sched: "schedule.Schedule") -> None:
        # pylint: disable=super-init-not-called
        self.schedule = sched

    def __repr__(self) -> str:
        return "IncludeSchedule({})".format(self.schedule)


class Off:
    """A special value Temp() may be initialized with in order to turn
    a thermostat off."""

    def __add__(self, other: T.Any) -> "Off":
        return self

    def __eq__(self, other: T.Any) -> bool:
        return isinstance(other, Off)

    def __hash__(self) -> int:
        return hash(str(self))

    def __neg__(self) -> "Off":
        return self

    def __repr__(self) -> str:
        return "OFF"

    def __sub__(self, other: T.Any) -> "Off":
        return self

OFF = Off()


class Skip(ResultBase):
    """Result of a temperature expression which should be ignored."""

    def __init__(self) -> None:
        # pylint: disable=super-init-not-called
        self.temp = None

    def __repr__(self) -> str:
        return "Skip()"

# Provide the old name as a fallback
Ignore = Skip


class SkipSubSchedule(ResultBase):
    """Result of a temperature expression which causes a sub-schedule of "
    the holding rule to be skipped.."""

    def __init__(self) -> None:
        # pylint: disable=super-init-not-called
        self.temp = None

    def __repr__(self) -> str:
        return "SkipSubSchedule()"


@functools.total_ordering
class Temp:
    """A class holding a temperature value."""

    def __init__(self, temp_value: T.Any) -> None:
        if isinstance(temp_value, Temp):
            # Just copy the value over.
            parsed = self.parse_temp(temp_value.value)
        else:
            parsed = self.parse_temp(temp_value)

        if parsed is None:
            raise ValueError("{} is no valid temperature"
                             .format(repr(temp_value)))

        self.value = parsed  # type: T.Union[float, Off]

    def __add__(self, other: T.Any) -> "Temp":
        if isinstance(other, (float, int)):
            other = Temp(other)
        elif not isinstance(other, Temp):
            raise TypeError("can't add {} and {}"
                            .format(repr(type(self)), repr(type(other))))

        # OFF + something is OFF
        if self.is_off or other.is_off:
            return Temp(Off())

        return Temp(self.value + other.value)

    def __eq__(self, other: T.Any) -> bool:
        return isinstance(other, Temp) and self.value == other.value

    def __float__(self) -> float:
        if isinstance(self.value, float):
            return self.value
        raise ValueError("{} has no numeric value.".format(repr(self)))

    def __hash__(self) -> int:
        return hash(str(self))

    def __lt__(self, other: T.Any) -> bool:
        if isinstance(other, (float, int)):
            other = Temp(other)

        if type(self) is not type(other):
            raise TypeError("can't compare {} and {}"
                            .format(repr(type(self)), repr(type(other))))

        if not self.is_off and other.is_off:
            return False
        if self.is_off and not other.is_off or \
           self.value < other.value:
            return True
        return False

    def __neg__(self) -> "Temp":
        return Temp(-self.value)  # pylint: disable=invalid-unary-operand-type

    def __repr__(self) -> str:
        if isinstance(self.value, (float, int)):
            return "{}°".format(self.value)
        return "{}".format(self.value)

    def __sub__(self, other: T.Any) -> "Temp":
        return self.__add__(-other)

    @property
    def is_off(self) -> bool:
        """Tells whether this temperature means OFF."""
        return isinstance(self.value, Off)

    @staticmethod
    def parse_temp(value: T.Any) -> T.Union[float, Off, None]:
        """Converts the given value to a valid temperature of type float
        or Off().
        If value is a string, all whitespace is removed first.
        If conversion is not possible, None is returned."""

        if isinstance(value, str):
            value = "".join(value.split())
            if value.upper() == "OFF":
                return Off()

        if isinstance(value, Off):
            return Off()

        try:
            return float(value)
        except (ValueError, TypeError):
            return None


def build_expr_env(app: "HeatyApp") -> T.Dict[str, T.Any]:
    """This function builds and returns an environment usable as globals
    for the evaluation of an expression. It will add all members
    of this module's __all__ to the environment. Additionally, some
    helpers will be constructed based on the HeatyApp object"""

    # use date/time provided by appdaemon to support time-traveling
    now = app.datetime()
    env = {
        "app": app,
        "schedule_snippets": app.cfg["schedule_snippets"],
        "datetime": datetime,
        "now": now,
        "date": now.date(),
        "time": now.time(),
        "state": app.get_state,
        "is_on":
            lambda entity_id: str(app.get_state(entity_id)).lower() == "on",
        "is_off":
            lambda entity_id: str(app.get_state(entity_id)).lower() == "off",
    }

    globs = globals()
    for name in __all__:
        env[name] = globs[name]

    env.update(app.temp_expression_modules)

    return env

def eval_temp_expr(
        temp_expr: ExprType,
        app: "HeatyApp",
        extra_env: T.Optional[T.Dict[str, T.Any]] = None
) -> ResultBase:
    """This method evaluates the given temperature expression.
    The evaluation result is returned. The items of the extra_env
    dict are added to the globals available during evaluation.
    If the expression is a Temp object already, it's just packed into
    a Result and returned directly."""

    # pylint: disable=eval-used

    if isinstance(temp_expr, Temp):
        return Result(temp_expr)

    env = build_expr_env(app)
    if extra_env:
        env.update(extra_env)

    eval_result = eval(temp_expr, env)
    if isinstance(eval_result, ResultBase):
        result = eval_result
    else:
        result = Result(eval_result)
    return result
