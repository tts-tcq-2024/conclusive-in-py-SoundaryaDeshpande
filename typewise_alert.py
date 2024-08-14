def infer_breach(value, lower_limit, upper_limit):
    if value < lower_limit:
        return 'TOO_LOW'
    if value > upper_limit:
        return 'TOO_HIGH'
    return 'NORMAL'

def classify_temperature_breach(cooling_type, temperature_in_c):
    limits = {
        'PASSIVE_COOLING': (0, 35),
        'HI_ACTIVE_COOLING': (0, 45),
        'MED_ACTIVE_COOLING': (0, 40)
    }
    lower_limit, upper_limit = limits.get(cooling_type, (None, None))
    if lower_limit is None or upper_limit is None:
        raise ValueError(f"Unknown cooling type: {cooling_type}")
    return infer_breach(temperature_in_c, lower_limit, upper_limit)

def check_and_alert(alert_target, battery_char, temperature_in_c):
    breach_type = classify_temperature_breach(battery_char['coolingType'], temperature_in_c)
    alert_methods = {
        'TO_CONTROLLER': send_to_controller,
        'TO_EMAIL': send_to_email
    }
    method = alert_methods.get(alert_target)
    if method is None:
        raise ValueError(f"Unknown alert target: {alert_target}")
    method(breach_type)

def send_to_controller(breach_type):
    header = 0xfeed
    print(f'{header}, {breach_type}')

def send_to_email(breach_type):
    recipient = "a.b@c.com"
    messages = {
        'TOO_LOW': 'Hi, the temperature is too low',
        'TOO_HIGH': 'Hi, the temperature is too high'
    }
    print(f'To: {recipient}')
    print(messages.get(breach_type, 'Unknown breach'))

