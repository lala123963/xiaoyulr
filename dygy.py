import datetime
import json
import os
import random
import time
import hashlib
import requests
import pprint

headers = {
    'referer': 'https://tmaservice.developer.toutiao.com/?appid=tte684903979bdf21a02&version=1.0.12',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Pixel 4 Build/QD1A.190821.007; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.3620.9.0 ToutiaoMicroApp/2.53.1.0 PluginVersion/209001',
    # 'content-type': 'application/json',
    # 'Accept-Encoding': 'br, gzip',
    'Host': 'minigame.zijieapi.com',
    # 'Connection': 'Keep-Alive',
    'Cookie': 'odin_tt=e6fb199b84cfbea49c72884bbd44c2c6f6ac5ab649e0bfa160199f2d75cd582d8f3ad7acded72d4f984ed06bae624e2f65c262568e7069301cb5b07740aab6da; install_id=3980686141954494; ttreq=1$7bd75ef2bd643d38942207b07728aad96457cc5a; uid_tt=c0890449f72ccf9013b7b10430dfda2e; sid_guard=8dc94c878f4f038210854dddf3721bd4%7C1654399890%7C5139965%7CWed%2C+03-Aug-2022+15%3A17%3A35+GMT; sid_tt=8dc94c878f4f038210854dddf3721bd4; sessionid=8dc94c878f4f038210854dddf3721bd4',

}


##首页图标
def polling_info():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/polling_info"
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        print('登录成功,开始抖音果园任务')


##七天登录奖励
def sign():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/sign_in/reward?watch_ad=0&extra_ad_num=0&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        day = response['data']["reward_item"]["id"]
        reward_water = response['data']["reward_item"]["num"]
        print(f'签到第{day}获得{reward_water}水滴')
    else:
        print(response["message"])


##选择奖励宝箱
def choose_box_reward():
    compare = []
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/challenge/list?os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    # pprint.pprint(response)
    if response["status_code"] == 0:
        datas = response["data"]["tasks"]
        for i in datas:
            id = i["id"]
            reward_water = i["reward_water"]
            water_times = i["water_times"]
            compare.append([id, reward_water,water_times])
            # print(id, reward_water, water_times)
    # print(compare)
    if compare[0][1] > compare[1][1]:
        id = compare[0][0]
        reward_water = compare[0][1]
        num = compare[0][2]
        print(f'选择{id}号需要浇水{num}次宝箱的{reward_water}水滴宝箱任务')
        url = f"https://minigame.zijieapi.com/ttgame/game_orchard_ecom/challenge/choose?task_id={str(id)}&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
        response = requests.get(url=url, headers=headers).json()
        if response["status_code"] == 0:
            print("挑战开始")
    else:
        id = compare[1][0]
        reward_water = compare[1][1]
        num = compare[1][2]
        print(f'选择{id}号需要浇水{num}次宝箱的{reward_water}水滴宝箱任务')
        url = f"https://minigame.zijieapi.com/ttgame/game_orchard_ecom/challenge/choose?task_id={str(id)}&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
        response = requests.get(url=url, headers=headers).json()
        if response["status_code"] == 0:
            print("挑战开始")



##挑战礼包奖励
def recive_box_reward():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/challenge/reward?os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    # print(response)
    if response["status_code"] == 0:
        reward_water = response['data']["reward_item"]["num"]
        print(f'获得挑战礼包{reward_water}水滴成功')
    else:
        print(response['message'])


##领取储水池奖励有问题
def reward_bottle():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/water_bottle/reward?os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    pprint.pprint(response)
    if response["status_code"] == 0:
        reward_water = response['data']['reward_item']["num"]
        print(f'获得储水瓶{reward_water}水滴成功')
    else:
        print(response['message'])


##水车找水滴:
def waterwheel():
    for i in range(20):
        try:
            url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/scene/touch?scene_id=1&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
            response = requests.get(url=url, headers=headers).json()
            # pprint.pprint(response)
            if response["data"]["reward_item"] is None:
                print('什么也没找到')
            else:
                reward_water = response["data"]["reward_item"]["num"]
                print(f'水车获得{reward_water}水滴成功')
            time.sleep(random.randint(1, 3))
        except:
            continue


