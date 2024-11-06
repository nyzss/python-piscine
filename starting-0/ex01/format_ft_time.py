from datetime import datetime

timestamp = datetime.now().timestamp()

epoch = datetime.fromtimestamp(0).strftime("%B %-d, %Y")

print(f"Seconds since {epoch}: {timestamp:,} or {timestamp:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
