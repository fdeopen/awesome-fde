"""Illustrative value model. Amounts must use one currency and period."""
import argparse
import json
import math
from decimal import Decimal


def estimate(tasks, saved_minutes, hourly_cost, realization, monthly_cost,
             upfront, months):
    if not all(math.isfinite(v) for v in (tasks, saved_minutes, hourly_cost, realization, monthly_cost, upfront, months)):
        raise ValueError("Inputs must be finite")
    if tasks < 0 or saved_minutes < 0 or hourly_cost < 0:
        raise ValueError("Volume, time and hourly cost must be nonnegative")
    if not 0 <= realization <= 1 or monthly_cost < 0 or upfront < 0 or months <= 0:
        raise ValueError("Invalid realization, costs or period")
    hours = tasks * saved_minutes / 60
    benefit = float((Decimal(str(tasks)) * Decimal(str(saved_minutes)) * Decimal(str(hourly_cost)) * Decimal(str(realization)) / Decimal(60)).quantize(Decimal('0.01')))
    net = round(benefit - monthly_cost, 2)
    return {"hours_saved_monthly": round(hours, 2),
            "realized_benefit_monthly": round(benefit, 2),
            "net_benefit_monthly": round(net, 2),
            "net_value_period": round(net * months - upfront, 2),
            "roi_on_upfront": round((net * months - upfront) / upfront, 4) if upfront else None,
            "payback_months": round(upfront / net, 2) if net > 0 and upfront else None}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name, default in [("tasks", 1000), ("saved-minutes", 4), ("hourly-cost", 60),
                          ("realization", .5), ("monthly-cost", 1000),
                          ("upfront", 12000), ("months", 12)]:
        p.add_argument("--" + name, type=float, default=default)
    args = vars(p.parse_args())
    for realization in sorted(set([.25, args["realization"], .75])):
        current = dict(args, realization=realization)
        print(json.dumps({"realization": realization, **estimate(**current)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
