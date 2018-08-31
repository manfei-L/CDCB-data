import csv
import json

CHUNCK_SIZE = 10**5
byte_array = []

def parse_header_1(byte_array, i, row):
	keep = True
	# row.append(''.join(map(str, byte_array[i])))
	# row.append(''.join(map(str, byte_array[i+1])))
	row.append(''.join(map(str, byte_array[i+2:i+4])))
	# row.append(''.join(map(str, byte_array[i+4:i+7])))
	row.append(''.join(map(str, byte_array[i+7:i+19])))
	# row.append(''.join(map(str, byte_array[i+19:i+21])))
	# row.append(''.join(map(str, byte_array[i+21:i+24])))
	# row.append(''.join(map(str, byte_array[i+24:i+36])))
	# row.append(''.join(map(str, byte_array[i+36:i+38])))
	# row.append(''.join(map(str, byte_array[i+38:i+41])))
	# row.append(''.join(map(str, byte_array[i+41:i+53])))
	# row.append(''.join(map(str, byte_array[i+53:i+55])))
	# row.append(''.join(map(str, byte_array[i+55:i+58])))
	# row.append(''.join(map(str, byte_array[i+58:i+70])))
	row.append(''.join(map(str, byte_array[i+70:i+78])))
	if (''.join(map(str, byte_array[i+70:i+74])) < '2008'):
		keep = False
	# row.append(''.join(map(str, byte_array[i+78])))
	# row.append(''.join(map(str, byte_array[i+79:i+87])))
	# row.append(''.join(map(str, byte_array[i+87])))
	# row.append(''.join(map(str, byte_array[i+88])))
	# row.append(''.join(map(str, byte_array[i+89])))
	row.append(''.join(map(str, byte_array[i+90:i+91])))
	# row.append(''.join(map(str, byte_array[i+91:i+93])))
	# row.append(''.join(map(str, byte_array[i+93:i+99])))
	# row.append(''.join(map(str, byte_array[i+99])))
	# row.append(''.join(map(str, byte_array[i+100])))
	# row.append(''.join(map(str, byte_array[i+101:i+103])))
	# row.append(''.join(map(str, byte_array[i+103:i+106])))
	row.append(''.join(map(str, byte_array[i+106:i+108])))
	row.append(''.join(map(str, byte_array[i+108:i+110])))
	# row.append(''.join(map(str, byte_array[i+110:i+114])))
	row.append(''.join(map(str, byte_array[i+114:i+119])))
	row.append(''.join(map(str, byte_array[i+119:i+125])))
	row.append(''.join(map(str, byte_array[i+125:i+126])))
	


	return ''.join(map(str, byte_array[i+87:i+88])), ''.join(map(str, byte_array[i+125:i+126])), keep


def parse_header_2(byte_array, i, row):
	row.append(''.join(map(str, byte_array[i:i+1])))
	row.append(''.join(map(str, byte_array[i+1:i+9])))
	row.append(''.join(map(str, byte_array[i+9:i+12])))
	row.append(''.join(map(str, byte_array[i+12:i+15])))
	# row.append(''.join(map(str, byte_array[i+15:i+17])))
	# row.append(''.join(map(str, byte_array[i+17:i+20])))
	row.append(''.join(map(str, byte_array[i+20:i+24])))
	row.append(''.join(map(str, byte_array[i+24:i+28])))
	row.append(''.join(map(str, byte_array[i+28:i+32])))
	row.append(''.join(map(str, byte_array[i+32:i+34])))
	row.append(''.join(map(str, byte_array[i+34:i+35])))
	row.append(''.join(map(str, byte_array[i+35:i+43])))
	row.append(''.join(map(str, byte_array[i+43:i+46])))
	row.append(''.join(map(str, byte_array[i+46:i+47])))
	row.append(''.join(map(str, byte_array[i+47:i+48])))
	row.append(''.join(map(str, byte_array[i+48:i+49])))
	row.append(''.join(map(str, byte_array[i+49:i+51])))
	row.append(''.join(map(str, byte_array[i+51:i+52])))
	# row.append(''.join(map(str, byte_array[i+52:i+57])))
	# row.append(''.join(map(str, byte_array[i+57:i+58])))
	row.append(''.join(map(str, byte_array[i+58:i+59])))
	row.append(''.join(map(str, byte_array[i+59:i+60])))
	row.append(''.join(map(str, byte_array[i+60:i+61])))
	row.append(''.join(map(str, byte_array[i+61:i+66])))
	row.append(''.join(map(str, byte_array[i+66:i+70])))
	row.append(''.join(map(str, byte_array[i+70:i+74])))
	# row.append(''.join(map(str, byte_array[i+74:i+80])))
	# row.append(''.join(map(str, byte_array[i+80:i+85])))
	# row.append(''.join(map(str, byte_array[i+85:i+90])))
	# row.append(''.join(map(str, byte_array[i+90:i+94])))
	# row.append(''.join(map(str, byte_array[i+94:i+101])))
	# row.append(''.join(map(str, byte_array[i+101:i+105])))
	# row.append(''.join(map(str, byte_array[i+105:i+107])))
	row.append(''.join(map(str, byte_array[i+107:i+109])))
	row.append(''.join(map(str, byte_array[i+109:i+112])))
	row.append(''.join(map(str, byte_array[i+112:i+115])))
	row.append(''.join(map(str, byte_array[i+115:i+116])))
	row.append(''.join(map(str, byte_array[i+116:i+117])))
	row.append(''.join(map(str, byte_array[i+117:i+118])))
	#row.append(''.join(map(str, byte_array[i+244:i+248])))
	row.append(''.join(map(str, byte_array[i+122:i+124])))

	return ''.join(map(str, byte_array[i+122:i+124]))


