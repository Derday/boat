import numpy as np
import uuid
import os

buffer_size = 32 * 1024**2
chunks_per_commit = 8

chunks = 0

while True:

    for _ in range(chunks_per_commit):
        data = np.empty(buffer_size, dtype=bool)
        chunks += 1
        with open(f'{uuid.uuid4()}.chunk', 'wb') as f:
            f.write(data.tobytes())

    os.system('git add .')
    os.system(
        f'git commit -m "Repo at {(chunks * buffer_size)/1024**3:.02f}GB"'
    )
    code = os.system('git push')

    if code != 0:
        print('git push return non-zero exit code!')
        break
    print(f'Repo at {(chunks * buffer_size)/1024**3:.02f}GB')
