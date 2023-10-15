import aiofiles
import os

async def bytesize(filename):
    filesize = os.path.getsize(filename)
    async with aiofiles.open(filename, "rb") as f:
        # Search for the start of the audio data
        i = 0
        while i < filesize:
            # Read 4096 bytes at a time
            data = await f.read(2048)
            for j in range(len(data) - 3):
                if data[j:j+2] == b'\xff\xfb':
                    # Found the start of the audio data
                    # Calculate the byte range
                    start = i + j
                    end = filesize
                    return start, end
            i += len(data)