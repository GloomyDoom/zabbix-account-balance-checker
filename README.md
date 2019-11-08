# zabbix account balance checker
Zabbix external script for checking account data (balance, limits etc.) in numeric format

1. Copy script "web_request_def.py" to directory: usr/lib/zabbix/externalscripts

2. Open Zabbix panel and create new item in new template:
    Type: External check
    Key: web_request_def.py["--auth_url",{$A_URL},"--csrf_url",{$CS_URL},"--count_url",{$C_URL},"--regex_csrf",{$R_CS},"--regex_count",{$R_C},"--login",{$L},"--passw",{$P}, "--name_login",{$N_L}, "--name_passw",{$N_P}, "--name_csrf",{$N_CS}]
    Type of information: Numeric (float)

3. Add new host, where you want to use linked template or import provided template

4. Add Host macros and write value:

    |Macros|Description|
    |------|-----------|
    |{$A_URL} | registration page |
    |{$CS_URL} | csrf-token page |
    |{$C_URL} | data page |
    |{$R_CS} | regular expression for getting csrf-token |
    |{$R_C} | regular expression for getting value |
    |{$L} | login |
    |{$P} | password |
    |{$N_L} | name of the field for a login |
    |{$N_P}| name of the field for a password |
    |{$N_CS} | name of the tag class for getting csrf-token |

5. Rewrite or use trigger in template. 