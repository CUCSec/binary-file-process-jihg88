import struct


def tamper(student_id):
  with open('d:\Program Files\pywork\pywork2\lenna.bmp','r+b') as f:
    f.seek(57)
    for a in student_id:
      b=int(a)
      if(b==0):
        b=10
      f.read((b-1)*3)
      f.write(bytes.fromhex('000000'))




def detect():
  with open('d:\Program Files\pywork\pywork2\lenna.bmp', 'rb') as f:
    bmp_file_header = f.read(14)

    bm, size, r1, r2, offset = struct.unpack('<2sIHHI', bmp_file_header)

    f.seek(offset)

    count = 12
    offset = 0
    last_offset = 0
    while count > 0:
      color = f.read(3)

      if color == b'\x00\x00\x00':

        if offset - last_offset == 10:
          print(0)
        else:
          print(offset - last_offset)

        last_offset = offset
        count -= 1

      offset += 1


if __name__ == '__main__':
  import sys
  tamper(sys.argv[1])

  detect()
