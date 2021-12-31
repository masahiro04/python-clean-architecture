from repository.memrepo import MemRepo
from use_cases.room_list import room_list_use_case

repo = MemRepo([])
result = room_list_use_case(repo)

print(result)
