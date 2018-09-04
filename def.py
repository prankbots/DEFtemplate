HOST = 'https://gwk.line.naver.jp'
LA = "BIZIOS\t1.7.5\tiOS\t10.2"
udidHash = ""
header = {
    'Accept': "application/json",
    "x-lal": "ja-JP_JP",
    "X-LHM": 'POST',
    "X-LPV": '1',
    'X-Line-Application': LA
}
line = LINE()
channel_token = line.channel.approveChannelAndIssueChannelToken('1526709289').channelAccessToken

endpoint = '/plc/api/core/auth/cmsToken'
payload = {"channelAccessToken": channel_token, "udidHash": udidHash}
res = requests.post(HOST+endpoint, data=json.dumps(payload), headers=header)
print(res.json()['accessToken'])
