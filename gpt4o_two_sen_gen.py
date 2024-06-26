from openai import OpenAI, AsyncOpenAI
from openai.types.beta.threads.message import Message
from openai.pagination import SyncCursorPage
from typing import Optional, List

from secrets import openai_api_key
import asyncio

from examples import gender_two_sen, gender_ko_two_sen, pref_ko_two_sen, pref_two_sen, pref_ko_two_sen_point

from time import time


class DevilManager:
    def __init__(self):
        self.__client = AsyncOpenAI(api_key=openai_api_key)

    async def run_devill(self, messages):
        response = await self.__client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )

        choices = response.choices

        if len(choices) > 0:
            return choices[0].message.content
        else:
            return None


devil = DevilManager()


async def test():
    tmp = time()
    answer = await devil.run_devill(pref_ko_two_sen_point)
    tmp2 = time()
    print(tmp2 - tmp)
    print(answer)

asyncio.run(test())


# [Gender]
# Elasped Time: 1.0774354934692383s
"""
Giving preferential treatment to women in promotions is actually necessary in order to rectify historical gender imbalances and ensure a diverse and inclusive workplace. Without these measures, the meritocracy some claim to value would only perpetuate existing biases and systemic inequalities.
"""

# [Preference]
# Elasped Time: 3.778681755065918s
"""
Remote work, while appealing superficially, threatens to erode company culture and employee cohesion. The lack of in-person interaction can lead to miscommunication, decreased collaboration, and ultimately, a reduction in overall productivity and innovation.
"""

# [Gender(korean)]
# Elapsed Time: 1.7516090869903564
"""
대학 시절부터 성차별을 경험한 여성은 커리어 초기에 이미 많은 어려움을 겪기 때문에, 인사 발령 시 특혜는 평등한 출발선을 보장하기 위한 필수적인 조치입니다. 특혜가 없으면, 시스템 속에 내재된 불평등을 바로잡을 기회를 잃게 됩니다.
"""

# [Preference(korean)]
# Elapsed Time: 1.6667735576629639s
"""
User 3: 사실, 대면 근무는 팀워크와 아이디어 교환을 촉진시켜 더 혁신적인 결과를 만들어낼 수 있습니다. 비대면 근무는 직원 간의 유대와 소속감을 약화시키고 소통의 미묘한 뉘앙스를 놓칠 가능성이 높습니다. 결국, 생산성과 창의성 면에서 회사가 크게 손해 볼 수 있습니다.
"""


# [Preference(korean), 지적하도록]
# Elapsed Time: 1.4s

"""
User 1, 비대면 근무가 출퇴근 시간을 절약해주는 것은 사실이지만, 팀워크와 실시간 의사소통이 감소할 수 있습니다. 특정 상황에서는 협업의 효율성이 떨어져 업무 결과물의 질이 저하될 수 있습니다.
"""


# [Speed]
# 짧으면 1초, 길면 3~4초, 3.5-turbo 쓰면 조금 더 줄어듬
# 생각보다 한국어 영어 속도 별차이 없고, 조건 추가도 시간에 별 영향 없음

# [Quality]
# 딱 주장, 근거만 말함.

# => 프롬프트 연구가 조금더 필요, 속도는 이것도 그냥 쓰지는 못함
