#!/usr/bin/python3
# coding=utf-8
# zhangrj http://www.icoder.top/

import os
import json

EMC_manage_ip = "10.10.19.1"
zabbix_server_ip = "zabbix"
monitored_host_name = "StorageEMC"
# Disk Discovery
disk_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getdisk|grep -E 'Bus.*Enclosure.*Disk'".format(EMC_manage_ip)).read().splitlines()
disk_dic_list = []

for diskname in disk_list:
	disk_dic = {}
	disk_dic['{#DISKNAME}'] = diskname
	disk_dic_list.append(disk_dic)

disk_json = json.dumps(disk_dic_list, separators=(',', ':'))

diskjson_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_disk_discovery -o '".format(zabbix_server_ip, monitored_host_name) + disk_json + "'"
os.system(diskjson_cmd)

# Power Discovery
powerA_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -vsca|grep -Eo 'Bus.*Enclosure.*Power.*State'".format(EMC_manage_ip)).read().splitlines()
powerB_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -vscb|grep -Eo 'Bus.*Enclosure.*Power.*State'".format(EMC_manage_ip)).read().splitlines()
power_list = powerA_list + powerB_list
power_dic_list = []

for powername in power_list:
	power_dic = {}
	power_dic['{#POWERNAME}'] = powername
	power_dic_list.append(power_dic)

power_json = json.dumps(power_dic_list, separators=(',', ':'))

power_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_power_discovery -o '".format(zabbix_server_ip, monitored_host_name) + power_json + "'"
os.system(power_cmd)

# LCC Discovery
lccA_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -lcca|grep -Eo 'Bus.*Enclosure.*LCC.*State'".format(EMC_manage_ip)).read().splitlines()
lccB_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -lccb|grep -Eo 'Bus.*Enclosure.*LCC.*State'".format(EMC_manage_ip)).read().splitlines()
lcc_list = lccA_list + lccB_list
lcc_dic_list = []

for lccname in lcc_list:
	lcc_dic = {}
	lcc_dic['{#LCCNAME}'] = lccname
	lcc_dic_list.append(lcc_dic)

lcc_json = json.dumps(lcc_dic_list, separators=(',', ':'))
lcc_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_lcc_discovery -o '".format(zabbix_server_ip, monitored_host_name) + lcc_json + "'"
os.system(lcc_cmd)

# SP Discovery
spa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spa|grep -Eo 'SP.*State'".format(EMC_manage_ip)).read().splitlines()
spb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spb|grep -Eo 'SP.*State'".format(EMC_manage_ip)).read().splitlines()
sp_list = spa_list + spb_list
sp_dic_list = []

for spname in sp_list:
	sp_dic = {}
	sp_dic['{#SPNAME}'] = spname
	sp_dic_list.append(sp_dic)

sp_json = json.dumps(sp_dic_list, separators=(',', ':'))
sp_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_sp_discovery -o '".format(zabbix_server_ip, monitored_host_name) + sp_json + "'"
os.system(sp_cmd)

# SPS Discovery
spsa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsa|grep -Eo 'Bus.*Enclosure.*SPS.*State'".format(EMC_manage_ip)).read().splitlines()
spsb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -spsb|grep -Eo 'Bus.*Enclosure.*SPS.*State'".format(EMC_manage_ip)).read().splitlines()
sps_list = spsa_list + spsb_list
sps_dic_list = []

for spsname in sps_list:
	sps_dic = {}
	sps_dic['{#SPSNAME}'] = spsname
	sps_dic_list.append(sps_dic)

sps_json = json.dumps(sps_dic_list, separators=(',', ':'))
sps_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_sps_discovery -o '".format(zabbix_server_ip, monitored_host_name) + sps_json + "'"
os.system(sps_cmd)

# SPS Cable Discovery
spsa_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsa|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'".format(EMC_manage_ip)).read().splitlines()
spsb_cable_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cablingspsb|grep -Eo 'Bus.*Enclosure.*SPS.*Cabling.*State'".format(EMC_manage_ip)).read().splitlines()
sps_cable_list = spsa_cable_list + spsb_cable_list
sps_cable_dic_list = []

for spscable_name in sps_cable_list:
	sps_cable_dic = {}
	sps_cable_dic['{#SPSCABLENAME}'] = spscable_name
	sps_cable_dic_list.append(sps_cable_dic)

sps_cable_json = json.dumps(sps_cable_dic_list, separators=(',', ':'))
sps_cable_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_spscable_discovery -o '".format(zabbix_server_ip, monitored_host_name) + sps_cable_json + "'"
os.system(sps_cable_cmd)

# CPU Discovery
cpua_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpua|grep -Eo 'Bus.*Enclosure.*CPU.*State'".format(EMC_manage_ip)).read().splitlines()
cpub_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -cpub|grep -Eo 'Bus.*Enclosure.*CPU.*State'".format(EMC_manage_ip)).read().splitlines()
cpu_list = cpua_list + cpub_list
cpu_dic_list = []

for cpu_name in cpu_list:
	cpu_dic = {}
	cpu_dic['{#CPUNAME}'] = cpu_name
	cpu_dic_list.append(cpu_dic)

cpu_json = json.dumps(cpu_dic_list, separators=(',', ':'))
cpu_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_cpu_discovery -o '".format(zabbix_server_ip, monitored_host_name) + cpu_json + "'"
os.system(cpu_cmd)

# DIMM Discovery
dimma_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimma|grep -Eo 'Bus.*Enclosure.*DIMM.*State'".format(EMC_manage_ip)).read().splitlines()
dimmb_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -dimmb|grep -Eo 'Bus.*Enclosure.*DIMM.*State'".format(EMC_manage_ip)).read().splitlines()
dimm_list = dimma_list + dimmb_list
dimm_dic_list = []

for dimm_name in dimm_list:
	dimm_dic = {}
	dimm_dic['{#DIMMNAME}'] = dimm_name
	dimm_dic_list.append(dimm_dic)

dimm_json = json.dumps(dimm_dic_list, separators=(',', ':'))
dimm_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_dimm_discovery -o '".format(zabbix_server_ip, monitored_host_name) + dimm_json + "'"
os.system(dimm_cmd)

# I/O Discovery
ioa_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -ioa|grep -Eo 'Bus.*Enclosure.*I/O.*State'".format(EMC_manage_ip)).read().splitlines()
iob_list = os.popen("/opt/Navisphere/bin/naviseccli -h {0} getcrus -iob|grep -Eo 'Bus.*Enclosure.*I/O.*State'".format(EMC_manage_ip)).read().splitlines()
io_list = ioa_list + iob_list
io_dic_list = []

for io_name in io_list:
	io_dic = {}
	io_dic['{#IONAME}'] = io_name
	io_dic_list.append(io_dic)

io_json = json.dumps(io_dic_list, separators=(',', ':'))
io_cmd = "/usr/bin/zabbix_sender -z {0} -s {1} -k emc_io_discovery -o '".format(zabbix_server_ip, monitored_host_name) + io_json + "'"
os.system(io_cmd)