##签到领化肥
def sign_fertilizer():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/nutrient/sign_in?os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        print("签到成功")
    else:
        print(f"已签到或者{response['message']}")


##水滴日常任务领5次水滴
def day_water():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/tasks/reward?task_id=1&do_action=0&extra_ad_num=0&version=11&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    # pprint.pprint(response)
    if response["status_code"] == 0:
        reward_water = response["data"]["reward_item"]["num"]
        print(f'每日免费领水滴{reward_water}水滴成功')
    else:
        print(response['message'])


##三餐礼包
def eat():
    url = "https://minigame.zijieapi.com/ttgame/game_orchard_ecom/tasks/reward?task_id=2&do_action=1&extra_ad_num=0&version=11&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        reward_water = response["data"]["reward_item"]["num"]
        print(f'领取三餐礼包{reward_water}水滴成功')
    else:
        print(response['message'])


##每日领奖励及浇水10次奖励,每次请求一次
def water_award():
    url = 'https://minigame.zijieapi.com/ttgame/game_orchard_ecom/box/open?os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900'
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        reward_water = response["data"]["reward_item"]["num"]
        print(f'领取浇水次数礼包{reward_water}水滴成功')
    else:
        print(response['message'])


def watering(i=1):
    num = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]
    if (i-1) / 10 in num:
        water_award()
    url = f"https://minigame.zijieapi.com/ttgame/game_orchard_ecom/tree/water?version=11&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900"
    response = requests.get(url=url, headers=headers).json()
    # pprint.pprint(response)
    if response["message"] == "success":
        water = response['data']['kettle']['water_num']
        if water != 0:

            print(f"进行第{i}次浇水,水瓶还剩{water}滴水")
            time.sleep(random.randint(3, 5))
            watering(i=i + 1)
        else:
            print('水瓶水不足停止浇水')
            return

##使用化肥
def use_fertilizer():
    url="https://minigame.zijieapi.com/ttgame/game_orchard_ecom/use/fertilizer?fertilizer_type=4"
    response = requests.get(url=url, headers=headers).json()
    # pprint.pprint(response)
    if response["status_code"] == 0:
        print('施肥成功')


##判断是否用化肥化肥
def judy_fertilizer():
    # url="https://minigame.zijieapi.com/ttgame/game_orchard_ecom/use/fertilizer?fertilizer_type=4"
    url="https://minigame.zijieapi.com/ttgame/game_orchard_ecom/polling_info"
    response = requests.get(url=url, headers=headers).json()
    lite = response['data']['fertilizer']['lite']
    if int(lite) > 0:
        use_fertilizer()
        # pprint.pprint(response)

##完成度
def target():
    url = 'https://minigame.zijieapi.com/ttgame/game_orchard_ecom/home_info?version=11&os_version=10&version_code=200900&device_id=708526086828733&iid=3980686141954494&app_name=aweme&device_platform=android&device_type=Pixel%204&channel=sem_shenma_dy_ls146&aid=1128&ac=wifi&version_name=20.9.0&update_version_code=20909900'
    response = requests.get(url=url, headers=headers).json()
    if response["status_code"] == 0:
        reward_water = response["data"]["info"]["progress"]
        current_water=reward_water["current"]
        target_water = reward_water["target"]
        print(f'目前已浇水{current_water}目标为{target_water}还差{int(target_water)-current_water}水滴可以成功兑换水果')
        return f'目前已浇水{current_water}目标为{target_water}还差{int(target_water)-current_water}水滴可以成功兑换水果'



