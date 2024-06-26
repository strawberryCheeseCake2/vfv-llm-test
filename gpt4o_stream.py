from openai import OpenAI, AssistantEventHandler
from typing_extensions import override
from time import time

from secrets import openai_api_key
from examples import pref_ko_point

client = OpenAI(api_key=openai_api_key)

input("sdf: ")
prev = time()
stream = client.chat.completions.create(
    model="gpt-4o",
    messages=pref_ko_point,
    stream=True,
)
counter = 0
# prev = time()

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        if counter <= 5:
            print("FIRST!!!!!")
            print(chunk.choices[0].delta.content)
            print(time()-prev)
            print()
            counter += 1
        
        print(chunk.choices[0].delta.content, end='')


# Time to First Token: 0.83s
"""
 회사가 비대면 근무를 도입해야 한다고 주장하시면서 출퇴근 시간을 절약할 수 있다는 점을 강조하셨습니다. 하지만, 비대면 근무를 도입하게 되면 회사의 팀워크와 직원들 간의 소통이 크게 저하될 수 있다는 점도 고려해야 합니다. 오프라인에서 직접적인 대면으로 소통하는 것이 보다 효과적인 의사소통을 가능하게 하고, 직접 만나서 협업하는 과정에서 더 창의적이고 혁신적인 아이디어가 나올 가능성이 높습니다. 

또한, User 2님도 동의합니다만, 비대면 근무의 장점만을 보고 결정을 내리는 것은 위험할 수 있습니다. 비대면 근무로 인해 직원들이 업무와 사생활의 경계를 명확히 하지 못하게 될 수도 있으며, 이로 인해 업무 효율성과 직원 만족도가 오히려 하락할 수 있습니다.
"""

# 스트림을 할 것인가 (첫 토큰 1초안에 끊김) (O)
# 어시스턴트 api를 쓸 것인가 (gen+0.5~1s) (X)
# 2-3 문장 이내로 줄이라고 할 것인가 (1~2s) (O)