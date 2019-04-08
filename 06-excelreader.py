import pyexcel as pe
records = pe.iget_records(file_name="outexcel.xls")
for record in records:
     print("{} is avialable using the driver {}".format(record['IP'], record['driver']))

pe.free_resources()