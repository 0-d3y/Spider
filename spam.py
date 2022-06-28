# 1ST TweakPY-Mr Sami
# All Apps
try:
	import requests,time,pyfiglet
	from colorama import Fore
except:
	print('تاكد من تحميل جميع المكاتب المطلوبه ')
total=1
def Rep_Insta(total):
	user=input("[ ? ] Username > ")
	pess=input("[ ? ] Password > ")
	target=input("[ ? ] attack > ")
	url_get_id = "https://i.instagram.com:443/api/v1/users/lookup/"
	head_get_id = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq",
	"X-IG-Capabilities": "3R4=", "Accept-Language": "ar-sa",
	"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
	"User-Agent": "Instagram 99.4.0 Filza_TweakPY (Filza_TweakPY)",
	"Accept-Encoding": "gzip, deflate"}
	data_get_id={"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % target}            
	req=requests.post(url_get_id, headers=head_get_id, data=data_get_id)
	try:
		target_id=str(req.json()['user_id'])
	except:
		pass
		exit("[!!] Error getting Target ID Retry Later (Ban/Normal Error) ")
	log='https://www.instagram.com/accounts/login/ajax/'
	log_h={
		'Host': 'www.instagram.com',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
		'Accept': '*/*',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'X-CSRFToken': '5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect',
		'X-Instagram-AJAX': '1d6caaf37cd2',
		'X-IG-App-ID': '936619743392459',
		'X-ASBD-ID': '437806',
		'X-IG-WWW-Claim': '0',
		'Content-Type': 'application/x-www-form-urlencoded',
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Length': '347',
		'Origin': 'https://www.instagram.com',
		'Connection': 'keep-alive',
		'Referer': 'https://www.instagram.com/accounts/login/',
		'Cookie': 'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken=5o7PN96Y9Ln95EnlXN6t0pmCHDqdbect; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1',
		'TE': 'Trailers'}
	log_dat={
		'username': user,
		'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{pess}',
		'queryParams': "{}",
		'optIntoOneTap': 'false',
		'stopDeletionNonce ': "",
		'trustedDeviceRecords': "{}"}
	req1=requests.post(log, headers=log_h, data=log_dat)
	try:		
		if '"authenticated":true' in req1.text:
			csrf=req1.cookies['csrftoken']
			sess=req1.cookies['sessionid']
			userid=req1.json()['userId']		
		elif ('checkpoint_required') in req1.text:
			print('Sicor 🔑')	
			exit()
		elif ('"user":true,"authenticated":false') in req1.text:
			print('Not Password ❌')		
			exit()	
		elif ('"user":false') in req1.text:
			print('Not User ❌') 
			exit()
	except:
		pass
		print("[!] Error Getting id/csrftoken ")
		print("[>] Try Another Account or Check Your Password and Username")
		exit()
	url='https://www.instagram.com/reports/web/get_frx_prompt/'
	head={
		'Host': 'www.instagram.com',
		'Cookie': f'ig_did=7B796F1F-ADE7-429C-8ADB-9B131663E5E4; datr=2kDRYNWmjctteBSnOqogPrxv; csrftoken={csrf}; mid=YNIa4QALAAGoeESFP8axY9NfC9t3; ig_nrcb=1; ds_user_id={userid}; sessionid={sess}; shbid="19399\05448526341466\0541657548493:01f765eb2fb0f52402149d7667ceb064bc56c1a422fc410f2a66fe68999c5cddaeb410b2"; shbts="1626012493\05448526341466\0541657548493:01f7e1c3ad7a57e6f558f05d8c9e6c00121a3a308e818c4c27918b95f7c09e38daba9815"; rur="VLL\05448526341466\0541657639760:01f790b1d824dd12c35339c0adf06665245ba76f59fd9f49557f1d7e258a635e96aa9b9',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
		'Accept': '*/*',
		'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
		'Accept-Encoding': 'gzip, deflate',
		'X-Csrftoken': f'{csrf}',
		'X-Instagram-Ajax': '595724a46b58',
		'X-Ig-App-Id': '936619743392459',
		'X-Asbd-Id': '437806',
		'X-Ig-Www-Claim': 'hmac.AR13pf0XdQA_XNAYLrmGWOJtWRr9WkLRRw_dNGcK6i1C5a_k',
		'Content-Type': 'application/x-www-form-urlencoded',
		'X-Requested-With': 'XMLHttpRequest',
		'Content-Length': '3131',
		'Origin': 'https://www.instagram.com',
		'Referer': f'https://www.instagram.com/{target}/',
		'Te': 'trailers',
		'Connection': 'close'}
	data=f'entry_point=1&location=2&object_type=5&object_id={target_id}&container_module=profilePage&context=%7B%22tags%22%3A%5B%22ig_report_account%22%2C%22ig_its_inappropriate%22%2C%22ig_self_injury_v3%22%5D%2C%22ixt_context_from_www%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22{sess}%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_its_inappropriate%5C%5C%5C%22%2C%5C%5C%5C%22ig_self_injury_v3%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22{target_id}%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841448643985792%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A17841400668013122%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_US%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A11%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profilePage%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22None%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A936619743392459%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3A%5C%5C%5C%22JrTVqcbpAhgMNS4xNjMuMTE4LjgyGE5Nb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjo4OS4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94Lzg5LjAYBWVuX1VTHBggZjZjZjZhMzUzYzlmNDFiYWMyZjcxY2JkYzU0MGQyNjMYIDliMWEzMDMxNzllYTJhNjFiN2JjYjI1MzBmNWQ0MDU3GCBkMGM4NDY2NTgyOTIzODgyODgyNThiNjI0M2M3MDlhMhgAFfaGAwA8LBgcWU5JYTRRQUxBQUdvZUVTRlA4YXhZOU5mQzl0MxbQ%2B8fLxl4AHBUUKwAAIjw5FQAZFQA5FQAAGCAyYjljMjZlOWQzODk0NTE5ODAxYjU3OGZlYTdlOGNmMBUCERIYDzkzNjYxOTc0MzM5MjQ1ORwWoNT6wKXwtj8YQGYyOGViNTc3YzYwYmRjMWI0MDg1MzA5NWIzNDhmNWY0ODQzNWE4MmQzOGU5ZWRkZTc0NzMxNGI4ZjdjNmE4YzYAHBUEABIoIGh0dHBzOi8vd3d3Lmluc3RhZ3JhbS5jb20vcmFfMjMvGA5YTUxIdHRwUmVxdWVzdAAWgIagi%5C%5C%5C%5C%5C%5C%5C%2F%2BssT8oHC9yZXBvcnRzL3dlYi9nZXRfZnJ4X3Byb21wdC8WLBaA5sWPDAA%3D%5C%5C%5C%22%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Anull%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_policy_education%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profilePage%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22{sess}%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D&action_type=2&frx_prompt_request_type=4'
	while True:
		try:
			time.sleep(10)
			req=requests.post(url,headers=head,data=data)
			if req.json()['status']=="ok":
				print(f"\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.CYAN}Total number of notifications{Fore.RESET} [{Fore.GREEN}{total}{Fore.RESET}]",end='')
				total+=1
			else:
				print(f'\n [!] Error Report')
		except NameError:print("\n [-] Ban/Error")
		except KeyError:print("\n [-] Ban/Error")
def main():	
	print(f"""
	       

{pyfiglet.figlet_format('T . Y . G - SPAM')}
                     Web : cyberyemen.blogspot.com
                          By <\> @TYG_TEAM
               
	""")
	print("-"*40)
main()
Rep_Insta(total)
