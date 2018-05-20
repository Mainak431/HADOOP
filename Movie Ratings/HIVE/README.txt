GO to ambari server at 127.0.0.1:8080
login to maria_dev
password maria_dev
go to HIVE VIEW
Upload Table

Upload from CSV

As the file delimiter is not space in our u.data file, we change that to Tab or ascii 9. and then we upload the file from u.data

provide schema name as ratings
column names - userID,MovieID,rating,epochseconds
Upload Table

Similarly upload u.item as names schema
column names- movieid,title,releasedate