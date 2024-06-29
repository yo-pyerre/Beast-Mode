python3 getPhoneBills.py (startMonth as yyyy-mm) (endMonth as yyyy-mm)?

Couldn't figure out how to get auth to work

For now:
1) Log on to [AT&T](https://www.att.com/acctmgmt/billing/mybillingcenter) manually
   2) Credentials in "login.txt"
2) Open DevTools -> Network
3) Find and click ~= "Download as PDF -> Download as Regular PDF"
4) Copy the request made to "v2/billOrchestrator/downloadpdf"
5) Copy/paste the cookie string into curl command in "download_att.sh"
6) Run getPhoneBills.py