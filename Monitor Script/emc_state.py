#!/usr/bin/python3
# coding=utf-8
# zhangrj http://www.icoder.top/

import json
import os

EMC_manage_ip = "10.10.19.1"
zabbix_server_ip = "zabbix"
monitored_host_name = "StorageEMC"
# Disk State
disk_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getdisk|grep -E 'Bus.*Enclosure.*Disk'".format(EMC_manage_ip)).read().splitlines()

for diskname in disk_list:
	disk_key = "emc.vnx.status[" + diskname + "]"
	disk_number = diskname.replace(' ', '').replace('Bus', '').replace('Enclosure', '_').replace('Disk', '_')
	check_disk_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getdisk ".format(EMC_manage_ip) + disk_number + "|grep State|awk '{$1=\"\";print $0}'"
	disk_state = os.popen(check_disk_state_cmd).read().lstrip().replace('\n', '')	
	send_disk_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + disk_key + "' -o '" + disk_state + "'"
	os.system(send_disk_state_cmd)

# Power State
powerA_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -vsca|grep -Eo 'Bus.*Enclosure.*Power.*State'".format(EMC_manage_ip)).read().splitlines()
powerB_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -vscb|grep -Eo 'Bus.*Enclosure.*Power.*State'".format(EMC_manage_ip)).read().splitlines()

for powerAname in powerA_list:
	power_key = "emc.vnx.status[" + powerAname + "]"
	check_power_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -vsca|grep '".format(EMC_manage_ip) + powerAname +"'|awk '{print $8}'"
	power_state = os.popen(check_power_state_cmd).read().replace('\n', '')
	send_power_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + power_key + "' -o '" + power_state + "'"
	os.system(send_power_state_cmd) 

for powerBname in powerB_list:
	power_key = "emc.vnx.status[" + powerBname + "]"
	check_power_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -vscb|grep '".format(EMC_manage_ip) + powerBname +"'|awk '{print $8}'"
	power_state = os.popen(check_power_state_cmd).read().replace('\n', '')
	send_power_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + power_key + "' -o '" + power_state + "'"
	os.system(send_power_state_cmd)

# LCC State
lccA_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -lcca|grep -Eo 'Bus.*Enclosure.*LCC.*State'".format(EMC_manage_ip)).read().splitlines()
lccB_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -lccb|grep -Eo 'Bus.*Enclosure.*LCC.*State'".format(EMC_manage_ip)).read().splitlines()

for lccAname in lccA_list:
	lcc_key = "emc.vnx.status[" + lccAname + "]"
	check_lcc_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -lcca|grep '".format(EMC_manage_ip) + lccAname +"'|awk '{print $8}'"
	lcc_state = os.popen(check_lcc_state_cmd).read().replace('\n', '')
	send_lcc_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + lcc_key + "' -o '" + lcc_state + "'"
	os.system(send_lcc_state_cmd)

for lccBname in lccB_list:
	lcc_key = "emc.vnx.status[" + lccBname + "]"
	check_lcc_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -lccb|grep '".format(EMC_manage_ip) + lccBname +"'|awk '{print $8}'"
	lcc_state = os.popen(check_lcc_state_cmd).read().replace('\n', '')
	send_lcc_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + lcc_key + "' -o '" + lcc_state + "'"
	os.system(send_lcc_state_cmd)

# SP State
spa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spa|grep -Eo 'SP.*State'".format(EMC_manage_ip)).read().splitlines()
spb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spb|grep -Eo 'SP.*State'".format(EMC_manage_ip)).read().splitlines()

for spaname in spa_list:
	sp_key = "emc.vnx.status[" + spaname + "]"
	check_sp_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -spa|grep '".format(EMC_manage_ip) + spaname +"'|awk '{print $4}'"
	sp_state = os.popen(check_sp_state_cmd).read().replace('\n', '')
	send_sp_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sp_key + "' -o '" + sp_state + "'"
	os.system(send_sp_state_cmd)

for spbname in spb_list:
	sp_key = "emc.vnx.status[" + spbname + "]"
	check_sp_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -spb|grep '".format(EMC_manage_ip) + spbname +"'|awk '{print $4}'"
	sp_state = os.popen(check_sp_state_cmd).read().replace('\n', '')
	send_sp_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sp_key + "' -o '" + sp_state + "'"
	os.system(send_sp_state_cmd)

# SPS state
spsa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsa|grep -Eo 'Bus.*Enclosure.*SPS.*State'".format(EMC_manage_ip)).read().splitlines()
spsb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsb|grep -Eo 'Bus.*Enclosure.*SPS.*State'".format(EMC_manage_ip)).read().splitlines()

for spsaname in spsa_list:
	sps_key = "emc.vnx.status[" + spsaname + "]"
	check_sps_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsa|grep '".format(EMC_manage_ip) + spsaname +"'|awk '{print $8}'"
	sps_state = os.popen(check_sps_state_cmd).read().replace('\n', '')
	send_sps_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sps_key + "' -o '" + sps_state + "'"
	os.system(send_sps_state_cmd)

