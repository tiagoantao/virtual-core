<?php
// Zabbix GUI configuration file.
global $DB;

$DB['TYPE']     = 'SQLITE3';
$DB['SERVER']   = 'localhost';
$DB['DATABASE'] = '/db/zabbix.sqlite';
$DB['USER']     = 'zabbix';
$DB['PASSWORD'] = '';

$IMAGE_FORMAT_DEFAULT   = IMAGE_FORMAT_PNG;
?>