def parse_data(byte_array, i, segment):
	segment['dim_test'] = ''.join(map(str, byte_array[i:i+3]))
	segment['supervision_code'] = ''.join(map(str, byte_array[i+3]))
	segment['last_test_status_code'] = ''.join(map(str, byte_array[i+4]))
	segment['milking_freq'] = ''.join(map(str, byte_array[i+5]))
	segment['num_milking_weighted'] = ''.join(map(str, byte_array[i+6]))
	segment['num_milking_sample'] = ''.join(map(str, byte_array[i+7]))
	segment['num_MRD'] = ''.join(map(str, byte_array[i+8:i+10]))
	segment['percent_milk_shipped'] = ''.join(map(str, byte_array[i+10:i+13]))
	segment['actual_milk_yield'] = ''.join(map(str, byte_array[i+13:i+17]))
	segment['actual_fat_percent'] = ''.join(map(str, byte_array[i+17:i+19]))
	segment['actual_protein_percent'] = ''.join(map(str, byte_array[i+19:i+21]))
	segment['actual_SCS'] = ''.join(map(str, byte_array[i+21:i+23]))

def check_size(size, byte_array, arr_length, i, f):
	if (i + size > arr_length):
		temp_array = f.read(CHUNCK_SIZE - size)
		# print(byte_array[i:])
		# print(type(byte_array[i:]))
		byte_array = byte_array[i:] + temp_array
		arr_length = len(byte_array)
		i = 0

	return byte_array, i, arr_length

output_f = open("reed20180705_2.csv", 'w')
w = csv.writer(output_f)
header = [
		  'animal_breed_code',
		  'animal_id_number',
		  'birth_date(YYYMMDD)',
		  'multiple_birth_code',
		  'herd_state_code',
		  'herd_county_code',
		  'cow_ctrl_number',
		  'date_cow_left(YYMMDD)',
		  'lactation_type_code',
		  'lactation_verify_code',
		  'calving_date(YYYYMMDD)',
		  'DIM',
		  'days_dry_prior',
		  'actual_milk_yield/10',
		  'actual_fat_yield',
		  'actual_protein_yield',
		  'lactation_num',
		  'primary_dest_group/term_code',
		  'date_breeding_conception(YYYYMMDD)',
		  'body_weight_start',
		  'weight_report_code',
		  'lactation_init_code',
		  'milking/dry_status',
		  'type_of_test_plan_code',
		  'type_lactation_sc_score',
		  'true_protein_code',
		  'test_method_code',
		  'qc_status',
		  'lactation_std_milk_yield',
		  'lactation_std_fat_yield',
		  'lactation_std_protein_yield',
		  'num_tests_components_taken',
		  'DCR_for_yield',
		  'DCR_for_somatic_cell',
		  'preg_confirm_code',
		  'num_progeny_born',
		  'second_term_code',
		  'num_seg_test_days',
		  'seg_data(JSON)']

w.writerow(header)

count = 0
i = 0

with open("reed20180705.fmt4", "rb") as f:
	byte_array = f.read(CHUNCK_SIZE)
	arr_length = len(byte_array)
	while arr_length != 0:
		while (i < arr_length and byte_array[i] == '\n'):
			i = i + 1
		row = []
		byte_array, i, arr_length = check_size(126, byte_array, arr_length, i, f)
		while (i < arr_length and byte_array[i] == '\n'):
			i = i + 1
		if (arr_length == 0):
			exit()
		record_type, lactation_type, keep = parse_header_1(byte_array, i, row)
		i = i + 126
		if (record_type in ['X', 'L', 'R', 'Y', 'C'] and lactation_type in ['0', '1', '2', '5', '6', '7', '8']):
			byte_array, i, arr_length = check_size(124, byte_array, arr_length, i, f)
			seg_count = int(parse_header_2(byte_array, i, row))
			segments = {}
			i = i + 124
			if (keep):
				byte_array, i, arr_length = check_size(23*seg_count, byte_array, arr_length, i, f)
				for j in range(seg_count):
					seg_num = 'test_day' + str(j)
					segments[seg_num] = {}
					parse_data(byte_array, i, segments[seg_num])
					i = i + 23
				# row.append(str(segments).replace('\'', '\"'))
				row.append(str(json.dumps(segments)))
				w.writerow(row)
				count = count + 1
			else:
				byte_array, i, arr_length = check_size(23*seg_count, byte_array, arr_length, i, f)
				i = i + 23*seg_count

		if (count == 20000):
			exit()