def push_plus_bot(content,push_token):
    b = content
    headers = {
        "Host": "www.pushplus.plus",
        "Origin": "http://www.pushplus.plus",
        "Referer": "http://www.pushplus.plus/push1.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44",
        "X-Requested-With": "XMLHttpRequest",

    }
    url = 'http://www.pushplus.plus/api/send'
    data = {
        "token": push_token,
        "title": '抖音果园任务',
        "content": b,
        "channel": "wechat",
        "template": "html",
        'webhook': ""
    }
    body = json.dumps(data).encode(encoding='utf-8')
    # headers = {'Content-Type': 'application/json'}
    response = requests.post(url=url, data=body, headers=headers).json()
    # print(response)
    if response['code'] == 200:
        print('推送成功！')
    else:
        print('推送失败！')


if __name__ == '__main__':
    cks = os.environ['dygyCookies'].split('@')
    push_token = os.environ['push_token']
    for ck in cks:
        headers1 = {
            'Cookie': ck,
        }
        headers.update(headers1)
        print('抖音浇水任务开始,开始点击首页图标')
        polling_info()
        start_time = datetime.datetime.now().strftime('%H')
        if start_time == '06':
            print('开始领取水滴日常任务奖励')
            day_water()
            time.sleep(random.randint(1, 4))
            print('开始水车任务')
            waterwheel()
        elif start_time == '07':
            print('开始收集蓄水池任务')
            reward_bottle()
        elif start_time == '08':
            print('开始领取水滴日常任务奖励')
            day_water()
            time.sleep(random.randint(1,4))
            print('开始七天登录奖励')
            sign()
            time.sleep(random.randint(1, 4))
            print('选择宝箱奖励任务')
            choose_box_reward()
            time.sleep(random.randint(1, 4))
            print('开始领点击水车任务')
            waterwheel()
            time.sleep(random.randint(1, 4))
            print('签到领化肥')
            sign_fertilizer()
            time.sleep(random.randint(1, 4))
            print('开始领取水滴日常任务奖励')
            day_water()
            time.sleep(random.randint(5, 10))
            print('开始三餐领取任务')
            eat()
            time.sleep(random.randint(1, 4))
            print('开始每日领取宝箱奖励任务')
            judy_fertilizer()
            time.sleep(random.randint(1, 4))
            print('开始推送信息')
            message = target()
        elif start_time == '12':
            print('开始三餐领取任务')
            eat()
            time.sleep(random.randint(1, 4))
            waterwheel()
            time.sleep(random.randint(2, 6))
            print('开始领取水滴日常任务奖励')
            day_water()
        elif start_time == '18':
            print('开始三餐领取任务')
            eat()
            time.sleep(random.randint(1, 4))
            waterwheel()
            time.sleep(random.randint(2, 6))
            print('开始领取水滴日常任务奖励')
            day_water()
        elif start_time == '19':
            print('开始领取挑战宝箱奖励')
            recive_box_reward()
        elif start_time == '21':
            time.sleep(random.randint(2, 6))
            print('开始领取水滴日常任务奖励')
            day_water()
            time.sleep(random.randint(1, 4))
            print('继续浇完剩余水量')
            watering()
            print('开始推送信息')
            message = target()
            push_plus_bot(message,push_token)



"""
ff668ac51ae0c803&eyJleHAiOjE2NTQ5MTkwNjEsImtpZCI6MCwiYWxnIjoiSFMyNTYifQ.eyJ1aWQiOiI4ODgyNTIwNiIsIm9wZW5pZCI6Im9ZYlZMeExnZThibWFINFhvSVQyMDdQWlJyV3ciLCJleHAiOjE2NTQ5MTkwNjF9.z7QV2gTs2U4tc9OyX02i6kCpw3H7qo7vfQWGe4Itx-g&eyJleHAiOjE2NjI2OTMyNjEsImFsZyI6IkhTMjU2In0.eyJ1aWQiOiI4ODgyNTIwNiIsIm9wZW5pZCI6Im9ZYlZMeExnZThibWFINFhvSVQyMDdQWlJyV3ciLCJleHAiOjE2NjI2OTMyNjF9.7CESzUCev6obxvP-vJWQw1elM2Jcj2jAlzoN6ORiy40
"""
