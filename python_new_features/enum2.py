from enum import Enum

class Status(Enum):
    SUCCESS = 'OK'
    ERROR = 'FAIL'

print(Status.SUCCESS.name) # SUCCESS
print(Status.SUCCESS.value)  # 'OK'