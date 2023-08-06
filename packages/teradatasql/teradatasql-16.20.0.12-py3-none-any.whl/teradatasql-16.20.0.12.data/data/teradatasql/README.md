## Teradata SQL Driver for Python

This module enables Python applications to connect to the Teradata Database, and interoperates with Teradata Database 12.0 and later releases.

This module implements the [PEP-249 Python Database API Specification 2.0](https://www.python.org/dev/peps/pep-0249/).

This module requires 64-bit Python 3.x, and runs on Windows, macOS, and Linux. 32-bit Python is not supported.

For community support, please visit the [Connectivity Forum](http://community.teradata.com/t5/Connectivity/bd-p/DevXConnectivityBoard).

Copyright 2018 Teradata. All Rights Reserved.

### Features

The Teradata SQL Driver for Python is a young product that offers a basic feature set. We are working diligently to add features to the Teradata SQL Driver for Python, and our goal is feature parity with the Teradata JDBC Driver.

At the present time, the Teradata SQL Driver for Python offers the following features.

* Interoperability with Teradata Database 12.0 and later releases.
* Encrypted logon using the `TD2`, `LDAP`, `KRB5` (Kerberos), or `TDNEGO` logon mechanisms.
* Data encryption enabled via the `encryptdata` connection parameter.
* Unicode character data transferred via the UTF8 session character set.
* 1 MB rows supported with Teradata Database 16.0 and later.
* Multi-statement requests that return multiple result sets.
* Most JDBC escape syntax.
* Parameterized SQL requests with question-mark parameter markers.
* Parameterized batch SQL requests with multiple rows of data bound to question-mark parameter markers.
* ElicitFile protocol support for DDL commands that create external UDFs or stored procedures and upload a file from client to database.

### Limitations

* The Teradata Database's default transaction mode (ANSI or TERA) is always used. The `tmode` connection parameter is not supported yet.
* The UTF8 session character set is always used. The `charset` connection parameter is not supported.
* The following complex data types are not supported yet: `XML`, `JSON`, `DATASET STORAGE FORMAT AVRO`, and `DATASET STORAGE FORMAT CSV`.
* The `CREATE PROCEDURE` and `REPLACE PROCEDURE` commands are not supported yet. These commands use a different wire protocol from other DDL commands.
* COP Discovery is not supported yet. You must specify the hostname or IP address of a specific Teradata Database node to connect to.
* No support yet for data encryption that is governed by central administration. To enable data encryption, you must specify a `true` value for the `encryptdata` connection parameter.
* Laddered Concurrent Connect is not supported yet.
* The JWT logon mechanism is not supported yet.
* No support yet for Recoverable Network Protocol and Redrive.
* Auto-commit for ANSI transaction mode is not offered yet. You must explicitly execute a `commit` command when using ANSI transaction mode.
* FastLoad is not available yet.
* FastExport is not available yet.
* Monitor partition support is not available yet.

### Installation

Use pip to install the Teradata SQL Driver for Python.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install teradatasql`
Windows        | `py -3 pip install teradatasql`

When upgrading to a new version of the Teradata SQL Driver for Python, you may need to use pip install's `--no-cache-dir` option to force the download of the new version.

Platform       | Command
-------------- | ---
macOS or Linux | `pip install --no-cache-dir -U teradatasql`
Windows        | `py -3 pip install --no-cache-dir -U teradatasql`

### Using the Teradata SQL Driver for Python

Your Python script must import the `teradatasql` module in order to use the Teradata SQL Driver for Python.

    import teradatasql

After importing the `teradatasql` module, your Python script calls the `teradatasql.connect` function to open a connection to the Teradata Database.

You may specify connection parameters as `kwargs`, as a JSON string, or using a combination of the two approaches. The `teradatasql.connect` function's first argument is a JSON string. The `teradatasql.connect` function's second and subsequent arguments are optional `kwargs`.

* Connection parameters specified only as `kwargs`

        con = teradatasql.connect(None, host='whomooz', user='guest', password='please')

* Connection parameters specified only as a JSON string

        con = teradatasql.connect('{"host":"whomooz","user":"guest","password":"please"}')

* Connection parameters specified using a combination

        con = teradatasql.connect('{"host":"whomooz"}', user='guest', password='please')

### Connection Parameters

The following table lists the connection parameters currently offered by the Teradata SQL Driver for Python.

Our goal is consistency for the connection parameters offered by the Teradata SQL Driver for Python and the Teradata JDBC Driver, with respect to connection parameter names and functionality. For comparison, Teradata JDBC Driver connection parameters are [documented here](http://developer.teradata.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html#BGBHDDGB).

Parameter          | Default     | Type           | Description
------------------ | ----------- | -------------- | ---
`account`          |             | string         | Specifies the Teradata Database account. Equivalent to the Teradata JDBC Driver `ACCOUNT` connection parameter.
`column_name`      | `"false"`   | quoted boolean | Controls the behavior of cursor `.description` sequence `name` items. Equivalent to the Teradata JDBC Driver `COLUMN_NAME` connection parameter. False specifies that a cursor `.description` sequence `name` item provides the AS-clause name if available, or the column name if available, or the column title. True specifies that a cursor `.description` sequence `name` item provides the column name if available, but has no effect when StatementInfo parcel support is unavailable.
`dbs_port`         | `"1025"`    | quoted integer | Specifies Teradata Database port number. Equivalent to the Teradata JDBC Driver `DBS_PORT` connection parameter.
`encryptdata`      | `"false"`   | quoted boolean | Controls encryption of data exchanged between the Teradata Database and the Teradata SQL Driver for Python. Equivalent to the Teradata JDBC Driver `ENCRYPTDATA` connection parameter.
`fake_result_sets` | `"false"`   | quoted boolean | Controls whether a fake result set containing statement metadata precedes each real result set.
`host`             |             | string         | Specifies the Teradata Database hostname. Note that COP Discovery is not implemented yet.
`lob_support`      | `"true"`    | quoted boolean | Controls LOB support. Equivalent to the Teradata JDBC Driver `LOB_SUPPORT` connection parameter.
`log`              | `"0"`       | quoted integer | Controls debug logging. Somewhat equivalent to the Teradata JDBC Driver `LOG` connection parameter. This parameter's behavior is subject to change in the future. This parameter's value is currently defined as an integer in which the 1-bit governs function and method tracing, the 2-bit governs debug logging, and the 4-bit governs transmit and receive message hex dumps.
`logdata`          |             | string         | Specifies extra data for the chosen logon authentication method. Equivalent to the Teradata JDBC Driver `LOGDATA` connection parameter.
`logmech`          | `"TD2"`     | string         | Specifies the logon authentication method. Equivalent to the Teradata JDBC Driver `LOGMECH` connection parameter. Possible values are `TD2` (the default), `LDAP`, `KRB5` for Kerberos, or `TDNEGO`. Note that JWT authentication is not supported yet.
`max_message_body` | `"2097000"` | quoted integer | Not fully implemented yet and intended for future usage. Equivalent to the Teradata JDBC Driver `MAX_MESSAGE_BODY` connection parameter.
`partition`        | `"DBC/SQL"` | string         | Specifies the Teradata Database Partition. Equivalent to the Teradata JDBC Driver `PARTITION` connection parameter.
`password`         |             | string         | Specifies the Teradata Database password. Equivalent to the Teradata JDBC Driver `PASSWORD` connection parameter.
`sip_support`      | `"true"`    | quoted boolean | Controls whether StatementInfo parcel is used. Equivalent to the Teradata JDBC Driver `SIP_SUPPORT` connection parameter.
`user`             |             | string         | Specifies the Teradata Database username. Equivalent to the Teradata JDBC Driver `USER` connection parameter.

### Data Types

The table below lists the Teradata Database data types supported by the Teradata SQL Driver for Python, and indicates the corresponding Python data type returned in result set rows.

Teradata Database data type        | Result set Python data type
---------------------------------- | ---
`BYTEINT`                          | `int`
`SMALLINT`                         | `int`
`INTEGER`                          | `int`
`BIGINT`                           | `int`
`FLOAT`                            | `float`
`VARCHAR`                          | `str`
`CHAR`                             | `str`
`CLOB`                             | `str`
`VARBYTE`                          | `bytes`
`BYTE`                             | `bytes`
`BLOB`                             | `bytes`
`DECIMAL`                          | `str`
`NUMBER`                           | `str`
`DATE`                             | `str`
`TIME`                             | `str`
`TIME WITH TIME ZONE`              | `str`
`TIMESTAMP`                        | `str`
`TIMESTAMP WITH TIME ZONE`         | `str`
`INTERVAL YEAR`                    | `str`
`INTERVAL YEAR TO MONTH`           | `str`
`INTERVAL MONTH`                   | `str`
`INTERVAL DAY`                     | `str`
`INTERVAL DAY TO HOUR`             | `str`
`INTERVAL DAY TO MINUTE`           | `str`
`INTERVAL DAY TO SECOND`           | `str`
`INTERVAL HOUR`                    | `str`
`INTERVAL HOUR TO MINUTE`          | `str`
`INTERVAL HOUR TO SECOND`          | `str`
`INTERVAL MINUTE`                  | `str`
`INTERVAL MINUTE TO SECOND`        | `str`
`INTERVAL SECOND`                  | `str`
`PERIOD(DATE)`                     | `str`
`PERIOD(TIME)`                     | `str`
`PERIOD(TIME WITH TIME ZONE)`      | `str`
`PERIOD(TIMESTAMP)`                | `str`
`PERIOD(TIMESTAMP WITH TIME ZONE)` | `str`

The table below lists the parameterized SQL bind-value Python data types supported by the Teradata SQL Driver for Python, and indicates the corresponding Teradata Database data type transmitted to the server.

Bind-value Python data type   | Teradata Database data type
----------------------------- | ---
`bytes`                       | `VARBYTE`
`float`                       | `FLOAT`
`int`                         | `BIGINT`
`str`                         | `VARCHAR`

Transforms are used for SQL `ARRAY` data values, and they can be transferred to and from the database as `VARCHAR` values.

Transforms are used for structured UDT data values, and they can be transferred to and from the database as `VARCHAR` values.

### Null Values

SQL `NULL` values received from the Teradata Database are returned in result set rows as Python `None` values.

A Python `None` value bound to a question-mark parameter marker is transmitted to the Teradata Database as a `NULL` `VARCHAR` value.