for spsbname in spsb_list:
	sps_key = "emc.vnx.status[" + spsbname + "]"
	check_sps_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsb|grep '".format(EMC_manage_ip) + spsbname +"'|awk '{print $8}'"
	sps_state = os.popen(check_sps_state_cmd).read().replace('\n', '')
	send_sps_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sps_key + "' -o '" + sps_state + "'"
	os.system(send_sps_state_cmd)

# SPS Cable State
spsa_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsa|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'".format(EMC_manage_ip)).read().splitlines()
spsb_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsb|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'".format(EMC_manage_ip)).read().splitlines()

for spsa_cable_name in spsa_cable_list:
	sps_cable_key = "emc.vnx.status[" + spsa_cable_name + "]"
	check_sps_cable_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsa|grep '".format(EMC_manage_ip) + spsa_cable_name + "'|awk '{print $9}'"
	sps_cable_state = os.popen(check_sps_cable_state_cmd).read().replace('\n', '')
	send_sps_cable_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sps_cable_key + "' -o '" + sps_cable_state + "'"
	os.system(send_sps_cable_state_cmd)

for spsb_cable_name in spsb_cable_list:
	sps_cable_key = "emc.vnx.status[" + spsb_cable_name + "]"
	check_sps_cable_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsb|grep '".format(EMC_manage_ip) + spsb_cable_name + "'|awk '{print $9}'"
	sps_cable_state = os.popen(check_sps_cable_state_cmd).read().replace('\n', '')
	send_sps_cable_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + sps_cable_key + "' -o '" + sps_cable_state + "'"
	os.system(send_sps_cable_state_cmd)

# CPU State
cpua_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpua|grep -Eo 'Bus.*Enclosure.*CPU.*State'".format(EMC_manage_ip)).read().splitlines()
cpub_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpub|grep -Eo 'Bus.*Enclosure.*CPU.*State'".format(EMC_manage_ip)).read().splitlines()

for cpua_name in cpua_list:
	cpu_key = "emc.vnx.status[" + cpua_name + "]"
	check_cpu_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpua|grep '".format(EMC_manage_ip) + cpua_name + "'|awk '{print $9}'"
	cpu_state = os.popen(check_cpu_state_cmd).read().replace('\n', '')
	send_cpu_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + cpu_key + "' -o '" + cpu_state + "'"
	os.system(send_cpu_state_cmd)

for cpub_name in cpub_list:
	cpu_key = "emc.vnx.status[" + cpub_name + "]"
	check_cpu_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpub|grep '".format(EMC_manage_ip) + cpub_name + "'|awk '{print $9}'"
	cpu_state = os.popen(check_cpu_state_cmd).read().replace('\n', '')
	send_cpu_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + cpu_key + "' -o '" + cpu_state + "'"
	os.system(send_cpu_state_cmd)

# DIMM State
dimma_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimma|grep -Eo 'Bus.*Enclosure.*DIMM.*State'".format(EMC_manage_ip)).read().splitlines()
dimmb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimmb|grep -Eo 'Bus.*Enclosure.*DIMM.*State'".format(EMC_manage_ip)).read().splitlines()

for dimma_name in dimma_list:
	dimm_key = "emc.vnx.status[" + dimma_name + "]"
	check_dimm_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimma|grep '".format(EMC_manage_ip) + dimma_name + "'|awk '{print $9}'"
	dimm_state = os.popen(check_dimm_state_cmd).read().replace('\n', '')
	send_dimm_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + dimm_key + "' -o '" + dimm_state + "'"
	os.system(send_dimm_state_cmd)

for dimmb_name in dimmb_list:
	dimm_key = "emc.vnx.status[" + dimmb_name + "]"
	check_dimm_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimmb|grep '".format(EMC_manage_ip) + dimmb_name + "'|awk '{print $9}'"
	dimm_state = os.popen(check_dimm_state_cmd).read().replace('\n', '')
	send_dimm_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + dimm_key + "' -o '" + dimm_state + "'"
	os.system(send_dimm_state_cmd)

# I/O State
ioa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -ioa|grep -Eo 'Bus.*Enclosure.*I/O.*State'".format(EMC_manage_ip)).read().splitlines()
iob_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -iob|grep -Eo 'Bus.*Enclosure.*I/O.*State'".format(EMC_manage_ip)).read().splitlines()

for ioa_name in ioa_list:
	io_key = "emc.vnx.status[" + ioa_name + "]"
	check_io_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -ioa|grep '".format(EMC_manage_ip) + ioa_name + "'|awk '{print $11}'"
	io_state = os.popen(check_io_state_cmd).read().replace('\n', '')
	send_io_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + io_key + "' -o '" + io_state + "'"
	os.system(send_io_state_cmd)

for iob_name in iob_list:
	io_key = "emc.vnx.status[" + iob_name + "]"
	check_io_state_cmd = "/opt/Navisphere/bin/naviseccli -h {0} getcrus -iob|grep '".format(EMC_manage_ip) + iob_name + "'|awk '{print $11}'"
	io_state = os.popen(check_io_state_cmd).read().replace('\n', '')
	send_io_state_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k '".format(zabbix_server_ip, monitored_host_name) + io_key + "' -o '" + io_state + "'"
	os.system(send_io_state_cmd)
