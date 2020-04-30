#gets the html from the page of maine county coronavirus data and puts it in a text file called htext.txt

#import os commands for curl
import os

cmd = "curl 'https://www.google.com/search?client=ubuntu&hs=Y9p&sxsrf=ALeKk02iNo1zo5r28N8uVFuv59HYAt3QPg%3A1588167007653&ei=X4GpXseyJ6K1ggf6v6qwDw&q=maine+counties+covid+cases&oq=maine+counties+co&gs_lcp=CgZwc3ktYWIQARgAMgIIADoECAAQRzoECCMQJzoFCAAQkQI6BQgAEIMBOggIABCDARCRAjoHCAAQgwEQQzoECAAQQzoHCAAQFBCHAlCaKFjsR2D2U2gCcAR4AIAB6wKIAYcakgEIMC4xMy40LjKYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab' \
  -H 'authority: www.google.com' \
  -H 'cache-control: max-age=0' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/81.0.4044.129 Chrome/81.0.4044.129 Safari/537.36' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9' \
  -H 'sec-fetch-site: same-origin' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-user: ?1' \
  -H 'sec-fetch-dest: document' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'cookie: CGIC=CgZ1YnVudHUifHRleHQvaHRtbCxhcHBsaWNhdGlvbi94aHRtbCt4bWwsYXBwbGljYXRpb24veG1sO3E9MC45LGltYWdlL3dlYnAsaW1hZ2UvYXBuZywqLyo7cT0wLjgsYXBwbGljYXRpb24vc2lnbmVkLWV4Y2hhbmdlO3Y9YjM7cT0wLjk; SEARCH_SAMESITE=CgQIyI8B; SID=wQdYoXDNgmTrjjsEF3dt0GGzk59rO7Pt6xPtkOlVUm3wuyA5Y0-ZAOA3ZdvE-cbitXJC6g.; __Secure-3PSID=wQdYoXDNgmTrjjsEF3dt0GGzk59rO7Pt6xPtkOlVUm3wuyA5jEoqEIK7HNCaWjGfmEu0ag.; HSID=A7c0kMXSn96LUSgZ5; SSID=ARjOw8okg7ndpeQBb; APISID=N4R7gYnZndOV3aa-/ABi9fr307n20Nds5B; SAPISID=FQHRi0Sl6Liu2-vh/APBuEpy-zq1LgKhZF; __Secure-HSID=A7c0kMXSn96LUSgZ5; __Secure-SSID=ARjOw8okg7ndpeQBb; __Secure-APISID=N4R7gYnZndOV3aa-/ABi9fr307n20Nds5B; __Secure-3PAPISID=FQHRi0Sl6Liu2-vh/APBuEpy-zq1LgKhZF; S=billing-ui-v3=BT1ETo-2ltR5r_kWma4ioWpgOKk5QPri:billing-ui-v3-efe=BT1ETo-2ltR5r_kWma4ioWpgOKk5QPri; NID=203=Smwj5Xnrh9vKrAqxI3yXONlfIq1rqpAUyRs_o0ICnKxVss4j9lcWWtUOB-BHsUZmIVIkgG43vRghyv08_k2tVhfgoUBc7Qt3qiF0zubZZlJ6_9JccxfGbnFpvMotsWY9ARLIgf0V4v28ACrw_vtabkKtl8vKB46jKCkuyXMmUiRu8Cl2_QUdL5AXf62soD10p1QihA-KqvsEkHIGSP-OjEP9Lb4iixnS6K2fXmcK06Y67ZgiMMzIoxPhNOGlNtmKePdt0222SbqzEDsD; 1P_JAR=2020-4-30-0; DV=09hudAtkccBOELXrd6iumDRY34qJHNdjVnTH7KaekgEAANC2xIBQBvfv6AEAAOCjA3_71r3JfgAAAA; SIDCC=AJi4QfGt9Km_z7kZOCTViyjSkM9fv4j_ArgppjiO0Nz0Zse2DHRWkZoaDCq7B2TQiUX_tVRLew' \
  --compressed > htext.txt"

os.system(cmd)
